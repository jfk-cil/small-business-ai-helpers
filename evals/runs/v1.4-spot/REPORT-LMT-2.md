# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-21 19:58 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.306 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `subset-of-testbank/LMT-subset2.json` | testbank | `51ce4fc2154639b6a91240983940737c32a6ccd7b9ea83ebf77a3318a0e2e8f9` |
| `../runs/v1.4-spot/LMT-2.json` | responses (replicate 1) | `41ef1509cab4bdd15b2640457a5e0c2e4e3713d79a502816482a08b0c126a17b` |

## Overall

- Cases in testbanks: 1. With a reply in every replicate: 1. Scored (has a programmatic check): 1.
- Case pass rate, replicate 1: 1/1 = 100.0% (95% CI 20.7–100.0)
- Check pass rate (all programmatic checks, all replicates): 5/5 = 100.0% (95% CI 56.6–100.0)


## By skill

| Skill | passed | n | rate | 95% CI |
|---|---|---|---|---|
| listing-matcher | 1 | 1 | 100% | 21–100% |

## By kind

| Kind | passed | n | rate | 95% CI |
|---|---|---|---|---|
| messy | 1 | 1 | 100% | 21–100% |

## By archetype

| Archetype | passed | n | rate | 95% CI |
|---|---|---|---|---|
| real-estate-agent | 1 | 1 | 100% | 21–100% |

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

None.

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (1, in 1 cases) not yet scored. Case pass rates above leave them out.

- B-LMT-008: The row follows the column order with one value per column and invents no source, status, price or feature.

## Missing replies

None.

## Method notes

- A case passes only when every programmatic check passes. Judge checks are listed, not scored.
- Length checks measured: the whole reply, including any notes around the draft.
- Checker v1.2. Cases were pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2). Compare numbers only under the same checker version.
- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; ₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and 2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and character counters are skipped. Number words ("three nights") are not checked.
- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and contains values); length checks measure the reply as given.
- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an independent test.
