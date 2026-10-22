# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-20 08:58 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.304 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `subset-of-testbank/CMR.json` | testbank | `0ca27ece91726f94ce13d031534b5e70e0d5c43d3512871da2944bd421756f18` |
| `../runs/v1.3-spot/CMR.json` | responses (replicate 1) | `9aabacd0dfd68697035f79075aee7d3add3533c019eaf2579de9c44026200ee0` |

## Overall

- Cases in testbanks: 2. With a reply in every replicate: 2. Scored (has a programmatic check): 2.
- Case pass rate, replicate 1: 2/2 = 100.0% (95% CI 34.2–100.0)
- Check pass rate (all programmatic checks, all replicates): 12/12 = 100.0% (95% CI 75.7–100.0)


## By skill

| Skill | passed | n | rate | 95% CI |
|---|---|---|---|---|
| customer-messages-routine | 2 | 2 | 100% | 34–100% |

## By kind

| Kind | passed | n | rate | 95% CI |
|---|---|---|---|---|
| normal | 2 | 2 | 100% | 34–100% |

## By archetype

| Archetype | passed | n | rate | 95% CI |
|---|---|---|---|---|
| bakery | 1 | 1 | 100% | 21–100% |
| homestay | 1 | 1 | 100% | 21–100% |

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

None.

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (2, in 2 cases) not yet scored. Case pass rates above leave them out.

- B-CMR-002: It gives the normal-WhatsApp paper version (replies saved in Message yourself, a paper list whose columns use what was asked rather than names) and does not tell the owner to use labels or quick replies as if they exist in normal WhatsApp; at most one line suggests WhatsApp Business.
- B-CMR-006: Writes one gentle day-2 follow-up for this one chat (no pressure, no invented offer), states the day 2 and day 7 limit and the stop-on-no rule, does not write a message for last month's contacts, and hands the many-people message to customer-message-writer in two or three lines.

## Missing replies

None.

## Method notes

- A case passes only when every programmatic check passes. Judge checks are listed, not scored.
- Length checks measured: the whole reply, including any notes around the draft.
- Checker v1.2. Cases were pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2). Compare numbers only under the same checker version.
- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; ₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and 2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and character counters are skipped. Number words ("three nights") are not checked.
- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and contains values); length checks measure the reply as given.
- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an independent test.
