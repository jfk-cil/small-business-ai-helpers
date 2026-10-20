# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-19 13:07 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.303 (Claude Code), mode append, replicate 1.
- Replicate 2 provenance: model run: claude-sonnet-5-5, 2.1.303 (Claude Code), mode append, replicate 1.
- Replicate 3 provenance: model run: claude-sonnet-5-5, 2.1.303 (Claude Code), mode append, replicate 1.
- Replicate 4 provenance: model run: claude-sonnet-5-5, 2.1.303 (Claude Code), mode append, replicate 1.
- Replicate 5 provenance: model run: claude-sonnet-5-5, 2.1.303 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `testbank/MSR.json` | testbank | `01141fde130998f7f3e939fcd44bb4fb5ae3c83b7a74a350ce0cd1cee8f392b7` |
| `testbank/BKC.json` | testbank | `186e9d9b28c3b24a4b1da64a18c47124c15bdadfb86af051a2bb18d3b5a1e6c7` |
| `testbank/FUP.json` | testbank | `42b1731abde0daae09efc69b472ee7dbc53e3735820be544ced62551fe0fd023` |
| `testbank/GPB.json` | testbank | `b9c6163a74a0a9bdf4ee703cb0201032f94d56efa3ff15bb0426fce01cf899f2` |
| `testbank/SHO.json` | testbank | `31c6321422a3adf2256cc07be795ffcb452a524d62a6b24ad63d64ee17124b04` |
| `runs/v1.0-new/MSR.json` | responses (replicate 1) | `7e5c5e56f387540369b5ccd41fae1809c55e84cd2088ca085a4a8fe6cb4a103f` |
| `runs/v1.0-new/BKC.json` | responses (replicate 2) | `e25a8af03abd72ba1ff29303d5191d1ea10fd01c53fc80ef1505e605efbeefe5` |
| `runs/v1.0-new/FUP.json` | responses (replicate 3) | `52a69c58c1d4d2ce086967e8e2ce1c8c4b5abbf68c7324dcc03d549477f0c082` |
| `runs/v1.0-new/GPB.json` | responses (replicate 4) | `8eae171e4d5ba0396000d12042811b6df6e06c6b8f22cccc4ed348285b4bfce1` |
| `runs/v1.0-new/SHO.json` | responses (replicate 5) | `134988575ae5ff8fa4814a5f311239be1d2d96f4d3ade500a52fd238cb90ca11` |

## Overall

- Cases in testbanks: 80. With a reply in every replicate: 0. Scored (has a programmatic check): 0.
- Case pass rate, replicate 1: n/a (0 graded)
- Case pass rate, replicate 2: n/a (0 graded)
- Case pass rate, replicate 3: n/a (0 graded)
- Case pass rate, replicate 4: n/a (0 graded)
- Case pass rate, replicate 5: n/a (0 graded)
- Passed in every replicate (strict): n/a (0 graded)
- Instability (pass in one replicate, fail in another): 0 of 0 cases
- Check pass rate (all programmatic checks, all replicates): n/a (0 graded)

Breakdowns below use the strict rule (passed in every replicate).

## By skill

_no scored cases_

## By kind

_no scored cases_

## By archetype

_no scored cases_

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

None.

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (0, in 0 cases) not yet scored. Case pass rates above leave them out.

None.

## Missing replies

B-MSR-001, B-MSR-002, B-MSR-003, B-MSR-004, B-MSR-005, B-MSR-006, B-MSR-007, B-MSR-008, B-MSR-009, B-MSR-010, B-MSR-011, B-MSR-012, B-MSR-013, B-MSR-014, B-MSR-015, B-MSR-016, B-BKC-001, B-BKC-002, B-BKC-003, B-BKC-004, B-BKC-005, B-BKC-006, B-BKC-007, B-BKC-008, B-BKC-009, B-BKC-010, B-BKC-011, B-BKC-012, B-BKC-013, B-BKC-014, B-BKC-015, B-BKC-016, B-FUP-001, B-FUP-002, B-FUP-003, B-FUP-004, B-FUP-005, B-FUP-006, B-FUP-007, B-FUP-008, B-FUP-009, B-FUP-010, B-FUP-011, B-FUP-012, B-FUP-013, B-FUP-014, B-FUP-015, B-FUP-016, B-GPB-001, B-GPB-002, B-GPB-003, B-GPB-004, B-GPB-005, B-GPB-006, B-GPB-007, B-GPB-008, B-GPB-009, B-GPB-010, B-GPB-011, B-GPB-012, B-GPB-013, B-GPB-014, B-GPB-015, B-GPB-016, B-SHO-001, B-SHO-002, B-SHO-003, B-SHO-004, B-SHO-005, B-SHO-006, B-SHO-007, B-SHO-008, B-SHO-009, B-SHO-010, B-SHO-011, B-SHO-012, B-SHO-013, B-SHO-014, B-SHO-015, B-SHO-016

## Method notes

- A case passes only when every programmatic check passes. Judge checks are listed, not scored.
- Length checks measured: the whole reply, including any notes around the draft.
- Checker v1.2. Cases were pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2). Compare numbers only under the same checker version.
- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; ₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and 2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and character counters are skipped. Number words ("three nights") are not checked.
- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and contains values); length checks measure the reply as given.
- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an independent test.
