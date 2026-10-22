# Changelog

## v0.2.3 (October 20, 2026)
- "Not for" and the description point to get-paid-routine for payment reminders saved as quick replies, a deposit line and the private payment list. This helper still writes a one-off reminder with [amount].

## v0.2.2 (October 20, 2026)
- The WhatsApp monthly-limit line is dated: "(as of October 2026; check WhatsApp's help pages)" (SKILL.md and example).
- Older changelog lines now describe the change only; no change to how the helper works.

## v0.2.1 (October 14, 2026)
Fixes from the live model run audit (runs/LIVE-RESULT.md).
- Shared rule: never invent durations or lead times either ("an hour", "arrive 10 minutes early").
- Shared rule: when pointing out a pasted private detail, name only its kind; never quote it.

## v0.2.0 (2026-10-14)
- Shared safety block: adds "photos of people" and the kit's stop rule (delete that chat, type it again with a [blank]).
Red-team fixes, October 14, 2026.
- Payment reminders to one customer are now in scope (from first-task-finder), with [amount] and [date], and no STOP line for those.
- "Fresh stock of" is now "New stock of" in the output template.
- Before you send: ask one-time buyers before sending offers; WhatsApp only, never bulk SMS or calls.
- Rules: added the pasted-content line and the delete-this-chat line. "Not for" names are bold.
- Blanks: [their name]. Removed the evals pointer from test prompt 3; SAFEGUARDS numbers now 98XXX XXXXX.
- SKILL-CARD.md renamed OWNER-CARD.md; full never-paste list and the stop-and-delete rule.
- LICENSE uses the shared bare template; RESULTS.md branding line made neutral.

## 0.1.1 (2026-10-14)
- "Not for" now points to the sales-funnel helpers.

## v0.1.0 (2026-10-14)
- First draft.
- Broadcasts, refill reminders and follow-ups for customers who agreed; 80 words or fewer; every message ends with [your business name] and a STOP opt-out line.
- Refuses bought or scraped lists, fake urgency and health promises.
- Pre-registered 3 evals; self-run results in evals/RESULTS.md in the GitHub repo.
