# Results: customer-messages-routine

Cases pre-registered October 20, 2026. The test bank CMR.json was run on v1.0.0: 13/16 cases passed (self-measured, programmatic checks only; not independent). Details: `evals/RESULTS.md` at the repo root. `evals/evals.json` has not been run.

- `evals/evals.json`: 6 cases. SHA-256 at pre-registration: `b11b48fd53cbaaca4bf4abda6d83939ec9aab390e543348068b90807af5f3e1e`
- Test bank: `evals/testbank/CMR.json` at the repo root (suite sbh-behavior-cmr, 16 cases), hash registered in `evals/testbank/HASHES.sha256` (re-registered once on October 20, 2026 after a wording-only change, before any run).
- Sanity check only (not a model run): the worked answer in `examples/example-01.md` passes every programmatic check of case B-CMR-001 with checker v1.2.

## Assumptions to check with a real owner
(These come from a builder's workflow page and owners' planning cards. Someone who works with owners should check them.)
1. Owners will spend about 10 minutes once to type 3 quick replies, an away message and 5 labels into WhatsApp Business, ideally with a builder sitting beside them.
2. Five labels (New, Replied, Follow up, Booked, Not now) are few enough to keep up on a busy weekend. Check whether owners drop "Replied" after the first week.
3. Two follow-ups (day 2 and day 7) feel helpful to customers in Goa, not pushy. Check with a tours business and a cleaning service.
4. Owners will actually open "Message yourself" and paste the "my helper" prompt into a free AI chat, and a prompt under 600 characters is short enough to keep there.
5. A paper list with "what they asked" instead of names is enough for owners on normal WhatsApp to find the right chat again.
