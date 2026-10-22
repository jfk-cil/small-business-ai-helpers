# Changelog

## v0.2.6 (October 21, 2026)
- "Not for" points to listing-matcher for matching several listings to one client and writing the shortlist. No new test cases yet.

## v0.2.5 (October 20, 2026)
- Registration and license numbers: included exactly if the owner gives one; never added, asked about or judged as needed. If a site asks and the owner has none to give, write [number, if the site asks] and say "Check with a qualified person what applies." The Goa stay listing no longer gets a registration line by default (SKILL.md and owner card).

## v0.2.4 (October 20, 2026)
- Description says "About or product pages" instead of "website pages", so it no longer overlaps with storefront-page-builder.

## v0.2.3 (October 20, 2026)
- "Not for" hands off a one-page shop or link page that brings all offers together to storefront-page-builder. The description gains one matching "Not for" clause.

## v0.2.2 (October 19, 2026)
- The Google Business Profile description job moved to google-profile-builder: removed from the description, "Use it when", formats, example, test prompt, owner card and safeguards, and eval 1 deleted from evals/evals.json. "Not for" points Google profile descriptions and Google posts to google-profile-builder.
- The example is now a website home page.

## v0.2.1 (October 14, 2026)
Fixes from the live model run audit (runs/LIVE-RESULT.md).
- Shared rule: never invent durations or lead times either ("an hour", "arrive 10 minutes early").
- Shared rule: when pointing out a pasted private detail, name only its kind; never quote it.

## v0.2.0 (2026-10-14)
- Food words with legal meaning only if the owner says them, plus an FSSAI check blank.
- Shared safety block: adds "photos of people" and the kit's stop rule (delete that chat, type it again with a [blank]).
Red-team fixes, October 14, 2026.
- Booking-site listings: Airbnb limits are 50 characters (title) and 500 characters (description), not 500 words; show the count.
- Goa stay listings get a "Goa Tourism registration no.: [registration number]" line to fill in.
- Rules: added the pasted-content line, the health-claims line, the registration-number line and the delete-this-chat line; "organic" now needs a named certificate like "certified".
- Blanks: [price]. "Not for" no longer says "a builder".
- SKILL-CARD.md renamed OWNER-CARD.md; full never-paste list and the stop-and-delete rule.
- LICENSE uses the shared bare template; RESULTS.md branding line made neutral.

## v0.1.0 (2026-10-14)
- First draft. Rewrites menus, product and catalog text, Google Business descriptions and website page text.
- Three test cases written and fingerprinted before the instructions (see `evals/RESULTS.md` in the GitHub repo).
- One round of fixes after self-run tests; see `evals/RESULTS.md` in the GitHub repo for what changed.
- Status: draft. Not yet tried with a real owner.
