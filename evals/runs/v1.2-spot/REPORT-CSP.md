# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-20 07:16 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.304 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `testbank/CSP.json (subset of the pre-registered cases)` | testbank | `a2978fc57cb27b0ab0575638eaab750ff3944d44e49027b2f70047daf90a9191` |
| `../runs/v1.2-spot/CSP.json` | responses (replicate 1) | `924e70540dba9181bab151668843f1bc6fd8706ffab427820f883cd089ea9074` |

## Overall

- Cases in testbanks: 3. With a reply in every replicate: 3. Scored (has a programmatic check): 3.
- Case pass rate, replicate 1: 1/3 = 33.3% (95% CI 6.1–79.2)
- Check pass rate (all programmatic checks, all replicates): 41/44 = 93.2% (95% CI 81.8–97.7)


## By skill

| Skill | passed | n | rate | 95% CI |
|---|---|---|---|---|
| channel-sales-plan | 1 | 3 | 33% | 6–79% |

## By kind

| Kind | passed | n | rate | 95% CI |
|---|---|---|---|---|
| messy | 0 | 1 | 0% | 0–79% |
| normal | 1 | 2 | 50% | 9–91% |

## By archetype

| Archetype | passed | n | rate | 95% CI |
|---|---|---|---|---|
| cake-studio | 1 | 1 | 100% | 21–100% |
| coffee-roaster | 0 | 1 | 0% | 0–79% |
| goan-sweets | 0 | 1 | 0% | 0–79% |

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

### B-CSP-002: channel-sales-plan / normal / coffee-roaster
- **contains** `[your business name]`: missing '[your business name]'
  > **Your 3-month sales plan: Sample Roasters** ⏎ November to January (you didn't give a start month, so I started next month) · Cafés and homest…
- **regex** `(?im)^Month\t[^\n]*orders[^\n]*sign-ups`: no match for /(?im)^Month\t[^\n]*orders[^\n]*sign-ups/
  > **Your 3-month sales plan: Sample Roasters** ⏎ November to January (you didn't give a start month, so I started next month) · Cafés and homest…

### B-CSP-008: channel-sales-plan / messy / goan-sweets
- **regex** `(?i)check-?in`: no match for /(?i)check-?in/
  > **Your 6-month sales plan: [your business name]** ⏎ December to May · Shops, WhatsApp orders, Facebook page · 3 hours a week ⏎  ⏎ Christmas is you…

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (3, in 3 cases) not yet scored. Case pass rates above leave them out.

- B-CSP-002: It says which month it started with in one line, does not state which months the tourist season or monsoon are, and the weekly minutes add up to 2 hours or less.
- B-CSP-005: Only the two channels the owner named are planned, with no business-to-business section; the rhythm fits 90 minutes a week.
- B-CSP-008: Existing shops get a check-in and reorder step, new shops get the first message; the rhythm fits 3 hours a week.

## Missing replies

None.

## Method notes

- A case passes only when every programmatic check passes. Judge checks are listed, not scored.
- Length checks measured: the whole reply, including any notes around the draft.
- Checker v1.2. Cases were pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2). Compare numbers only under the same checker version.
- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; ₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and 2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and character counters are skipped. Number words ("three nights") are not checked.
- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and contains values); length checks measure the reply as given.
- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an independent test.
