#!/usr/bin/env python3
"""Grade skill replies against Goa testbank files. Python 3 standard library only.

Checker v1.2 (October 14, 2026, red-team fixes). Changelog:
  v1.2  - no_new_numbers strips a label number only when it is clearly structural: Email, Follow-up,
          Step, Option, Post or Version + N at the start of a line (after any bullet, "#" or "**") or
          inside a bold span on one line ("**Message, version 2**"). Everything else is checked
          again, so an invented "day 15", "no. 12", "table 4", "week 2" or "3-day offer" fails (T11).
        - Counter stripping is bounded: "(35 words, 168 characters)", "64 words", "120 characters",
          "64/500 characters" and "(12/25)". It no longer eats the rest of a line, and "10/50 rooms"
          or "450 / 500 large" are checked (T12).
        - One digit fold for every content check (contains, not_contains, regex, not_regex, min_blanks,
          no_new_numbers), applied to reply, prompt and contains values alike: Indic and other Unicode
          decimal digits and full-width forms become ASCII, and zero-width characters next to digits are
          dropped. Length checks still measure the reply as given.
        - Times: 10:30 = 10.30 and 8:00 = 8. "24/7" is not a number. Crore/cr (x 10^7) and an attached
          L ("1.5L" = 150000) are read (T21). Number words ("three nights") are still not checked.
        - Report: checker version, responses provenance (no model recorded = reference answers, not a
          model run), and the count of unscored judge checks.
  v1.1  - (kept as check_v1_1.py) label and counter exclusions; too broad, see T11/T12.
  v1.0  - (kept as check_v1_0.py) first version.
Cases were pre-registered; the checker was revised after first results. Always say which checker
version produced a number, and report it next to the other versions when comparing.

Usage:
  python3 check.py --responses responses.json testbank/*.json [--out report.md]
  python3 check.py -r run1.json -r run2.json testbank/*.json      # two replicates

responses.json: {"responses": {"<case id>": "<reply text>", ...}}
Testbank files use the common schema in 01-WAVE-1-1-ADDENDUM.md:
  {"suite","version","date","cases":[{"id","skill","archetype","kind","prompt","expected","checks":[...]}]}

Check types: contains, not_contains, regex, not_regex, max_words, max_chars,
no_new_numbers, min_blanks, judge (skipped and listed).
Matching rules:
  contains / not_contains  case-insensitive substring.
  regex / not_regex        Python re, MULTILINE, case-sensitive unless the pattern has (?i).
  max_words                whitespace-separated tokens.
  max_chars                len() of the reply as given.
  min_blanks               count of [...] blanks; markdown links [text](url) are not blanks.
  no_new_numbers           every number in the reply must appear in the prompt (see numbers_in).
Scope: by default every check reads the whole reply. A check with "scope": "paste" (or, for
max_words/max_chars, the flag --length-scope paste) reads only the fenced code blocks in the reply,
the part an owner would paste; if the reply has no code block, the whole reply is used.
A case passes when every non-judge check passes. A case with only judge checks is "judge only"
and is not counted in pass rates.
"""
import argparse, collections, datetime, hashlib, json, math, re, sys, unicodedata
from decimal import Decimal, InvalidOperation

CHECKER_VERSION = "1.2"
LABEL = ("self-measured behavioral check pass rate on fictional test cases; "
         "programmatic checks only (judge checks not scored); not independent")

# ---------- digit fold (v1.2) ----------
_ZW = "\u200b\u200c\u200d\u2060\ufeff\u00ad"
_ZW_NEAR_DIGIT = re.compile(r"(?<=[0-9])[%s]+|[%s]+(?=[0-9])" % (_ZW, _ZW))


def fold(text):
    """One normalization for every content check: Unicode decimal digits (Devanagari, Kannada,
    Arabic-Indic, full-width ...) become ASCII 0-9, full-width ASCII forms (U+FF01-FF5E) become
    ASCII, U+3000 becomes a space, and zero-width characters touching a digit are dropped.
    Every other character is left alone, so lengths of non-digit text do not change."""
    if not text:
        return text or ""
    out = []
    for ch in str(text):
        o = ord(ch)
        if o < 128:
            out.append(ch)
        elif 0xFF01 <= o <= 0xFF5E:
            out.append(chr(o - 0xFEE0))
        elif o == 0x3000:
            out.append(" ")
        elif unicodedata.category(ch) == "Nd":
            out.append(str(unicodedata.decimal(ch)))
        else:
            out.append(ch)
    return _ZW_NEAR_DIGIT.sub("", "".join(out))


# ---------- numbers ----------
_LIST_NUM = re.compile(r"^(\s*(?:[-*]\s+)?(?:\*\*)?)(10|[1-9])([.)])(?=\s|\*\*)", re.M)
_NUM = re.compile(
    r"(?P<cur>₹|\bRs\.?|\bINR)?\s?"
    r"(?P<num>[0-9]{1,3}(?:,[0-9]{2,3})+(?:\.[0-9]+)?|[0-9]+(?:\.[0-9]+)?)"
    r"(?P<suf>\s?(?:k|K|lakhs?|lacs?|Lakhs?|Lacs?|crores?|Crores?|cr|Cr)\b\.?|L\b)?",
)
_SUFFIX_MULT = {"k": 1000, "lakh": 100000, "lakhs": 100000, "lac": 100000, "lacs": 100000, "l": 100000,
                "crore": 10000000, "crores": 10000000, "cr": 10000000}
# times: 10:30 -> 10.30 (read as 10.3), 8:00 -> 8.00 (read as 8), so "10.30am" and "10:30" match.
_TIME = re.compile(r"(?<![0-9:.,])([01]?[0-9]|2[0-4]):([0-5][0-9])(?![0-9:])")
_ALWAYS_OK = re.compile(r"(?i)\b24\s*[/x×]\s*7\b")


def _norm(s):
    try:
        d = Decimal(s)
    except InvalidOperation:
        return s
    d = d.normalize()
    return format(d, "f")


def numbers_in(text, ignore_list_numbering=False):
    """Return list of (shown, {normalized values}) for each number in text.

    - Commas inside numbers are dropped: 12,450 and 1,20,000 become 12450 and 120000.
    - A ₹ / Rs / Rs. / INR prefix is read as part of the number, so ₹1,500, Rs 1500 and 1500 match.
    - 15k is read as 15000 (and also 15); 1.5 lakh / 1.5L as 150000; 2 crore / 2 cr as 20000000.
    - Text is folded first (see fold): Indic and full-width digits count as ASCII digits.
    - Times 10:30 and 10.30 are the same number; "24/7" is skipped.
    - With ignore_list_numbering, "1." / "2)" list markers at line start (1-10) are skipped.
    """
    text = fold(text)
    text = _ALWAYS_OK.sub(" ", text)
    text = _TIME.sub(r"\1.\2", text)
    if ignore_list_numbering:
        text = _LIST_NUM.sub(lambda m: m.group(1) + "#" + m.group(3), text)
    out = []
    for m in _NUM.finditer(text):
        raw = m.group("num").replace(",", "")
        vals = {_norm(raw)}
        suf = (m.group("suf") or "").strip().rstrip(".").lower()
        if suf in _SUFFIX_MULT:
            vals.add(_norm(str(Decimal(raw) * _SUFFIX_MULT[suf])))
        out.append((m.group(0).strip(), vals))
    return out


# v1.2: only clearly structural labels and the helper's own counters are not facts.
# A label word followed by N counts as structure only at the start of a line (after any bullet,
# quote, heading "#" or bold "**"/"__") or inside a bold span. "Book by day 15", "room no. 12",
# "week 2" and "3-day offer" are checked like any other number.
_LABEL_WORDS = r"(?:e-?mail|follow[- ]?up|step|option|post|version)"
_LABEL_LINE = re.compile(r"(?im)^([ \t]*(?:[-*+>#]+[ \t]*)*(?:\*\*|__)?[ \t]*)(" + _LABEL_WORDS + r")[ \t]*#?[0-9]{1,2}\b")
# inside one bold span on one line, e.g. "**Message, version 2** (164 characters)"
_BOLD_SPAN = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
_LABEL_IN_SPAN = re.compile(r"(?i)\b(" + _LABEL_WORDS + r")[ \t]*#?[0-9]{1,2}\b")
# Counters: "(35 words, 168 characters)", "(12/25)", "64/500 characters", bare "64 words" or
# "120 characters" (optionally "/ 500"), "Characters: 42 / 50". Bounded: never runs past a bracket or
# to the end of a line.
_CNT_UNIT = r"(?:words?|characters?|chars?|lines?)"
_CNT_ITEM = r"(?:about\s+|under\s+|max\.?\s+)?[0-9]+(?:\s*/\s*[0-9][0-9,]*)?\s*" + _CNT_UNIT
_LIMITS = r"(?:25|50|60|100|150|160|200|300|500|750|1,?200|1,?500|2,?200)"
_COUNTER = re.compile(
    r"(?im)\(\s*" + _CNT_ITEM + r"(?:\s*(?:,|;|·|and|/)\s*" + _CNT_ITEM + r")*\s*\)"
    r"|\(\s*[0-9]+\s*/\s*" + _LIMITS + r"\s*\)"
    r"|\b[0-9]+\s*/\s*" + _LIMITS + r"\s*(?:characters?|chars?)\b"
    r"|\b[0-9]+\s*/\s*" + _LIMITS + r"[ \t]*$"
    r"|\b(?:characters?|chars?|words?)[ \t]*:?[ \t]*[0-9]+[ \t]*/[ \t]*" + _LIMITS + r"\b"
    r"|\b[0-9]+\s*(?:words?|characters?|chars?)\b(?:\s*/\s*" + _LIMITS + r"\b)?")


def strip_structure(text):
    text = fold(text)
    text = _COUNTER.sub(" ", text)
    text = _LABEL_LINE.sub(lambda m: m.group(1) + m.group(2), text)
    return _BOLD_SPAN.sub(lambda m: _LABEL_IN_SPAN.sub(lambda n: n.group(1), m.group(0)), text)


def no_new_numbers(reply, prompt):
    reply = strip_structure(reply)
    allowed = set()
    for _, vals in numbers_in(fold(prompt)):
        allowed |= vals
    new = [shown for shown, vals in numbers_in(reply, ignore_list_numbering=True) if not (vals & allowed)]
    return new


_BLANK = re.compile(r"\[[^\[\]\n]+\](?!\()")


def count_blanks(text):
    return len(_BLANK.findall(text))


# ---------- checks ----------
def snippet(text, start=None, end=None, width=70):
    if start is None:
        s = text[:2 * width]
        return s.replace("\n", " ⏎ ") + ("…" if len(text) > 2 * width else "")
    a, b = max(0, start - width), min(len(text), end + width)
    s = ("…" if a else "") + text[a:b] + ("…" if b < len(text) else "")
    return s.replace("\n", " ⏎ ")


_FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
LENGTH_SCOPE = "reply"


def paste_part(reply):
    blocks = _FENCE.findall(reply)
    return "\n".join(b.strip() for b in blocks) if blocks else reply


def run_check(chk, reply, prompt):
    """Return (status, detail, snippet). status in pass|fail|judge|error."""
    t = chk.get("type")
    scope = chk.get("scope") or (LENGTH_SCOPE if t in ("max_words", "max_chars") else "reply")
    if scope == "paste":
        reply = paste_part(reply)
    v = chk.get("value")
    if t not in ("max_words", "max_chars"):  # v1.2: one digit fold for every content check
        reply = fold(reply)
        if t in ("contains", "not_contains") and isinstance(v, str):
            v = fold(v)
    try:
        if t == "judge":
            return "judge", str(v), ""
        if t == "contains":
            i = reply.lower().find(str(v).lower())
            return ("pass", "", "") if i >= 0 else ("fail", "missing %r" % v, snippet(reply))
        if t == "not_contains":
            i = reply.lower().find(str(v).lower())
            return ("pass", "", "") if i < 0 else ("fail", "found %r" % v, snippet(reply, i, i + len(str(v))))
        if t in ("regex", "not_regex"):
            m = re.search(v, reply, re.M)
            if t == "regex":
                return ("pass", "", "") if m else ("fail", "no match for /%s/" % v, snippet(reply))
            return ("pass", "", "") if not m else ("fail", "matched %r" % m.group(0), snippet(reply, m.start(), m.end()))
        if t == "max_words":
            n = len(reply.split())
            return ("pass", "", "") if n <= int(v) else ("fail", "%d words > %d" % (n, int(v)), snippet(reply))
        if t == "max_chars":
            n = len(reply)
            return ("pass", "", "") if n <= int(v) else ("fail", "%d chars > %d" % (n, int(v)), snippet(reply))
        if t == "min_blanks":
            n = count_blanks(reply)
            return ("pass", "", "") if n >= int(v) else ("fail", "%d blanks < %d" % (n, int(v)), snippet(reply))
        if t == "no_new_numbers":
            new = no_new_numbers(reply, prompt)
            if not new:
                return "pass", "", ""
            first = new[0]
            i = reply.find(first)
            return "fail", "new numbers: " + ", ".join(new[:8]), snippet(reply, i, i + len(first)) if i >= 0 else snippet(reply)
        return "error", "unknown check type %r" % t, ""
    except (re.error, ValueError, TypeError) as e:
        return "error", "%s: %s" % (type(e).__name__, e), ""


def grade_case(case, reply):
    """Return dict with status in pass|fail|judge_only, plus per-check results."""
    results = []
    for chk in case.get("checks", []):
        st, detail, snip = run_check(chk, reply, case.get("prompt", ""))
        results.append({"check": chk, "status": st, "detail": detail, "snippet": snip})
    scored = [r for r in results if r["status"] != "judge"]
    if not scored:
        status = "judge_only"
    elif all(r["status"] == "pass" for r in scored):
        status = "pass"
    else:
        status = "fail"  # an "error" check counts as a fail and is listed
    return {"status": status, "checks": results}


# ---------- stats ----------
def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def fmt_rate(k, n):
    if n == 0:
        return "n/a (0 graded)"
    lo, hi = wilson(k, n)
    return "%d/%d = %.1f%% (95%% CI %.1f–%.1f)" % (k, n, 100 * k / n, 100 * lo, 100 * hi)


def table(rows, key, title):
    groups = collections.OrderedDict()
    for r in sorted(rows, key=lambda r: str(r[key])):
        groups.setdefault(r[key] or "(none)", []).append(r["ok"])
    out = ["| %s | passed | n | rate | 95%% CI |" % title, "|---|---|---|---|---|"]
    for g, oks in groups.items():
        k, n = sum(oks), len(oks)
        lo, hi = wilson(k, n)
        out.append("| %s | %d | %d | %.0f%% | %.0f–%.0f%% |" % (g, k, n, 100 * k / n, 100 * lo, 100 * hi))
    return "\n".join(out)


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ---------- loading ----------
def load_cases(paths):
    cases, seen = [], {}
    for p in paths:
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        lst = d if isinstance(d, list) else d.get("cases", [])
        suite = d.get("suite", p) if isinstance(d, dict) else p
        for c in lst:
            if c["id"] in seen:
                raise SystemExit("duplicate case id %s in %s and %s" % (c["id"], seen[c["id"]], p))
            seen[c["id"]] = p
            c = dict(c)
            c["_suite"] = suite
            cases.append(c)
    return cases


def load_responses(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    r = d.get("responses", d) if isinstance(d, dict) else {}
    return {k: v for k, v in r.items() if isinstance(v, str)}, (d.get("meta") if isinstance(d, dict) else None)


# ---------- report ----------
def provenance(meta):
    """One line on where the replies came from. No model recorded = reference answers."""
    if not isinstance(meta, dict) or not (meta.get("model_requested") or meta.get("model")):
        return ("no model recorded in the responses file: treat these as reference answers written "
                "by people or scripts, not a model run")
    return "model run: %s, %s, mode %s, replicate %s" % (
        meta.get("model_requested") or meta.get("model"), meta.get("claude_version", "version not recorded"),
        meta.get("mode", "?"), meta.get("replicate", "?"))


def build_report(case_paths, resp_paths, cases, runs, metas=None):
    """runs: list of dicts {case_id: graded} per replicate (only cases with a reply)."""
    metas = metas or [None] * len(runs)
    L = []
    L.append("# Behavioral check report")
    L.append("")
    L.append("**Label:** %s." % LABEL)
    L.append("")
    L.append("Generated %s by `check.py` (checker v%s)." % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                                          CHECKER_VERSION))
    L.append("")
    for i, m in enumerate(metas, 1):
        L.append("- Replicate %d provenance: %s." % (i, provenance(m)))
    L.append("")
    L.append("| file | role | SHA-256 |")
    L.append("|---|---|---|")
    for p in case_paths:
        L.append("| `%s` | testbank | `%s` |" % (p, sha256(p)))
    for i, p in enumerate(resp_paths, 1):
        L.append("| `%s` | responses (replicate %d) | `%s` |" % (p, i, sha256(p)))
    L.append("")

    by_id = {c["id"]: c for c in cases}
    common = [cid for cid in by_id if all(cid in run for run in runs)]
    scored = [cid for cid in common if all(run[cid]["status"] != "judge_only" for run in runs)]

    def rows_for(pick):
        return [{"id": cid, "skill": by_id[cid].get("skill"), "kind": by_id[cid].get("kind"),
                 "archetype": by_id[cid].get("archetype"), "ok": pick(cid)} for cid in scored]

    L.append("## Overall")
    L.append("")
    L.append("- Cases in testbanks: %d. With a reply in every replicate: %d. Scored (has a programmatic check): %d."
             % (len(cases), len(common), len(scored)))
    for i, run in enumerate(runs, 1):
        k = sum(1 for cid in scored if run[cid]["status"] == "pass")
        L.append("- Case pass rate, replicate %d: %s" % (i, fmt_rate(k, len(scored))))
    if len(runs) > 1:
        k = sum(1 for cid in scored if all(run[cid]["status"] == "pass" for run in runs))
        flips = [cid for cid in scored if len({run[cid]["status"] for run in runs}) > 1]
        L.append("- Passed in every replicate (strict): %s" % fmt_rate(k, len(scored)))
        L.append("- Instability (pass in one replicate, fail in another): %d of %d cases%s"
                 % (len(flips), len(scored), (": " + ", ".join(flips)) if flips else ""))
    ck = cn = 0
    for run in runs:
        for cid in scored:
            for r in run[cid]["checks"]:
                if r["status"] != "judge":
                    cn += 1
                    ck += r["status"] == "pass"
    L.append("- Check pass rate (all programmatic checks, all replicates): %s" % fmt_rate(ck, cn))
    L.append("")
    if len(runs) > 1:
        pick = lambda cid: all(run[cid]["status"] == "pass" for run in runs)
        L.append("Breakdowns below use the strict rule (passed in every replicate).")
    else:
        pick = lambda cid: runs[0][cid]["status"] == "pass"
    L.append("")
    rows = rows_for(pick)
    for key, title in (("skill", "Skill"), ("kind", "Kind"), ("archetype", "Archetype")):
        L.append("## By %s" % key)
        L.append("")
        L.append(table(rows, key, title) if rows else "_no scored cases_")
        L.append("")
    L.append("Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.")
    L.append("")

    L.append("## Failed checks")
    L.append("")
    any_fail = False
    for i, run in enumerate(runs, 1):
        for cid in common:
            g = run[cid]
            bad = [r for r in g["checks"] if r["status"] in ("fail", "error")]
            if not bad:
                continue
            any_fail = True
            c = by_id[cid]
            tag = (" (replicate %d)" % i) if len(runs) > 1 else ""
            L.append("### %s%s: %s / %s / %s" % (cid, tag, c.get("skill"), c.get("kind"), c.get("archetype")))
            for r in bad:
                chk = r["check"]
                val = "" if chk.get("value") is None else " `%s`" % str(chk.get("value")).replace("`", "'")
                L.append("- **%s**%s: %s%s" % (chk.get("type"), val, r["detail"],
                                                " (check error)" if r["status"] == "error" else ""))
                if r["snippet"]:
                    L.append("  > %s" % r["snippet"].replace("|", "\\|"))
            L.append("")
    if not any_fail:
        L.append("None.")
        L.append("")

    judges = [(cid, r["check"].get("value")) for cid in common for r in runs[0][cid]["checks"] if r["status"] == "judge"]
    L.append("## Judge checks (skipped, need a person or a blinded judge)")
    L.append("")
    L.append("Judge checks (%d, in %d cases) not yet scored. Case pass rates above leave them out."
             % (len(judges), len({cid for cid, _ in judges})))
    L.append("")
    if judges:
        for cid, v in judges:
            L.append("- %s: %s" % (cid, v))
    else:
        L.append("None.")
    L.append("")
    jo = [cid for cid in common if any(run[cid]["status"] == "judge_only" for run in runs)]
    if jo:
        L.append("Judge-only cases (not in pass rates): " + ", ".join(jo))
        L.append("")

    missing = [cid for cid in by_id if cid not in common]
    L.append("## Missing replies")
    L.append("")
    L.append(", ".join(missing) if missing else "None.")
    L.append("")
    L.append("## Method notes")
    L.append("")
    L.append("- A case passes only when every programmatic check passes. Judge checks are listed, not scored.")
    L.append("- Length checks measured: %s." % ("code blocks only (--length-scope paste)" if LENGTH_SCOPE == "paste"
                                                 else "the whole reply, including any notes around the draft"))
    L.append("- Checker v%s. Cases were pre-registered; the checker was revised after first results "
             "(v1.0, v1.1, v1.2). Compare numbers only under the same checker version." % CHECKER_VERSION)
    L.append("- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; "
             "₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and "
             "2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped "
             "only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and "
             "character counters are skipped. Number words (\"three nights\") are not checked.")
    L.append("- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and "
             "contains values); length checks measure the reply as given.")
    L.append("- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an "
             "independent test.")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-r", "--responses", action="append", required=True, help="responses JSON (repeat for replicates)")
    ap.add_argument("testbanks", nargs="+", help="testbank JSON files")
    ap.add_argument("--out", help="write the markdown report here (default: print)")
    ap.add_argument("--length-scope", choices=["reply", "paste"], default="reply",
                    help="what max_words/max_chars measure: the whole reply (default) or its code blocks")
    a = ap.parse_args(argv)
    global LENGTH_SCOPE
    LENGTH_SCOPE = a.length_scope

    cases = load_cases(a.testbanks)
    by_id = {c["id"]: c for c in cases}
    runs, metas, stray = [], [], set()
    for p in a.responses:
        resp, meta = load_responses(p)
        stray |= set(resp) - set(by_id)
        runs.append({cid: grade_case(by_id[cid], resp[cid]) for cid in by_id if cid in resp})
        metas.append(meta)
    rep = build_report(a.testbanks, a.responses, cases, runs, metas)
    if stray:
        rep += "\nReplies with no matching case (ignored): %s\n" % ", ".join(sorted(stray))
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(rep)
        print("wrote", a.out)
    else:
        sys.stdout.write(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
