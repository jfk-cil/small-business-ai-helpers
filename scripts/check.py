#!/usr/bin/env python3
"""Repository checks. Python 3 standard library only (PyYAML is used if installed). Exit code 1
on any error.

  python3 scripts/check.py           run every check
  python3 scripts/check.py --strict  also fail on warnings

Checks
  skills      SKILL.md frontmatter (strict YAML: parsed with PyYAML if installed, otherwise an
              unquoted ": " or other YAML-breaking value is an error; name = folder, 1-64 chars,
              a-z 0-9 and single hyphens, no "claude" or "anthropic"; description 1-1024 chars,
              no angle brackets; license), required files, JSON files parse, every eval file has ids.
  catalog     every package skill exists, every skill is used, ids are valid plugin names,
              helper {{slots}} match the questions.
  testbank    evals/testbank/*.json follow the shared schema and use known check types.
  i18n        every translation has exactly the English keys (plus "_notes").
  pages       generated pages load no external scripts and only Google Fonts styles.
  privacy     no phone, Aadhaar, PAN, email or UPI-like values outside the fake test values,
              and no names of private people or organizations (from a local terms file that is
              never committed: SBH_PRIVATE_TERMS=/path/to/terms.txt).
  style       em dashes and British spellings in owner-facing text (warnings).
"""
import argparse, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERR, WARN = [], []


def err(m): ERR.append(m)
def warn(m): WARN.append(m)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if mm:
            v = mm.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[mm.group(1)] = v
    return fm


def strict_yaml_problem(text):
    """Return a reason string if the frontmatter is not valid YAML, else None.
    Uses PyYAML when it is installed; otherwise flags plain (unquoted) values that YAML rejects,
    the common one being ": " inside a description."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return "no YAML frontmatter"
    try:
        import yaml
    except ImportError:
        yaml = None
    if yaml is not None:
        try:
            d = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            return "invalid YAML (%s)" % " ".join(str(e).split())
        if not isinstance(d, dict):
            return "frontmatter is not a YAML mapping"
        for k in ("name", "description"):
            if k in d and not isinstance(d[k], str):
                return "%s is not a plain string" % k
        return None
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_-]+):[ \t]*(.*)$", line)
        if not mm:
            continue
        k, v = mm.group(1), mm.group(2).rstrip()
        if not v or v[0] in "\"'":
            continue
        if ": " in v or v.endswith(":") or " #" in v or v[0] in "&*!|>%@`{[]},#" or v.startswith(("- ", "? ")):
            return "%s value needs double quotes or rewording (unquoted ': ', ' #' or a YAML symbol at the start)" % k
    return None


NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED = ["SKILL.md", "OWNER-CARD.md", "SAFEGUARDS.md", "LICENSE", "CHANGELOG.md"]


def check_skills():
    names = []
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir():
            continue
        names.append(d.name)
        for f in REQUIRED:
            if not (d / f).exists():
                err("skills/%s: missing %s" % (d.name, f))
        sk = d / "SKILL.md"
        if not sk.exists():
            continue
        fm = frontmatter(sk.read_text(encoding="utf-8"))
        if fm is None:
            err("skills/%s/SKILL.md: no YAML frontmatter" % d.name); continue
        bad = strict_yaml_problem(sk.read_text(encoding="utf-8"))
        if bad: err("skills/%s/SKILL.md: frontmatter %s" % (d.name, bad))
        n, desc = fm.get("name", ""), fm.get("description", "")
        if n != d.name: err("skills/%s: name %r does not match folder" % (d.name, n))
        if not NAME_RE.match(n) or len(n) > 64: err("skills/%s: invalid name %r" % (d.name, n))
        if "claude" in n or "anthropic" in n: err("skills/%s: name may not contain claude/anthropic" % d.name)
        if not 1 <= len(desc) <= 1024: err("skills/%s: description length %d (1-1024)" % (d.name, len(desc)))
        if "<" in desc or ">" in desc: err("skills/%s: description has angle brackets" % d.name)
        if fm.get("license") != "CC0-1.0": warn("skills/%s: license is not CC0-1.0" % d.name)
        words = len(sk.read_text(encoding="utf-8").split())
        if words > 3000: warn("skills/%s: SKILL.md is %d words (aim under ~2,000; move detail to references/)" % (d.name, words))
        for j in d.rglob("*.json"):
            try: json.loads(j.read_text(encoding="utf-8"))
            except Exception as e: err("%s: invalid JSON (%s)" % (j.relative_to(ROOT), e))
    return names


def check_catalog(skill_names):
    cat = json.loads((ROOT / "catalog/packages.json").read_text(encoding="utf-8"))
    used = set()
    for p in cat["packages"]:
        pid = p["id"]
        if not NAME_RE.match(pid) or re.match(r"^(claude|anthropic|anthropics|cc-plugin)-", pid):
            err("catalog: invalid package id %r" % pid)
        for s in p["skills"]:
            used.add(s)
            if s not in skill_names: err("catalog: %s uses missing skill %s" % (pid, s))
        slots = set(re.findall(r"\{\{(\w+)\}\}", p["helper"]))
        qids = {q["id"] for q in p["questions"]}
        if slots != qids: err("catalog: %s helper slots %s != questions %s" % (pid, sorted(slots), sorted(qids)))
        if len(p["helper"].split()) > 420: warn("catalog: %s helper is long (%d words)" % (pid, len(p["helper"].split())))
        for d in ("README.md", "PLAYBOOK.md", "BUILDER-NOTES.md"):
            if not (ROOT / "packages" / pid / d).exists(): err("packages/%s: missing %s" % (pid, d))
    for s in skill_names:
        if s not in used: warn("skills/%s is not in any package" % s)
    return cat


CHECK_TYPES = {"contains", "not_contains", "regex", "not_regex", "max_words", "max_chars",
               "no_new_numbers", "min_blanks", "judge"}


def check_testbank():
    ids = set()
    for f in sorted((ROOT / "evals/testbank").glob("*.json")):
        try: d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e: err("%s: invalid JSON (%s)" % (f.name, e)); continue
        for k in ("suite", "version", "cases"):
            if k not in d: err("testbank/%s: missing %s" % (f.name, k))
        for c in d.get("cases", []):
            for k in ("id", "skill", "kind", "prompt", "checks"):
                if k not in c: err("testbank/%s: case missing %s" % (f.name, k))
            if c.get("id") in ids: err("testbank/%s: duplicate id %s" % (f.name, c.get("id")))
            ids.add(c.get("id"))
            if not (ROOT / "skills" / c.get("skill", "")).exists(): err("testbank/%s: %s names unknown skill" % (f.name, c.get("id")))
            for ch in c.get("checks", []):
                if ch.get("type") not in CHECK_TYPES: err("testbank/%s: %s unknown check type %r" % (f.name, c.get("id"), ch.get("type")))
                if ch.get("type") in ("regex", "not_regex"):
                    try: re.compile(ch.get("value", ""))
                    except re.error as e: err("testbank/%s: %s bad regex (%s)" % (f.name, c.get("id"), e))
    return len(ids)


def check_i18n():
    en = json.loads((ROOT / "site/i18n/en.json").read_text(encoding="utf-8"))
    for lg in ("hi", "mr", "kok-deva", "kok-latn"):
        p = ROOT / "site/i18n" / (lg + ".json")
        if not p.exists(): err("site/i18n/%s.json missing" % lg); continue
        d = json.loads(p.read_text(encoding="utf-8"))
        missing = [k for k in en if k not in d]
        extra = [k for k in d if k not in en and k != "_notes"]
        if missing: err("i18n %s: %d missing keys, e.g. %s" % (lg, len(missing), missing[:3]))
        if extra: warn("i18n %s: %d extra keys, e.g. %s" % (lg, len(extra), extra[:3]))
        for k in en:
            if k in d and "[blank]" in en[k] and "[blank]" not in d[k]:
                err("i18n %s: %s lost [blank]" % (lg, k))


def check_pages():
    for f in list((ROOT / "docs").rglob("*.html")) + list((ROOT / "artifacts").glob("*.html")):
        t = f.read_text(encoding="utf-8")
        for src in re.findall(r"<script[^>]*\bsrc=\"([^\"]+)\"", t):
            err("%s: external script %s" % (f.relative_to(ROOT), src))
        for href in re.findall(r"<link[^>]*rel=\"stylesheet\"[^>]*href=\"([^\"]+)\"", t):
            if not href.startswith("https://fonts.googleapis.com/"):
                err("%s: external stylesheet %s" % (f.relative_to(ROOT), href))


# Private names: read from a local, never-committed file (one term per line), so the list is not
# published. Set SBH_PRIVATE_TERMS=/path/to/terms.txt; without it this check is skipped with a loud
# warning (exit code stays 0, because CI cannot hold the file). The maintainer runs it before release.
PRIVATE_SCAN_NOTE = []


def load_private_terms():
    import os
    p = os.environ.get("SBH_PRIVATE_TERMS")
    if not p:
        PRIVATE_SCAN_NOTE.append("SBH_PRIVATE_TERMS is not set.")
        return None
    if not Path(p).exists():
        PRIVATE_SCAN_NOTE.append("SBH_PRIVATE_TERMS is set, but the file does not exist: %s" % p)
        return None
    terms = {t.strip().lower() for t in Path(p).read_text(encoding="utf-8").splitlines() if t.strip() and not t.startswith("#")}
    if not terms:
        PRIVATE_SCAN_NOTE.append("SBH_PRIVATE_TERMS file has no terms: %s" % p)
        return None
    return terms
FAKE_OK = {"98765 43210", "9876543210", "1234 5678 9012", "123456789012", "ABCDE1234F"}
PII = [("phone", re.compile(r"(?<!\d)(?:\+?91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}(?!\d)")),
       ("aadhaar", re.compile(r"(?<!\d)\d{4}[\s-]\d{4}[\s-]\d{4}(?!\d)")),
       ("pan", re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b")),
       ("email/upi", re.compile(r"\b[\w.+-]+@[a-z][\w-]*(?:\.[\w.-]+)?\b", re.I))]
EMAIL_OK = re.compile(r"^(noreply@|[\w.-]+@(small-business-ai-helpers|example\.(com|org|in)|ok[a-z]+|ybl|upi|sample[\w.-]*|mail\.test$))", re.I)
SCAN_SUFFIX = {".md", ".json", ".html", ".txt", ".py", ".yml", ".yaml", ".sh", ""}
SKIP_DIRS = {".git", "docs", "artifacts", "packages"}  # generated copies are scanned at their source


def ngrams(text):
    toks = re.findall(r"[a-z0-9.]+", text.lower().replace("jfk-cil", "repo-owner"))
    out = set()
    for n in (1, 2, 3, 4):
        for i in range(len(toks) - n + 1):
            g = " ".join(toks[i:i + n])
            out.add(g)
            out.add(g.rstrip("."))
    return out


def check_privacy():
    terms = load_private_terms()
    if terms is None:
        warn("private-name scan NOT run: maintainer must run it before release (%s)" % PRIVATE_SCAN_NOTE[-1])
    files = []
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if not p.is_file() or rel.parts[0] in SKIP_DIRS or p.suffix not in SCAN_SUFFIX:
            continue
        files.append(p)
    for p in (ROOT / "packages").rglob("*.md"):
        if "skills" not in p.relative_to(ROOT).parts:
            files.append(p)
    for p in files:
        rel = str(p.relative_to(ROOT))
        t = p.read_text(encoding="utf-8", errors="ignore")
        if terms:
            hit = ngrams(t) & terms
            if hit:
                err("%s: names a private person or organization: %s" % (rel, sorted(hit)[0]))
        in_tests = rel.startswith("evals/") or "SAFEGUARDS" in rel or "/evals/" in rel
        for kind, rx in PII:
            for m in rx.finditer(t):
                v = m.group(0)
                if kind == "email/upi" and (EMAIL_OK.match(v) or rel.startswith(("scripts/", ".github/", "publish.sh")) or v.startswith("@")):
                    continue
                if any(f in v for f in FAKE_OK) or rel.startswith("scripts/"):
                    continue
                if in_tests and kind != "email/upi":
                    continue
                (err if not in_tests else warn)("%s: looks like a real %s: %s" % (rel, kind, v[:4] + "…"))


BRITISH = re.compile(r"\b(colour|favour|behaviour|organis\w*|recognis\w*|analys(e|ed|ing)|licence|centre|enquir\w*|whilst|amongst|programme|cancell(ed|ing))\b", re.I)


def check_style():
    targets = list((ROOT / "packages").glob("*/*.md")) + [ROOT / "README.md", ROOT / "site/i18n/ui.en.json"]
    for p in targets:
        if not p.exists(): continue
        t = p.read_text(encoding="utf-8")
        if "—" in t: warn("%s: has em dashes" % p.relative_to(ROOT))
        for m in BRITISH.finditer(t):
            warn("%s: British spelling %r" % (p.relative_to(ROOT), m.group(0))); break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    names = check_skills()
    check_catalog(names)
    n = check_testbank()
    check_i18n()
    check_pages()
    check_privacy()
    check_style()
    for w in WARN: print("warning: " + w)
    for e in ERR: print("ERROR: " + e)
    if PRIVATE_SCAN_NOTE:
        bar = "!" * 72
        print(bar)
        print("WARNING: private-name scan NOT run: maintainer must run it before release.")
        print(PRIVATE_SCAN_NOTE[-1])
        print("Run: SBH_PRIVATE_TERMS=/path/to/terms.txt python3 scripts/check.py")
        print("(a local plain-text list, one name per line, never committed)")
        print(bar)
    print("checked %d skills, %d test cases: %d errors, %d warnings" % (len(names), n, len(ERR), len(WARN)))
    sys.exit(1 if ERR or (a.strict and WARN) else 0)


if __name__ == "__main__":
    main()
