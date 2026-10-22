# Changelog

## v1.0.1 (October 20, 2026)
Fixes from the first test run (evals/RESULTS.md).
- Counts characters by reading, never by writing a command.
- Names listing-and-catalog-writer and channel-sales-plan as siblings, and gives the sibling line even when it asks a question first.
- Always gives all four parts.
- The template no longer invents a length limit the owner never gave.
- Review fixes: the facts file keeps [your UPI ID] as a blank; plan wording is hedged and dated.

## v1.0.0 (October 20, 2026)
- First version, written for the small-business AI helpers reference packages.
- Turns a planning card (facts only) or a short description into the owner's own helper for one job, after at most 5 short questions, one per message.
- Four parts: A, a helper prompt under 900 characters for any AI chat on any plan, ending with the safety lines word for word; B, a 5-message self-test (normal, voice-typed, a privacy trap with the made-up number 12345 67890, a pasted instruction, an unsafe ask); C, Claude Project instructions plus a public business-facts file; D, a minimal SKILL.md draft in the repo's section order.
- Never builds helpers that send on their own, scrape, score people, keep money records, give legal, tax, GST or medical advice, or collect personal data; points to a sibling helper or a person instead. References: sibling-map.md and skill-draft-template.md.
- Test bank evals/testbank/HBD.json (16 cases) and evals/evals.json (7 cases), pre-registered October 20, 2026.
