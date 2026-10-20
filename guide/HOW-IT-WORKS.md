# How it works

The design rule is **simple front end, robust back end**. An owner sees one phone page, a few questions and a Copy button. Behind that page sit full Skills with references, written safeguards, owner cards, pre-registered test banks, a checker and repository checks that run on every change.

## The owner-facing layer

One template, `site/template.html`, makes every phone page: a hub (`docs/index.html`) and one page per package (`docs/<id>/index.html`).

What an owner does on a page:

1. **Answers a few questions** about the business (hours, prices, tone, what must come to them). Every question is optional; "pass" or an empty box is fine. The keyboard mic works.
2. **Taps "Make my helper".** The page assembles the helper text locally, in the browser: the package's helper template from `catalog/packages.json` with each `{{slot}}` filled from the answers, then a language line and a closing safety line. Nothing leaves the phone to do this.
3. **Taps "Copy helper", then "Open Claude"** (the helper is plain text, so it should also work in ChatGPT or Gemini; tested so far in Claude only). They paste it into a new chat and then paste a customer message or describe the job.
4. **Saves the helper** in WhatsApp "Message yourself" to reuse it any day, even after free credits end.

Other parts of the page:

- **Privacy scan in the page.** Before a helper is made, the page scans the answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card or account numbers, IFSC codes, passport numbers, and passwords or OTPs. If it finds one, it names the kind and does not make the helper until the owner takes it out. The same scan runs on the "Try it here" box. It is a safety net, not a guarantee; see [PRIVACY.md](PRIVACY.md).
- **"Try it here" inside Claude pages.** When the page runs as a Claude page (from `artifacts/`), it asks for the page's own Claude access (the `sample` capability). If the viewer allows it, a box appears where they can paste a fictional or cleaned-up message and see the helper's answer on the page. It runs on the viewer's own Claude account, not the publisher's. Nothing is saved. If the viewer declines, or the page is opened on GitHub Pages, the box stays hidden and Copy plus Open Claude still work.
- **Five languages:** English, Hindi, Marathi, Konkani in Devanagari and Konkani in Roman script. The language line in the helper tells the AI to reply in that language and to end each reply to the owner (not the drafts) with "Please check this with someone who reads it well." Non-English pages show a note that the translation is a draft.
- **Laptop section:** a Download link for each Skill zip and the two Claude Code commands for the package.
- **Nothing stored.** The only thing the page keeps is the chosen language, in the browser's own storage (`sbh-lang`). There are no accounts, no analytics and no external scripts; `scripts/check.py` fails a build that adds one. The page uses the phone's own fonts, so it makes no requests to other sites.

## The back end

| Part | Where | What it is for |
|---|---|---|
| Skills | `skills/<name>/SKILL.md` | The full helper: when to use it, what to ask, steps, output format, rules, an example and test prompts. Claude loads it when the owner asks for that job. |
| References | `skills/<name>/references/` | Longer detail a Skill reads only when needed (domain notes, setup steps, templates), so `SKILL.md` stays short. |
| Examples | `skills/<name>/examples/` | Worked examples with fictional "Sample" businesses. |
| Safeguards | `skills/<name>/SAFEGUARDS.md` | What the Skill refuses, the exact redirect it gives, and red-team prompts with the expected safe behavior. |
| Owner card | `skills/<name>/OWNER-CARD.md` | One plain page for the owner: what to type, what you get, what never to paste. |
| Changelog | `skills/<name>/CHANGELOG.md` | The Skill's own version history. |
| Skill evals | `skills/<name>/evals/` | A few quick cases and a results note. Kept in the repo; not copied into packages or zips. |
| Test banks | `evals/testbank/<CODE>.json` | 16 to 20 pre-registered behavior cases per Skill, with programmatic checks and judge notes. |
| Harness | `evals/harness/` | `check.py` grades replies, `make_responses.py` runs cases through Claude Code, `route_check.py` grades which Skill gets picked, `selftest.py` tests the graders. |
| Repository checks | `scripts/check.py` | Skill frontmatter and required files, catalog consistency, test-bank schema, translation keys, page safety, privacy scan of the repo, style warnings. |
| CI | `.github/workflows/` | Runs `scripts/check.py` and `scripts/build.py --check` on every push and pull request. |

## Sources and generated files

This table is copied from the docstring of `scripts/build.py`.

| Sources (edit these) | |
|---|---|
| `catalog/packages.json` | packages, their skills, questions and helper templates (English) |
| `skills/<name>/` | one folder per Skill (the single source of truth) |
| `site/template.html` | the phone page (one template for every page) |
| `site/i18n/ui.en.json` | English interface text |
| `site/i18n/<lang>.json` | translations (hi, mr, kok-deva, kok-latn); keys match en.json |

| Generated (never edit by hand) | |
|---|---|
| `site/i18n/en.json` | English source table for translators |
| `packages/<id>/skills/<skill>/` | copies of the Skills each package uses |
| `packages/<id>/.claude-plugin/plugin.json` | plugin manifest for each package |
| `.claude-plugin/marketplace.json` | so Claude Code and Cowork can install packages |
| `docs/index.html`, `docs/<id>/index.html` | phone pages (GitHub Pages serves `/docs`) |
| `docs/downloads/<skill>.zip` | one-click Skill downloads for claude.ai upload |
| `artifacts/<page>.html` | the same pages as Claude artifact fragments |

`python3 scripts/build.py --check` rebuilds everything in a temporary folder and fails if any generated file differs from what is committed. `artifacts/urls.json` is hand-written and is not generated (see [DEPLOY.md](DEPLOY.md)). The package docs `packages/<id>/README.md`, `PLAYBOOK.md` and `BUILDER-NOTES.md` are also hand-written; they live beside the generated `skills/` and `.claude-plugin/` folders.

### Why Skills live once in `skills/` and are copied into `packages/`

- **One fix, everywhere.** Several packages share a Skill: `tracker-sheet-builder` is in three packages and `sop-and-checklist-writer` is in two. Each Skill is written once in `skills/`, so a safety fix lands in one place and reaches every package on the next build.
- **Plugins must be self-contained.** Claude Code and Cowork install a package from its own folder (`./packages/<id>`), and an installed plugin cannot reach files outside that folder. So each package needs real copies of its Skills, not links.
- **Copies cannot drift.** The build deletes and recopies every `packages/<id>/skills/` folder, and `build.py --check` fails if a copy was edited by hand or left stale.
- **Tests stay in the repo.** Each Skill's `evals/` folder is left out of package copies and zips, so owners install only what the Skill needs.
- **Reproducible downloads.** Zips are written with a fixed timestamp (`ZIP_DATE` in `build.py`), so the same sources always give byte-identical zips and the stale check can compare them.

## How a package maps to owner problems

A package is one owner problem, answered end to end. Each entry in `catalog/packages.json` holds:

- `cards`: the owner problems it answers, by id (C1 to C10 in [catalog/problems.md](../catalog/problems.md)).
- `text.problem` and `text.outcome`: the problem in the owner's own terms and what they get.
- `questions`: the few facts the helper needs from the owner. Each question id is a `{{slot}}` in `helper`; `check.py` fails if they don't match.
- `helper`: the short phone version, plain text written for any chat AI.
- `try`: the label and example for the "Try it here" box.
- `skills`: the full versions for Claude, installed by upload or as a plugin.

| Package | Owner problems | Skills |
|---|---|---|
| start-here | none directly; for owners not sure which job to start with | first-task-finder |
| customer-replies | C3, C4 | message-sorter, guest-inquiry-replies, quote-and-proposal-writer |
| booking-reminders | C1 | booking-confirmations, tracker-sheet-builder |
| follow-ups | C8 | follow-up-planner, lead-reply-and-follow-up, tracker-sheet-builder, customer-message-writer |
| find-clients | C2 | target-customer-finder, outreach-email-writer, lead-qualifier, client-onboarding-writer |
| one-page-shop | C9 | storefront-page-builder, listing-and-catalog-writer, target-customer-finder |
| get-found-on-google | C6 | google-profile-builder, listing-and-catalog-writer, review-replies |
| staff-checklists | C5 | sop-and-checklist-writer, tracker-sheet-builder |
| hire-and-onboard | C7 | staff-hiring-and-onboarding, sop-and-checklist-writer |
| social-posts | C10 | social-content-planner, followers-to-customers, simple-marketing-plan |

The phone helper and the Skills answer the same problem at two depths. The helper gets an owner started in two minutes in Claude or another chat AI. The Skills add the longer rules, references, output formats and refusals, and are what the test banks measure.

## Versioning

- **Catalog version.** `version` and `date` in `catalog/packages.json` (now 1.1.1, October 20, 2026) are the release version of the whole collection. The build writes it into `.claude-plugin/marketplace.json`, every `packages/<id>/.claude-plugin/plugin.json`, and the footer line of every page ("v1.1.1 · github.com/jfk-cil/small-business-ai-helpers"). Bump it on every release that changes anything people install or open, so installed plugins can see an update:
  - patch (1.0.1): wording fixes, translation fixes, a Skill rule tightened;
  - minor (1.1.0): a new Skill, package, question or language;
  - major (2.0.0): a package removed or renamed, or a Skill renamed (install commands change).
- **Skill CHANGELOGs.** Each Skill keeps its own version in `skills/<name>/CHANGELOG.md`, independent of the catalog. Every behavior change gets an entry: the date, what changed and why (for example, the test case or audit finding that prompted it).
- **Test banks and checker.** Each test bank has its own `version`, and `evals/harness/check.py` has its own checker version. Any number reported must name the Skill version, the test-bank hash and the checker version that produced it.
