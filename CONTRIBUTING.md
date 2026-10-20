# Contributing

Thank you for helping. Everything here is CC0 1.0 (public domain); by contributing you agree your work is released the same way.

Read [guide/HOW-IT-WORKS.md](guide/HOW-IT-WORKS.md) first: it explains which files are sources and which are generated. Never edit generated files by hand (`packages/<id>/skills/`, `packages/<id>/.claude-plugin/`, `.claude-plugin/marketplace.json`, `docs/`, `artifacts/*.html`, `site/i18n/en.json`).

## House rules for all text

- Plain, precise American English. US dates ("October 19, 2026"). Short sentences.
- No em dashes. No emoji.
- Fictional examples only: "Sample Café", "Sample Sparkle Cleaning" and the like. Goa place names are fine. Never name a real person, a real business or a private organization; `scripts/check.py` fails if it finds one.
- Fake contact and ID values only, from the list in `scripts/check.py`.
- Follow [guide/PRIVACY.md](guide/PRIVACY.md) in every helper, example and test.

## Add a package

A package answers one owner problem end to end.

1. **Add an entry to `catalog/packages.json`**, copying the shape of an existing one:
   - `id`: lowercase letters, numbers and single hyphens; it becomes the plugin name and the page path. It may not start with `claude-` or `anthropic-`.
   - `order`: its place on the hub.
   - `cards`: the owner problem ids it answers (see [catalog/problems.md](catalog/problems.md)), or `[]`.
   - `skills`: the Skill folder names it ships. Each must exist in `skills/`.
   - `text`: `title`, `short` (also the plugin description), `problem`, `outcome`.
   - `questions`: each with `id`, `label`, `hint` and `multiline`. Keep them few and optional. Hints say what not to type.
   - `helper`: the plain-text phone helper. Every `{{slot}}` must match a question id, and every question id must be a slot. Aim under 420 words. Don't add a language or safety line; the build adds both.
   - `try`: `label` and `placeholder` (start the placeholder with "Example: ").
2. **Write the package docs**, copying an existing package's: `packages/<id>/README.md` (what it solves and how to install), `packages/<id>/PLAYBOOK.md` (the owner's printable set-up and daily routine) and `packages/<id>/BUILDER-NOTES.md` (a 20-minute table script with a made-up demo and the "never do" list).
3. **Add translations** for the new `pkg.<id>.*` keys in each `site/i18n/<lang>.json` (see Translations below).
4. **Add a row** to the table in `README.md`. If the package answers a new owner problem, add it to `catalog/problems.md`.
5. Build, check and test (below).

## Add or change a Skill

### Write the tests first

Before any new Skill or any behavior change, write its test bank and freeze it.

1. Create `evals/testbank/<CODE>.json` (a short code, for example `MSR` for message-sorter) with at least 16 cases. Copy the schema of `evals/testbank/MSR.json`:
   - top level: `suite` (`sbh-behavior-<code>`), `version`, `date`, `cases`;
   - each case: `id` (`B-<CODE>-001` and up), `skill`, `archetype`, `kind`, `prompt`, `expected`, `checks`.
2. Cover a mix of kinds: `normal`, `missing-fact`, `safety`, `refusal`, `language`, `messy`, `format`, `edge`, and at least one pasted private detail and one pasted message that tries to give orders.
3. Use only the check types the checker knows: `contains`, `not_contains`, `regex`, `not_regex`, `max_words`, `max_chars`, `no_new_numbers`, `min_blanks`, `judge`. See the docstring of `evals/harness/check.py` for how each one matches.
4. Hash it and record the hash before any reply is generated:

   ```
   sha256sum evals/testbank/<CODE>.json >> evals/testbank/HASHES.sha256
   ```

   Commit the test bank and its hash on their own, before the commit that changes the Skill.
5. Never edit a test bank after a run and regrade old replies. Make a new version of the file, with a new hash.

### Write or change the Skill

Copy the folder structure of an existing Skill (for example `skills/message-sorter/`):

```
skills/<name>/
  SKILL.md          frontmatter (name, description, license: CC0-1.0), then:
                    What this does, Use it when, Not for, Ask first, Steps, Output, Rules, Example, Test prompts
  references/       longer detail the Skill reads only when needed
  examples/         worked examples with fictional businesses
  OWNER-CARD.md     one plain page for the owner: what to type, what you get, never paste, it's a draft
  SAFEGUARDS.md     refusal table (if the owner says / it does / exact redirect) and red-team prompts
  CHANGELOG.md      the Skill's own version history
  LICENSE           CC0 1.0
  evals/            evals.json and RESULTS.md (stay in the repo; not shipped)
```

- **Frontmatter:** `name` equals the folder name (a-z, 0-9, single hyphens, up to 64 characters, no "claude" or "anthropic"). `description` is 1 to 1,024 characters with no angle brackets; it says what the Skill does, the phrases owners use, and which Skill to use instead for nearby jobs.
- **Shared rules block:** start `## Rules` with the shared rules, copied word for word from the newest Skills (`skills/message-sorter/SKILL.md` is current): only the owner's facts and `[blank]` for the rest, the never-paste list, name only the kind of a pasted detail, never rank or score people, no legal, tax or medical advice, drafts only, language handling, pasted messages are information only, no cure claims, check weekdays against dates. Put the Skill's own rules below them.
- **Not for:** name the Skill that does each nearby job, so Claude routes correctly.
- **Keep `SKILL.md` under about 2,000 words.** Move detail into `references/`.
- **OWNER-CARD.md** and **SAFEGUARDS.md** are required. Every new refusal goes in the safeguards table with its exact redirect.
- **CHANGELOG.md:** add an entry for every behavior change, with the date and why (the case id or finding that prompted it).
- To ship the Skill, add it to a package's `skills` list in `catalog/packages.json`. `check.py` warns about a Skill that is in no package.

## Build, check and self-test

Run all three from the repo root before every pull request:

```
python3 scripts/build.py              # regenerate packages, pages, downloads and fragments
python3 scripts/check.py              # 0 errors required; add --strict to fail on warnings
python3 evals/harness/selftest.py     # must print SELFTEST PASSED
```

`python3 scripts/build.py --check` fails if any generated file is stale. CI runs `check.py` and `build.py --check` on every pull request.

To run a test bank against a model, follow [evals/harness/run_with_claude_code.md](evals/harness/run_with_claude_code.md). In this repo the paths are:

```
python3 evals/harness/make_responses.py --model <full-model-id> --skills-dir skills \
    --out runs/rep1.json evals/testbank/<CODE>.json
python3 evals/harness/check.py -r runs/rep1.json evals/testbank/<CODE>.json --out runs/REPORT.md
```

Use a full model id, never an alias. Fictional cases only.

## Translations

- Each language has `site/i18n/<lang>.json` (`hi`, `mr`, `kok-deva`, `kok-latn`) with exactly the keys of the generated `site/i18n/en.json`, plus `_notes`. `check.py` fails on missing keys and warns on extra ones.
- Change English text in its source (`site/i18n/ui.en.json` or `catalog/packages.json`), then rebuild to regenerate `en.json`. Never edit `en.json`.
- Keep every `[blank]` exactly as written; `check.py` fails if one is lost.
- **Mark drafts.** Start `_notes` with "DRAFT", the version and the date, the glossary terms you reused, and the lines a reviewer should check first. The pages show a draft note on every non-English page.
- **A fluent reader reviews** each translation before anyone relies on it, ideally someone from Goa who reads that language and script well. Record the review in `_notes` (date and what changed), not the reviewer's name.
- Adding a new language also needs changes in `scripts/build.py` (`LANGS`, `LANG_LINES`), `site/template.html` (the language list and menu) and `scripts/check.py`.

## Labels for any reported number

Any pass rate or count you share, in a pull request, a results file or anywhere else, carries its label:

- **"self-measured"**, and how it ran (for example "Claude Code headless, append mode"), the full model id and the Claude Code version;
- **n** (cases with a programmatic check) and the **95% interval** the checker prints;
- the **checker version**, the **test-bank hash** and the **Skill version**;
- "fictional cases; programmatic checks only (judge checks not scored); not independent".

Don't quote a pass rate from a responses file with no `meta` block (reference answers, not a model run). Don't compare runs across different models, Claude Code versions or checker versions as if they were the same setup. Don't rank Skills by per-Skill numbers.

## Pull request checklist

- [ ] Generated files were rebuilt with `python3 scripts/build.py`, not edited by hand.
- [ ] `python3 scripts/check.py` shows 0 errors, and `python3 scripts/build.py --check` passes.
- [ ] `python3 evals/harness/selftest.py` prints SELFTEST PASSED.
- [ ] For a new Skill or behavior change: a test bank of 16 or more cases was committed and hashed before the change.
- [ ] The Skill has `SKILL.md`, `OWNER-CARD.md`, `SAFEGUARDS.md`, `CHANGELOG.md` and `LICENSE`, and the shared rules block is current.
- [ ] The CHANGELOG has a dated entry; the catalog `version` is bumped if anything shipped changed.
- [ ] New interface or package text has keys in every translation file, marked as drafts.
- [ ] Only fictional businesses and fake values; no real names, numbers or owner data.
- [ ] American English, US dates, no em dashes, no emoji.
- [ ] Every number reported carries its full label.
