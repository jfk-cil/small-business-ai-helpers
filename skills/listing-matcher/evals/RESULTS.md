# Results: listing-matcher

Cases pre-registered October 21, 2026. First run below.

- `evals/evals.json` (7 cases) and the behavior test bank `evals/testbank/LMT.json` at the repo root (suite sbh-behavior-lmt, 16 cases).

## Assumptions to check with a real owner
(These come from one owner's notes. Someone who works with owners should check them.)
1. Agents will keep one row per listing with a short code, and will talk about listings by code and area rather than building or flat numbers.
2. Agents are willing to keep seller and landlord contacts in their phone or a private tab, and paste only the public columns.
3. A filter on the sheet, then copy and paste, is quick enough to do for each client on a phone.
4. Clients are happy to answer an 8-question form on WhatsApp, or agents will ask it on a call.
5. One message per listing plus a short summary is the format clients expect, with photos and videos sent from a folder link.


## First run, October 21, 2026

Self-measured, Claude Code headless (append mode), model claude-sonnet-5-5, one reply per case, programmatic checks only, checker v1.2; not independent. Test bank LMT (16 cases): 12/16 passed with v1.0.0. Two real misses (the reply tried to open a reference file) are fixed in v1.0.1 and passed a spot rerun. Details: evals/RESULTS.md at the repo root.
