#!/usr/bin/env python3
"""Produce a responses file for check.py by running each test case through Claude Code headless.
Stdlib only. See run_with_claude_code.md before using it.

Each case runs in its own fresh `claude -p` process, in an empty temp folder, with only that
case's skill available. Nothing is saved as a session (--no-session-persistence).

  python3 make_responses.py --model <full model id> --skills-dir ../skills \
      --out runs/rep1.json ../testbank/*.json [--mode append|slash] [--dry-run]

Modes:
  append (default)  claude -p --safe-mode --append-system-prompt-file <skill>/SKILL.md ...
                    Works with your normal Claude login. Your own skills, plugins, CLAUDE.md and MCP
                    servers do not load (--safe-mode), so only this skill's text is added.
  slash             claude --bare -p --add-dir <tmp> "/<skill> <prompt>" with the skill copied into
                    <tmp>/.claude/skills/<skill>/. Closer to "installed". Needs ANTHROPIC_API_KEY
                    (bare mode does not use a subscription login).
"""
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys, tempfile


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_cases(paths):
    out = []
    for p in paths:
        d = json.load(open(p, encoding="utf-8"))
        out += d if isinstance(d, list) else d.get("cases", [])
    return out


def build_cmd(a, case, skill_md, tmp):
    base = [a.claude, "-p", "--no-session-persistence", "--model", a.model,
            "--output-format", "json", "--tools", "", "--max-turns", "3"]
    if a.mode == "append":
        return base + ["--safe-mode", "--append-system-prompt-file", skill_md, case["prompt"]]
    dst = os.path.join(tmp, ".claude", "skills", case["skill"])
    if not a.dry_run:
        shutil.copytree(os.path.dirname(skill_md), dst)
    return [a.claude, "--bare"] + base[1:] + ["--add-dir", tmp, "/%s %s" % (case["skill"], case["prompt"])]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("testbanks", nargs="+")
    ap.add_argument("--model", required=True, help="full model ID, not an alias")
    ap.add_argument("--skills-dir", required=True, help="folder holding <skill>/SKILL.md")
    ap.add_argument("--out", required=True)
    ap.add_argument("--mode", choices=["append", "slash"], default="append")
    ap.add_argument("--replicate", default="1")
    ap.add_argument("--only", help="comma-separated case ids to run")
    ap.add_argument("--claude", default="claude")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--dry-run", action="store_true", help="print commands, run nothing")
    a = ap.parse_args(argv)

    if a.model in ("sonnet", "opus", "haiku", "fable", "default"):
        sys.exit("Use a full model ID, not the alias %r: aliases move to new models." % a.model)
    cases = load_cases(a.testbanks)
    if a.only:
        keep = set(a.only.split(","))
        cases = [c for c in cases if c["id"] in keep]

    version = "dry-run"
    if not a.dry_run:
        version = subprocess.run([a.claude, "-v"], capture_output=True, text=True).stdout.strip()
    meta = {"date": datetime.datetime.now().isoformat(timespec="seconds"), "claude_version": version,
            "model_requested": a.model, "models_seen": [], "mode": a.mode, "replicate": a.replicate,
            "testbanks": {p: sha(p) for p in a.testbanks}, "skills": {}, "errors": {},
            "label": "self-measured, Claude Code headless (%s mode), fictional cases; not independent" % a.mode}
    responses = {}
    if os.path.exists(a.out) and not a.dry_run:  # resume a stopped run
        old = json.load(open(a.out, encoding="utf-8"))
        if old.get("meta", {}).get("model_requested") == a.model:
            responses = old.get("responses", {})

    for c in cases:
        if c["id"] in responses:
            continue
        skill_md = os.path.join(a.skills_dir, c["skill"], "SKILL.md")
        if not os.path.exists(skill_md):
            meta["errors"][c["id"]] = "no SKILL.md for %s" % c["skill"]
            continue
        meta["skills"][c["skill"]] = sha(skill_md)
        with tempfile.TemporaryDirectory() as tmp:
            cmd = build_cmd(a, c, os.path.abspath(skill_md), tmp)
            if a.dry_run:
                print(" ".join(repr(x) if (" " in x or not x) else x for x in cmd))
                continue
            try:
                p = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True, timeout=a.timeout)
                d = json.loads(p.stdout)
            except (subprocess.TimeoutExpired, ValueError) as e:
                meta["errors"][c["id"]] = "%s: %s" % (type(e).__name__, str(e)[:200])
                continue
        if d.get("is_error"):
            meta["errors"][c["id"]] = str(d.get("result"))[:300]
            continue
        responses[c["id"]] = d.get("result", "")
        for m in (d.get("modelUsage") or {}):
            if m not in meta["models_seen"]:
                meta["models_seen"].append(m)
        print("ok", c["id"], file=sys.stderr)
        json.dump({"meta": meta, "responses": responses}, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)

    if not a.dry_run:
        after = subprocess.run([a.claude, "-v"], capture_output=True, text=True).stdout.strip()
        if after != version:
            meta["errors"]["_version"] = "Claude Code changed during the run: %s -> %s. Rerun." % (version, after)
        json.dump({"meta": meta, "responses": responses}, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("wrote %s: %d replies, %d errors" % (a.out, len(responses), len(meta["errors"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
