#!/usr/bin/env python3
"""Grade routing picks against a routing suite (e.g. wave/routing/cases.json). Stdlib only.

Usage:
  python3 route_check.py ../routing/cases.json ../routing/judge-1.json [../routing/judge-2.json ...]
         [--expect-sha <sha256 of cases.json>] [--out report.md]

Picks file: {"judge": "1", "picks": {"r001": "first-task-finder", ...}} or a flat {"r001": "...", ...}.
A pick counts only when it equals the case's "expected" label exactly (after trimming and lowercasing;
"none" in any case means NONE). Missing picks count as wrong and are listed.

v1.2 (October 14, 2026, red-team T22): a pick missing from both judges no longer counts as agreement
(in the agreement count or in Cohen's kappa), and --expect-sha exits with code 2 when the cases file
does not match the pre-registered hash. Exit codes: 0 ok, 2 hash mismatch.
"""
import argparse, collections, datetime, hashlib, json, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import wilson, fmt_rate, sha256  # noqa: E402

LABEL = ("self-measured, description-level; same model family wrote and judged the tests; "
         "closed skill set + NONE; not trigger accuracy in Claude")


def norm(x):
    if x is None:
        return None
    x = str(x).strip().strip("`").strip()
    return "NONE" if x.lower() == "none" else x.lower()


def load_picks(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    name = str(d.get("judge", os.path.basename(path))) if isinstance(d, dict) else os.path.basename(path)
    picks = d.get("picks", d) if isinstance(d, dict) else {}
    return name, {k: norm(v) for k, v in picks.items() if k not in ("judge", "meta")}


def kappa(a, b):
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[k] * cb.get(k, 0) for k in ca) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def build_report(cases_path, pick_paths, cases, judges, expect_sha=None):
    L = ["# Routing check report", "", "**Label:** %s." % LABEL, "",
         "Generated %s by `route_check.py`." % datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ""]
    h = sha256(cases_path)
    L.append("| file | role | SHA-256 |")
    L.append("|---|---|---|")
    L.append("| `%s` | cases | `%s` |" % (cases_path, h))
    for p in pick_paths:
        L.append("| `%s` | picks | `%s` |" % (p, sha256(p)))
    L.append("")
    if expect_sha:
        L.append("Pre-registered hash %s: **%s**." % (expect_sha, "matches" if expect_sha.strip().lower() == h
                                                       else "DOES NOT MATCH (new suite; exit code 2)"))
        L.append("")

    exp = {c["id"]: norm(c["expected"]) for c in cases}
    kind = {c["id"]: c.get("kind", "") for c in cases}
    ids = [c["id"] for c in cases]
    L.append("## Overall (n = %d)" % len(ids))
    L.append("")
    for name, picks in judges:
        k = sum(picks.get(i) == exp[i] for i in ids)
        L.append("- Judge %s: %s" % (name, fmt_rate(k, len(ids))))
        missing = [i for i in ids if i not in picks]
        if missing:
            L.append("  - missing picks (counted wrong): %s" % ", ".join(missing))
    if len(judges) > 1:
        both = sum(all(p.get(i) == exp[i] for _, p in judges) for i in ids)
        L.append("- Correct for every judge: %s" % fmt_rate(both, len(ids)))
        for x in range(len(judges)):
            for y in range(x + 1, len(judges)):
                # a missing pick is its own value per judge, so two blanks never "agree"
                a = [judges[x][1].get(i) or "(missing-%s)" % judges[x][0] for i in ids]
                b = [judges[y][1].get(i) or "(missing-%s)" % judges[y][0] for i in ids]
                agree = sum(p == q for p, q in zip(a, b))
                L.append("- Agreement, judge %s vs %s: %d/%d, Cohen's kappa %.2f"
                         % (judges[x][0], judges[y][0], agree, len(ids), kappa(a, b)))
    L.append("")

    def group_table(keyf, title):
        out = ["| %s | n | %s |" % (title, " | ".join("judge %s" % n for n, _ in judges)),
               "|---|---|%s" % ("---|" * len(judges))]
        groups = collections.OrderedDict()
        for i in ids:
            groups.setdefault(keyf(i), []).append(i)
        for g in sorted(groups):
            members = groups[g]
            cells = []
            for _, p in judges:
                k = sum(p.get(i) == exp[i] for i in members)
                lo, hi = wilson(k, len(members))
                cells.append("%d/%d (%.0f–%.0f%%)" % (k, len(members), 100 * lo, 100 * hi))
            out.append("| %s | %d | %s |" % (g, len(members), " | ".join(cells)))
        return "\n".join(out)

    L.append("## By kind")
    L.append("")
    L.append(group_table(lambda i: kind[i], "kind"))
    L.append("")
    L.append("## By expected skill (recall)")
    L.append("")
    L.append(group_table(lambda i: exp[i], "expected"))
    L.append("")
    L.append("Per-skill n is small. These rows find boundary failures; they do not rank skills.")
    L.append("")

    L.append("## Confusions (expected → picked, wrong picks only, all judges)")
    L.append("")
    conf = collections.Counter()
    for _, p in judges:
        for i in ids:
            if p.get(i) != exp[i]:
                conf[(exp[i], p.get(i) or "(missing)")] += 1
    if conf:
        L.append("| expected | picked | count |")
        L.append("|---|---|---|")
        for (e, g), n in conf.most_common():
            L.append("| %s | %s | %d |" % (e, g, n))
    else:
        L.append("None.")
    L.append("")

    L.append("## Misses")
    L.append("")
    prompt = {c["id"]: c.get("prompt", "") for c in cases}
    rows = [i for i in ids if any(p.get(i) != exp[i] for _, p in judges)]
    if rows:
        L.append("| id | kind | expected | %s | prompt |" % " | ".join("judge %s" % n for n, _ in judges))
        L.append("|---|---|---|%s---|" % ("---|" * len(judges)))
        for i in rows:
            pr = prompt[i].replace("|", "\\|").replace("\n", " ")
            pr = pr[:90] + ("…" if len(pr) > 90 else "")
            L.append("| %s | %s | %s | %s | %s |" % (i, kind[i], exp[i],
                                                     " | ".join(p.get(i) or "(missing)" for _, p in judges), pr))
    else:
        L.append("None.")
    L.append("")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cases")
    ap.add_argument("picks", nargs="+")
    ap.add_argument("--expect-sha")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    with open(a.cases, encoding="utf-8") as f:
        d = json.load(f)
    cases = d["cases"] if isinstance(d, dict) else d
    judges = [load_picks(p) for p in a.picks]
    rep = build_report(a.cases, a.picks, cases, judges, a.expect_sha)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(rep)
        print("wrote", a.out)
    else:
        sys.stdout.write(rep)
    if a.expect_sha and a.expect_sha.strip().lower() != sha256(a.cases):
        print("ERROR: %s does not match the pre-registered hash %s" % (a.cases, a.expect_sha), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
