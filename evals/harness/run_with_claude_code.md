# Run the test cases with Claude Code on your Mac

This makes the responses file that `check.py` grades. It uses Claude Code in headless mode (`claude -p`). `make_responses.py` does the loop for you. Python 3 is all you need; there are no packages to install.

Checked against Claude Code 2.1.299 on October 14, 2026. One case ran end to end in `append` mode.

## 0. Before you start

- **Use fictional cases only.** Use only the cases in `evals/testbank/`. They use "Sample Café"-style businesses. Never put a real owner's message, a business name, or a row from owner notes into a prompt. Owner notes stay out of AI tools. If you want to test something an owner said, rewrite it as a new fictional case first. Then add it to a testbank file and record the new hash.
- **Run the self-test:** `python3 selftest.py`. It should print `SELFTEST PASSED`.
- **Freeze the inputs.** Note the SHA-256 of each testbank file and each `SKILL.md`. `make_responses.py` records them in the output's `meta` block. If a skill changes after a run, that is a new run.
- **Check the hashes** from `evals/testbank/`: `sha256sum -c HASHES.sha256`. Every line should say OK.
- **Two suites.** `testbank/*.json` is the pre-registered v1.0 bank (310 cases). `testbank-addon/ADDON-RT.json` (suite `goa-behavior-addon-rt`, 45 cases, ids `A-RT-…`) covers what the October 14 red team found untested: pasted-message injection, health claims, Form C, registration blanks, paid posts, payment reminders, consent, weekday/date checks, Sheets color rules, Airbnb limits, food words and blank style. It was hashed before any reply was generated. Run and report it separately from the v1.0 bank.

## 1. Pin the version and the model

```bash
claude -v                                   # write this down, e.g. 2.1.299 (Claude Code)
claude install 2.1.299                      # optional: install an exact version
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1   # stops auto-updates (and telemetry) mid-run
export CLAUDE_CODE_RETRY_WATCHDOG=1                 # wait out rate limits instead of failing a case
```

- **Model:** pass a full model ID, never an alias like `sonnet`, because aliases move to newer models. The script refuses aliases. Use the model owners will meet if you can. Claude Code can't pick the free claude.ai model for you, so write down which one you used.
- The script checks `claude -v` before and after the run. If the version changed, it writes an error into `meta.errors`, and you should rerun.
- `meta.models_seen` can list a small helper model next to yours. Claude Code uses one in the background. Check that the model you asked for is there.

## 2. One fresh session per case

Each case runs as its own `claude -p` process. It runs in an empty temp folder with `--no-session-persistence`, so no case can see another. The tools are switched off (`--tools ""`) because the skills only write text. Pick one of two ways to give Claude the skill.

**`append` (default; uses your normal Claude login).** The skill is "loaded":

```bash
python3 make_responses.py --model <full-model-id> --skills-dir ../skills \
    --out runs/rep1.json ../testbank/*.json
```

Under the hood, each case runs:
`claude -p --safe-mode --append-system-prompt-file <skill>/SKILL.md --no-session-persistence --model <id> --tools "" --output-format json "<prompt>"`.
`--safe-mode` keeps your own skills, plugins, CLAUDE.md and MCP servers from loading. They would change the answers.

**`slash` (closer to "installed"; needs an API key).** Bare mode does not use a subscription login:

```bash
export ANTHROPIC_API_KEY=...                # from the Claude Console
python3 make_responses.py --mode slash --model <full-model-id> --skills-dir ../skills \
    --out runs/rep1.json ../testbank/*.json
```

Each case copies only its skill into `<tmp>/.claude/skills/<skill>/`. Then it runs:
`claude --bare -p --add-dir <tmp> ... "/<skill> <prompt>"`.
Claude Code expands `/<skill>` into the skill text.

First try one case with `--only <case id>`, and read the reply. Make sure it follows the skill's `## Output` format. If it doesn't, the skill did not load. Use `--dry-run` to print the commands without running them. A stopped run resumes when you run the same command again.

Neither mode tests whether Claude *picks* the right skill on its own. That is routing, and `route_check.py` covers it. Neither mode is the claude.ai app on a phone. Claude Code adds its own system prompt, so treat the results as a close stand-in.

## 3. One replicate or two

- **One replicate** is fine for a first look and for fixing skills. Report it as one run.
- **Two replicates** are better for any number you share. Run the same command twice with `--replicate 2` and a second `--out` file. Then grade both runs together:

```bash
python3 check.py -r runs/rep1.json -r runs/rep2.json ../testbank/*.json --out runs/REPORT.md
python3 check.py -r runs/addon1.json ../testbank-addon/ADDON-RT.json --out runs/REPORT-ADDON-RT.md
```

The report gives each replicate's pass rate and a strict rate (passed in both). It also gives the instability count: cases that passed once and failed once. Instability means the skill wording is loose there. With n of about 15 per skill, two replicates won't tighten the per-skill intervals much. Their main use is catching flaky cases.

- **Length checks.** `max_words` and `max_chars` measure the whole reply, including notes around the draft. Add `--length-scope paste` to measure only the code blocks the owner would paste. Report which setting you used.

## 4. Label every number

Put this line next to every figure you share, with n, the 95% interval, and the testbank hash:

> self-measured, Claude Code headless (append mode), model <id>, Claude Code <version>, checker v1.2, fictional cases, programmatic checks only (judge checks not yet scored); not independent

Also say: "Cases pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2)." Older versions stay in `check_v1_0.py` and `check_v1_1.py` so earlier numbers can be reproduced; compare numbers only under the same checker version.

A responses file without a `meta` block (no model recorded) holds reference answers written by people or scripts, not a model run, and the report says so. Don't quote a pass rate from such a file.

Why "not independent": the people who wrote the skills (and the model family) also wrote the cases. Judge checks are listed but not scored. A blinded judge or someone who works with owners reading the replies has to mark them. Per-skill numbers don't support ranking the skills.

## 5. What not to do

- Don't paste real owner data, phone numbers, IDs, prices, or owner notes into any prompt or testbank.
- Don't edit a testbank after a run and regrade the old replies as if nothing changed. Make a new file with a new hash.
- Don't drop failed cases or relabel them after you see the results.
- Don't compare runs that used different models or Claude Code versions as if they were the same setup.
