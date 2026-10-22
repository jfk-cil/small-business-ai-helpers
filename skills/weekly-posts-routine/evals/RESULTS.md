# Results: weekly-posts-routine

Cases pre-registered October 20, 2026. The test bank WPR.json was run on v1.0.0: 15/16 cases passed (self-measured, programmatic checks only; not independent). Details: `evals/RESULTS.md` at the repo root. `evals/evals.json` has not been run.

- `evals/evals.json`: 7 cases. SHA-256 at pre-registration: `ada7302d0d27d95a3abe66a0044d180561261f37ef6c448b072f57c19691f5f8`
- Behavior test bank: `evals/testbank/WPR.json` at the repo root (suite sbh-behavior-wpr, 16 cases), SHA-256 `287352d37fb32ad87eeb803c66c0f1280628c7c46dda86eef67986a0c47c83a3`, registered in `evals/testbank/HASHES.sha256`.
- The worked example (`examples/example-01.md`) was checked by hand against the programmatic checks of B-WPR-001 while the bank was written. That is a sanity check of the checks, not a model run.
- Before any run, one wording change was made on October 20, 2026: the term for the owner's pasted card was replaced with "planning card" in the cases that paste one (the repo's private-name check flagged the old term). The hashes above are the ones registered after that change.

## Assumptions to check with a real owner
(These come from a builder page and owners' planning cards, not interviews. Someone who works with owners should check them.)
1. Owners who "post when they remember" will keep a phone album and a 20-minute weekly sitting more easily than a planned month of posts.
2. Describing 3 photos in a few words is quicker for owners than uploading them, and keeps people and children out of the chat.
3. Saving two posts as drafts in the app they already use is enough; owners don't need a scheduling tool.
4. A "my helper" prompt kept in WhatsApp "Message yourself" is easy to find and paste each week on an Android phone.
5. Owners can open and edit their own Google Business Profile once a month; those who can't need google-profile-builder first.
6. The copy boxes paste cleanly into a social app's caption field and into WhatsApp.
