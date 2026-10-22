# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-21 19:58 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.306 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `subset-of-testbank/LMT-subset.json` | testbank | `4b532ab34e2015dd79e21a2546a443d33c20473c91ce4d08e28a9e3f504bac11` |
| `../runs/v1.4-spot/LMT.json` | responses (replicate 1) | `40b32090e95b38ba6bd73e6f0171b4afab280136cf705bc79cfbf7a69b6de7f8` |

## Overall

- Cases in testbanks: 3. With a reply in every replicate: 3. Scored (has a programmatic check): 3.
- Case pass rate, replicate 1: 1/3 = 33.3% (95% CI 6.1–79.2)
- Check pass rate (all programmatic checks, all replicates): 16/18 = 88.9% (95% CI 67.2–96.9)


## By skill

| Skill | passed | n | rate | 95% CI |
|---|---|---|---|---|
| listing-matcher | 1 | 3 | 33% | 6–79% |

## By kind

| Kind | passed | n | rate | 95% CI |
|---|---|---|---|---|
| messy | 0 | 1 | 0% | 0–79% |
| normal | 1 | 2 | 50% | 9–91% |

## By archetype

| Archetype | passed | n | rate | 95% CI |
|---|---|---|---|---|
| real-estate-agent | 1 | 3 | 33% | 6–79% |

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

### B-LMT-001: listing-matcher / normal / real-estate-agent
- **contains** `[your business name]`: missing '[your business name]'
  > **Shortlist: 2BHK flat for rent, Porvorim or Alto Betim, ₹30,000 to ₹40,000 a month, from 1 November, covered parking, not ground level** ⏎  ⏎ *…

### B-LMT-008: listing-matcher / messy / real-estate-agent
- **contains** `[photo/video link]`: missing '[photo/video link]'
  > Here is the row, in the same order as the header, ready to paste into your sheet: ⏎  ⏎ ``` ⏎ PV-15	2BHK flat	Sale	Porvorim	1,150 sq ft	2	₹85 lakh	…

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (3, in 3 cases) not yet scored. Case pass rates above leave them out.

- B-LMT-001: PV-03 is the only Fits listing; PV-07 is Close with covered parking marked as unknown (Check); PV-09 is Close for the ground level deal-breaker; PV-12 is put aside; every reason uses only the row's facts.
- B-LMT-004: It says plainly that it can't open photo or video folders or keep listings between chats, gives the filter-and-paste routine, and calls a real searchable database a builder project.
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
