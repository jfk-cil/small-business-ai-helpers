# Small business AI helpers

Free, ready-to-use AI helpers for small businesses: replying to customers, bookings and reminders, follow-ups, finding clients, a one-page shop, getting found on Google, posts, staff checklists and hiring. Written with owners in Goa, India, and usable anywhere.

**On a phone? Open the helpers:** https://jfk-cil.github.io/small-business-ai-helpers/

Pick a job, answer a few short questions in English, Hindi, Marathi or Konkani, and copy your ready helper into Claude, or into ChatGPT or Gemini if that's what you use. The page saves only your language choice and sends your answers nowhere. What you paste into an AI goes to that AI, so leave out names and numbers.

## The helpers

Each package solves one problem that owners named in their own words.

| Package | The problem | Phone page | Skills inside |
|---|---|---|---|
| [Start here](packages/start-here/) | "I'm not sure which job to hand to AI first." | [open](https://jfk-cil.github.io/small-business-ai-helpers/start-here/) | first-task-finder |
| [Reply to customer messages](packages/customer-replies/) | Dozens of WhatsApp messages a day, most asking the same things. | [open](https://jfk-cil.github.io/small-business-ai-helpers/customer-replies/) | message-sorter, guest-inquiry-replies, quote-and-proposal-writer |
| [Bookings and reminders](packages/booking-reminders/) | Customers book, then forget what to bring or don't turn up. | [open](https://jfk-cil.github.io/small-business-ai-helpers/booking-reminders/) | booking-confirmations, tracker-sheet-builder |
| [Follow-ups that get replies](packages/follow-ups/) | No time to follow up each call or unanswered message. | [open](https://jfk-cil.github.io/small-business-ai-helpers/follow-ups/) | follow-up-planner, lead-reply-and-follow-up, tracker-sheet-builder, customer-message-writer |
| [Find new clients](packages/find-clients/) | Not sure who to look for or how to reach out. | [open](https://jfk-cil.github.io/small-business-ai-helpers/find-clients/) | target-customer-finder, outreach-email-writer, lead-qualifier, client-onboarding-writer |
| [Your shop on one page](packages/one-page-shop/) | People find you online, but there's no single place to buy, book or ask. | [open](https://jfk-cil.github.io/small-business-ai-helpers/one-page-shop/) | storefront-page-builder, listing-and-catalog-writer, target-customer-finder |
| [Get found on Google](packages/get-found-on-google/) | People search for what you sell nearby, and you don't show up. | [open](https://jfk-cil.github.io/small-business-ai-helpers/get-found-on-google/) | google-profile-builder, listing-and-catalog-writer, review-replies |
| [Staff checklists](packages/staff-checklists/) | Things slip when you're not there. | [open](https://jfk-cil.github.io/small-business-ai-helpers/staff-checklists/) | sop-and-checklist-writer, tracker-sheet-builder |
| [Hire and welcome staff](packages/hire-and-onboard/) | Skilled people don't reach out, or stop halfway through signing up. | [open](https://jfk-cil.github.io/small-business-ai-helpers/hire-and-onboard/) | staff-hiring-and-onboarding, sop-and-checklist-writer |
| [Posts that bring customers](packages/social-posts/) | No time to post, and views that don't turn into customers. | [open](https://jfk-cil.github.io/small-business-ai-helpers/social-posts/) | social-content-planner, followers-to-customers, simple-marketing-plan |

## Three ways to use them

**1. Phone, any plan, any AI (2 minutes).** Open the phone page, answer the questions, tap **Copy helper**, open Claude and paste. The helper is plain text, so it also works in ChatGPT and Gemini, and it keeps working after any free credits end. Save it in WhatsApp "Message yourself" to reuse it.

**2. Claude on a laptop (full version, 5 minutes).** Each package's page has a **Download** link for each Skill (also in [docs/downloads](docs/downloads/)). In Claude, open **Settings**, then **Capabilities**, then **Skills**, and upload the zip (as of October 2026). Skills need a paid Claude plan with code execution turned on (as of October 2026). Once uploaded, Claude uses the right Skill when you ask for that job.

**3. Claude Code or Cowork (one command).** Add this collection once, then install any package:

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install customer-replies@small-business-ai-helpers
```

In Cowork: **Customize**, then **Plugins**, then **Add marketplace**, and enter `jfk-cil/small-business-ai-helpers`.

If you install several packages, shared Skills (like tracker-sheet-builder) come with each one. That's expected.

## What these helpers will and won't do

- They draft. You check and send everything yourself. Nothing here sends a message, posts, or books anything on its own.
- They use only the facts you give and write `[blank]` where something is missing. They don't invent prices, dates, reviews or results.
- They never ask for, and tell you to remove: customers' names or phone numbers, Aadhaar, PAN or passport details, bank, UPI or card details, passwords or OTPs, health details.
- They don't give legal, tax or medical advice, and they never rank or score people.

## For builders and contributors

- [How it works](guide/HOW-IT-WORKS.md): sources, what is generated, and why.
- [Deploying and publishing](guide/DEPLOY.md): GitHub Pages, Claude pages, Skill uploads, plugin installs.
- [Privacy and safety rules](guide/PRIVACY.md).
- [Contributing](CONTRIBUTING.md): add or change a Skill, run the checks and tests.
- [Test results](evals/RESULTS.md) and the [owner problems](catalog/problems.md) each package answers.
- [Changelog](CHANGELOG.md): what changed in each release.

```
python3 scripts/build.py          # regenerate packages, pages and downloads
python3 scripts/check.py          # lint everything (also runs in CI)
python3 scripts/build.py --check  # fail if generated files are stale
```

## License

CC0 1.0: public domain. Copy, change and share it, even commercially, without asking. Translations are drafts; please have a fluent reader check them before relying on them.
