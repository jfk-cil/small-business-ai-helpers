# Results: get-paid-routine

Cases pre-registered October 20, 2026. The test bank GPR.json was run on v1.0.0: 13/16 cases passed (self-measured, programmatic checks only; not independent). Details: `evals/RESULTS.md` at the repo root. `evals/evals.json` has not been run.

- `evals/evals.json`: 6 cases. SHA-256 at pre-registration: `3f2fded7522b48a7f66eac910a672b48331884bb4dd23eaaa444b3f71a50ee3b`
- Test bank: `evals/testbank/GPR.json` at the repo root (suite sbh-behavior-gpr, 16 cases), hash registered in `evals/testbank/HASHES.sha256` (re-registered once on October 20, 2026 after a wording-only change, before any run).
- Sanity check only (not a model run): the worked answer in `examples/example-01.md` passes every programmatic check of case B-GPR-001 with checker v1.2.

## Assumptions to check with a real owner
(These come from a builder's workflow page and owners' planning cards. Someone who works with owners should check them.)
1. Owners are willing to keep the "who owes what" list on paper or a private sheet, and fill in [amount], [job], [due date] and [your UPI ID] on their phone each time, rather than have the AI fill them.
2. A friendly /pay1 and a final, polite /pay2, then a phone call, is the right order in Goa. Check whether some owners prefer a call first for regular customers.
3. "Job" written as the work ("chocolate cake, Saturday delivery") is enough for the owner to know who it is without writing a name.
4. One weekly 10-minute check is often enough for deposit-based businesses; cake orders with short lead times may need a quick daily glance.
5. Owners understand that GST, invoices and disputes go to their accountant or a qualified person, and don't expect the helper to answer them.
