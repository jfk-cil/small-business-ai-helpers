# Changelog

## v1.0.1 (October 20, 2026)
Fixes from the first test run (evals/RESULTS.md).
- The paper version has its own list columns and stays within 600 characters when references/ is not loaded.
- Keeps [location link] even when the owner sends a map pin.
- A message to many past customers goes to customer-message-writer.
- Review fixes: the quick-reply example no longer carries fixed facts; the menu note is dated.

## v1.0.0 (October 20, 2026)
- First version, written for the small-business AI helpers reference packages.
- Tool-first routine for WhatsApp questions and inquiries. Setup mode: 3 quick replies with shortcuts plus a follow-up reply, an away message, 5 labels (New, Replied, Follow up, Booked, Not now), a routine card, a "my helper" prompt under 600 characters for "Message yourself", and a 3-line plan for the week. Weekly mode: one new quick reply for a question asked 3 or more times, and fixes to out-of-date replies.
- Follow-up rule: only people who messaged first, at most 2 follow-ups (day 2 and day 7), then Not now; stop on no. A paper version for normal WhatsApp.
- Accepts a pasted planning card as facts only; its "Keep out of any AI" items join the never-include list.
- References: whatsapp-setup.md, routine-card.md (long owner card and paper card) and conversation-starter.md. Test bank evals/testbank/CMR.json (16 cases) and evals/evals.json (6 cases), pre-registered October 20, 2026.
