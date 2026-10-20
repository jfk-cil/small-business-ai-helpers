# Changelog

## v1.0.0 (October 19, 2026)
- Routing table points to the five new helpers: message-sorter, booking-confirmations, follow-up-planner, google-profile-builder, staff-hiring-and-onboarding.

## v0.2.1 (October 14, 2026)
Fixes from the live model run audit (runs/LIVE-RESULT.md).
- Shared rule: never invent durations or lead times either ("an hour", "arrive 10 minutes early").
- Shared rule: when pointing out a pasted private detail, name only its kind; never quote it.
- "One line" requests get one sentence of 30 words or fewer.

## v0.2.0 (2026-10-14)
- Shared safety block: adds "photos of people" and the kit's stop rule (delete that chat, type it again with a [blank]).
Red-team fixes, October 14, 2026.
- A payment-reminder message now routes to customer-message-writer, with [amount].
- Only bookkeeping, cash records, payroll, tax and staff judging stay "not for AI here, for now; the people helping you decide" (no more "keep it on paper").
- "Ask a builder at the session" is now "Ask the people running your session."
- Plain words instead of idioms ("takes most of your time each week", "Which job do you most want help with first?").
- Ties go to the start-with-3 helpers: guest-inquiry-replies, social-content-planner, tracker-sheet-builder.
- Rules: added the pasted-content line and the delete-this-chat line.
- SKILL-CARD.md renamed OWNER-CARD.md; full never-paste list and the stop-and-delete rule.

## 0.1.1 (2026-10-14)
- Routes to 14 helpers: adds target-customer-finder, lead-reply-and-follow-up, lead-qualifier and client-onboarding-writer (Wave 1.1, sales funnel).

## v0.1.0 (2026-10-14)
- First draft for a small-business AI series in Goa.
- Routes to one of 10 helpers, with a "not for AI here" list for money records, payroll, tax and staff judging.
- After self-test run 1: steps now handle refusals and pasted private details before asking questions, and re-ask "What else eats your week?" when the owner's main need is not one for AI.
