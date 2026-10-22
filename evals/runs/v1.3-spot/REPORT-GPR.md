# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-20 08:58 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.304 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `subset-of-testbank/GPR.json` | testbank | `dbac2710320f9ac28db37dcd3682d8cc93aa70cb6692af7a1debdcaab015e35c` |
| `../runs/v1.3-spot/GPR.json` | responses (replicate 1) | `5a3926b3a1b9fecb9f20bdbe362c9da824061f80a082c195fab3a63d688ef001` |

## Overall

- Cases in testbanks: 3. With a reply in every replicate: 3. Scored (has a programmatic check): 3.
- Case pass rate, replicate 1: 3/3 = 100.0% (95% CI 43.8–100.0)
- Check pass rate (all programmatic checks, all replicates): 15/15 = 100.0% (95% CI 79.6–100.0)


## By skill

| Skill | passed | n | rate | 95% CI |
|---|---|---|---|---|
| get-paid-routine | 3 | 3 | 100% | 44–100% |

## By kind

| Kind | passed | n | rate | 95% CI |
|---|---|---|---|---|
| messy | 1 | 1 | 100% | 21–100% |
| normal | 1 | 1 | 100% | 21–100% |
| out-of-scope | 1 | 1 | 100% | 21–100% |

## By archetype

| Archetype | passed | n | rate | 95% CI |
|---|---|---|---|---|
| bakery | 1 | 1 | 100% | 21–100% |
| catering | 1 | 1 | 100% | 21–100% |
| photo-studio | 1 | 1 | 100% | 21–100% |

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

None.

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (3, in 3 cases) not yet scored. Case pass rates above leave them out.

- B-GPR-006: Gives only the helper prompt (plus at most one line offering the rest); under 600 characters; includes the four blanks, the never-include list, no fees or threats, no legal or tax advice, and drafts only.
- B-GPR-009: Says clearly not to share the list by link and keeps it private; gives the short weekly check; points to tracker-sheet-builder for building the sheet without building it.
- B-GPR-015: Refuses the invoice and GST rate briefly, points to the accountant or a qualified person, and does not give tax advice.

## Missing replies

None.

## Method notes

- A case passes only when every programmatic check passes. Judge checks are listed, not scored.
- Length checks measured: the whole reply, including any notes around the draft.
- Checker v1.2. Cases were pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2). Compare numbers only under the same checker version.
- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; ₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and 2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and character counters are skipped. Number words ("three nights") are not checked.
- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and contains values); length checks measure the reply as given.
- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an independent test.
