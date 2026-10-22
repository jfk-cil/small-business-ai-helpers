# Results: helper-builder

Cases pre-registered October 20, 2026. The test bank HBD.json was run on v1.0.0: 11/16 cases passed (self-measured, programmatic checks only; not independent). Details: `evals/RESULTS.md` at the repo root. `evals/evals.json` has not been run.

- `evals/evals.json` (7 cases) SHA-256 at pre-registration: `87bdc6364b22de8372d5a88583688d31dc0692f8aca4088cfe16592718d9ac03`
- Behavior test bank: `evals/testbank/HBD.json` at the repo root (suite sbh-behavior-hbd, 16 cases), hash registered in `evals/testbank/HASHES.sha256`.
- Checker note: the test bank uses no `no_new_numbers` check, because every full reply carries the fixed made-up number 12345 67890 (Test 3) and `CC0-1.0` (part D), which are not the owner's numbers. Invented prices and times are caught with `not_regex` checks instead.

## Assumptions to check with a real owner
(These come from planning cards and a builder page. Someone who works with owners should check them.)
1. Owners will save a helper prompt (in WhatsApp "Message yourself" or notes) and paste it at the top of a new chat each time, rather than retyping their facts.
2. 900 characters is enough for one job's facts plus the safety lines; owners with long price lists are fine pasting "more facts" after it.
3. Owners will run the 5 self-test messages once and come back when one fails.
4. Owners on a paid Claude plan can follow three setup lines to make a Project and add a facts file.
5. Builders find the minimal SKILL.md draft a useful start, and will add the shared rules block, owner card, safeguards and evals before publishing.
