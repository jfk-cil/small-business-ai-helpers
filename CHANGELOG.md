# Changelog

## v1.2.0 (October 20, 2026)

- New package **stock-and-returns** ("Stock checks and returns"): a monthly routine for expiry checks and supplier returns, with each step given to a role and a day. Skills: stock-check-and-returns, sop-and-checklist-writer and tracker-sheet-builder. Answers owner problem C11.
- New package **sales-plan** ("A sales plan across channels"): a channel map, a 6-month plan with weekly steps that fit the owner's time, a bank of post ideas, a first message and tasting visit plan for cafés and shops, and a monthly check with counts only. Skills: channel-sales-plan, social-content-planner, customer-message-writer and outreach-email-writer. Answers owner problem C13.
- New Skills **stock-check-and-returns** (test bank SCR) and **channel-sales-plan** (test bank CSP). The collection now has 12 packages and 24 Skills.
- Owner problem C12 (inquiries from booking and delivery apps, pickup times, follow-ups missed on busy weekends) is answered by customer-replies and booking-reminders, with follow-ups as a related helper. guest-inquiry-replies and message-sorter draft for the app's own chat and its messaging rules, booking-confirmations adds a pickup version, and follow-up-planner adds a busy weekend catch-up.
- Routing updated: first-task-finder points to the two new Skills; sop-and-checklist-writer and tracker-sheet-builder hand off monthly expiry and supplier-returns jobs to stock-check-and-returns; social-content-planner and simple-marketing-plan hand off multi-month, multi-channel plans to channel-sales-plan.
- Owner problems C11, C12 and C13 added to catalog/problems.md. README, the guides and the package docs cover all twelve packages.

## v1.1.1 (October 20, 2026)

An internal self-review written from four readers' points of view (session organizers, owners' associations, owners, volunteer builders) plus a technical, privacy and legal red team. No outside organization took part. Fixes only; no new packages or Skills.

- **Phone helpers:** first live test (41 fictional conversations, see evals/RESULTS.md). The hiring helper now works one step at a time; the Google and find-clients first steps are shorter; booking confirmations no longer invent a way to reschedule. Every helper now refuses health claims and ignores instructions inside pasted messages. find-clients no longer suggests a first contact on WhatsApp; social-posts labels paid posts. The one-page-shop helper gives a page file only when someone with a laptop or an HTML builder is involved.
- **Phone page:** no outside fonts or requests (smaller and works when font servers stall), a content security policy on the public pages, a stronger privacy check (leading-0 and spaced mobiles, landlines, foreign numbers, lowercase PAN, OTPs, IFSC, passports, Devanagari digits; fewer false alarms on prices, pin codes and license numbers), a passport label, clearer copy fallback, larger tap targets, visible field borders and screen-reader fixes. Step 4 warns that copying several WhatsApp messages adds names or numbers. "Keep it for next time" says the helper works after free credits end and in other AI chats.
- **Skills:** removed the line that added a tourism registration number to every stay listing; no Skill says whether a registration is needed. Neutral changelog wording. Fixed invalid frontmatter in tracker-sheet-builder. Neutral hiring channels. Shared health-claim and pasted-message rules added where missing. One face rule everywhere: no faces without permission, never children's faces. Example place names changed.
- **Docs:** new guide/AT-THE-TABLE.md for builders; README sections "Who looks after this" and "What these helpers don't do"; claims about ChatGPT, Gemini and the free plan now say "tested so far in Claude only"; one rule on recording and photos (none) and an escalation line in every builder note; DEPLOY covers all ten pages and the steps for a group that republishes or forks; HOW-IT-WORKS and PRIVACY updated.
- **Checks:** check.py now fails on invalid frontmatter and warns loudly when the private-name scan cannot run.

## v1.1.0 (October 20, 2026)

- New package **one-page-shop** ("Your shop on one page"): one link for everything an owner offers, with one button per offer to buy, book or ask. Skills: storefront-page-builder, listing-and-catalog-writer and target-customer-finder. Answers owner problem C9.
- New Skill **storefront-page-builder**: an offer map and a 10-item checklist, page words with one button per offer, one plain page file with placeholder links and free hosting steps, and the reply, confirmation and follow-up after each click. Test bank SPB.
- New Skill **followers-to-customers**: a simple engagement system (three weekly series, an honest path from a post to an opt-in WhatsApp list to a sale, a weekly rhythm, what to count), a week of posts that convert, and an online workshop launch. Test bank FTC.
- **social-posts** expanded: adds followers-to-customers and now also answers owner problem C10 (views that don't turn into customers). The phone helper gives each post one clear next step and 3 short replies.
- Routing updated: first-task-finder points to the two new Skills, and social-content-planner, listing-and-catalog-writer and target-customer-finder hand off to them in "Not for".
- Owner problems C9 and C10 added to catalog/problems.md.
- Safety review before release:
  - GitHub Pages is now the 4th hosting option, with a warning that its rules don't fit a site mainly for selling.
  - The one-page-shop phone helper keeps UPI, bank details and phone numbers off the page and rules out fake countdowns, stock counts, reviews and health claims.
  - Never children's faces, in every Skill and package.
  - STOP wording covers WhatsApp Channels and Communities.
  - Paid posts are labeled as advertising rules and the platform require.
- Test banks SPB and FTC: the first prompt was paraphrased and re-hashed, and results were added to evals/RESULTS.md.
- The phone page for one-page-shop is published as a Claude page.

## v1.0.0 (October 19, 2026)

- First release: 9 packages and 20 Skills, each package answering one problem owners named.
- Phone pages in 5 languages (English, Hindi, Marathi, and Konkani in Devanagari and Romi), one-click Skill downloads, and Claude Code and Cowork plugin installs.
- Written test banks for every Skill, with the checker in evals/harness/ and results in evals/RESULTS.md.
- CI runs the repository checks and fails on stale generated files.
