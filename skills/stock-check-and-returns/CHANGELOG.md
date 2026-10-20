# Changelog

## v1.0.1 (October 20, 2026)
Fixes from the first test run (evals/RESULTS.md).
- If a references/ file can't be opened, the Skill writes that part from its Output section instead of stopping.
- Roles, never names, also in notes to the owner.
- The new-staff how-to counts its title and common mistakes in the 200-word limit.
- An owner-given return term stays out of the supplier message; the supplier is asked to confirm their terms.
- Review fixes: the staff how-to handles packs that show only a packing date; the safeguards no longer offer to quote an owner's return term.

## v1.0.0 (October 20, 2026)
- First version, written for the small-business AI helpers reference packages.
- Four parts from one owner request: a monthly routine (each step given to a role, with a day of the month, a duration, "Done when" and a sign-off line), a first-time how-to for new staff (200 words or fewer, billing steps as [menu name in your billing software]), tracker columns with quantities and dates only (building the sheet goes to tracker-sheet-builder), and supplier messages (a return or pickup request, one polite follow-up, and what to do if there's no reply).
- Safety rules: uses the owner's near-expiry or slow window exactly; never decides whether expired or near-expiry items are safe to sell, donate, discount or throw away ("check with a qualified person and your supplier's terms"); never invents supplier terms, return windows, credit notes or deadlines; no money in the chat or tracker; staff are roles, never rated.
- References: routine-steps.md (default routines for expiry, supplier returns, damaged and slow stock), staff-how-to.md and supplier-messages.md.
- Test bank evals/testbank/SCR.json (16 cases) and evals/evals.json (7 cases), pre-registered October 20, 2026.
