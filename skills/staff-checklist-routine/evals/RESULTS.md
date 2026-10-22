# Results: staff-checklist-routine

Cases pre-registered October 20, 2026. The test bank SCL.json was run on v1.0.0: 14/16 cases passed (self-measured, programmatic checks only; not independent). Details: `evals/RESULTS.md` at the repo root. `evals/evals.json` has not been run.

- `evals/evals.json`: 7 cases. SHA-256 at pre-registration: `38831664f763d22b6a53283bc618e0273e14c146d2a761cd6a937cb6097420e0`
- Behavior test bank: `evals/testbank/SCL.json` at the repo root (suite sbh-behavior-scl, 16 cases), SHA-256 `4a84294c2b18180f434bade84f758302eeb9853cd58db6a8580b7efb6e64708f`, registered in `evals/testbank/HASHES.sha256`.
- The worked example (`examples/example-01.md`) was checked by hand against the programmatic checks of B-SCL-001 while the bank was written. That is a sanity check of the checks, not a model run.
- Before any run, one wording change was made on October 20, 2026: the term for the owner's pasted card was replaced with "planning card" in the cases that paste one (the repo's private-name check flagged the old term). The hashes above are the ones registered after that change.

## Assumptions to check with a real owner
(These come from a builder page and owners' planning cards, not interviews. Someone who works with owners should check them.)
1. Owners already have a staff WhatsApp group, and someone in it can pin messages (or the owner is the admin).
2. Pinned messages last 30 days at most, so a monthly re-pin reminder is needed. Check the pin options on the phones owners use.
3. A checklist of 8 to 12 short lines in one copy box is readable on a staff member's phone without scrolling sideways.
4. Staff are comfortable sending one photo of the finished space, and owners accept that photos are never used to check who or when.
5. A 10-minute weekly huddle that changes one line is realistic for small teams with shifts.
6. A staff member can read and correct a Hindi, Marathi or Konkani translation before it is pinned.
