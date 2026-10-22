# Small business AI helpers

Free, ready-to-use AI helpers for small businesses: replying to customers, bookings and reminders, follow-ups, getting paid on time, finding clients, a one-page shop, getting found on Google, posts and reels, a sales plan across channels, staff checklists, stock checks and returns, hiring, and making your own helper. Written with owners in Goa, India, and usable anywhere.

**On a phone? Open the helpers:** https://jfk-cil.github.io/small-business-ai-helpers/

Pick a job, answer a few short questions in English, Hindi, Marathi or Konkani, and copy your ready helper into Claude. It should also work in ChatGPT or Gemini if that's what you use (tested so far in Claude only). The page saves only your language choice and sends your answers nowhere. What you paste into an AI goes to that AI, so leave out names and numbers.

## The helpers

Each package solves a problem that owners named in their own words: 14 packages and 31 Skills. Most answer one or more of the owner problems C1 to C21; Start here, Get paid on time and Make your own helper serve needs that many owners share.

| Package | The problem | Phone page | Skills inside |
|---|---|---|---|
| [Start here](packages/start-here/) | "I'm not sure which job to hand to AI first." | [open](https://jfk-cil.github.io/small-business-ai-helpers/start-here/) | first-task-finder |
| [Reply to customer messages](packages/customer-replies/) | Dozens of messages a day on WhatsApp or booking apps, most asking the same things. | [open](https://jfk-cil.github.io/small-business-ai-helpers/customer-replies/) | message-sorter, guest-inquiry-replies, quote-and-proposal-writer, customer-messages-routine, listing-matcher |
| [Bookings and reminders](packages/booking-reminders/) | Customers book, then forget what to bring or don't turn up. | [open](https://jfk-cil.github.io/small-business-ai-helpers/booking-reminders/) | booking-confirmations, tracker-sheet-builder |
| [Follow-ups that get replies](packages/follow-ups/) | No time to follow up each call or unanswered message. | [open](https://jfk-cil.github.io/small-business-ai-helpers/follow-ups/) | follow-up-planner, lead-reply-and-follow-up, tracker-sheet-builder, customer-message-writer |
| [Get paid on time](packages/get-paid/) | People pay late, you forget who still owes you, and chasing feels awkward. | [open](https://jfk-cil.github.io/small-business-ai-helpers/get-paid/) | get-paid-routine, customer-message-writer, tracker-sheet-builder |
| [Find new clients](packages/find-clients/) | Not sure who to look for or how to reach out. | [open](https://jfk-cil.github.io/small-business-ai-helpers/find-clients/) | target-customer-finder, outreach-email-writer, lead-qualifier, client-onboarding-writer |
| [Your shop on one page](packages/one-page-shop/) | People find you online, but there's no single place to buy, book or ask. | [open](https://jfk-cil.github.io/small-business-ai-helpers/one-page-shop/) | storefront-page-builder, listing-and-catalog-writer, target-customer-finder |
| [Get found on Google](packages/get-found-on-google/) | People search for what you sell nearby, and you don't show up. | [open](https://jfk-cil.github.io/small-business-ai-helpers/get-found-on-google/) | google-profile-builder, listing-and-catalog-writer, review-replies |
| [Staff checklists](packages/staff-checklists/) | Things slip when you're not there. | [open](https://jfk-cil.github.io/small-business-ai-helpers/staff-checklists/) | sop-and-checklist-writer, tracker-sheet-builder, staff-checklist-routine |
| [Stock checks and returns](packages/stock-and-returns/) | Expired stock has to be found, returned and chased every month, and staff need hand-holding. | [open](https://jfk-cil.github.io/small-business-ai-helpers/stock-and-returns/) | stock-check-and-returns, sop-and-checklist-writer, tracker-sheet-builder |
| [Hire and welcome staff](packages/hire-and-onboard/) | Skilled people don't reach out, or stop halfway through signing up. | [open](https://jfk-cil.github.io/small-business-ai-helpers/hire-and-onboard/) | staff-hiring-and-onboarding, sop-and-checklist-writer |
| [Posts that bring customers](packages/social-posts/) | No time to post, and views that don't turn into customers. | [open](https://jfk-cil.github.io/small-business-ai-helpers/social-posts/) | social-content-planner, followers-to-customers, simple-marketing-plan, weekly-posts-routine, reel-script-writer |
| [A sales plan across channels](packages/sales-plan/) | Selling to cafés or shops, on WhatsApp and through posts, with no plan that ties them together. | [open](https://jfk-cil.github.io/small-business-ai-helpers/sales-plan/) | channel-sales-plan, social-content-planner, customer-message-writer, outreach-email-writer |
| [Make your own helper](packages/make-your-own/) | The ready helpers don't quite fit your job, or you want one in your own words. | [open](https://jfk-cil.github.io/small-business-ai-helpers/make-your-own/) | helper-builder, first-task-finder |

## Three ways to use them

**1. Phone, any plan (2 minutes).** Open the phone page, answer the questions, tap **Copy helper**, open Claude and paste. The helper is plain text, so it should also work in ChatGPT and Gemini (tested so far in Claude only), and you can keep using it after any free credits end. Save it in WhatsApp "Message yourself" to reuse it.

**2. Claude on a laptop (full version, 5 minutes).** Each package's page has a **Download** link for each Skill (also in [docs/downloads](docs/downloads/)). In Claude, open **Settings**, then **Capabilities**, then **Skills**, and upload the zip (as of October 2026). Skills need a paid Claude plan with code execution turned on (as of October 2026). Once uploaded, Claude uses the right Skill when you ask for that job.

**3. Claude Code or Cowork (one command).** Add this collection once, then install any package:

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install customer-replies@small-business-ai-helpers
```

In Cowork: **Customize**, then **Plugins**, then **Add marketplace**, and enter `jfk-cil/small-business-ai-helpers` (as of October 2026).

If you install several packages, shared Skills (like tracker-sheet-builder) come with each one. That's expected.

## Make your own, and other ways to use AI

The ready helpers are one way in. Often the best fix uses less AI, not more.

- [Make your own helper](guide/MAKE-YOUR-OWN.md): turn one weekly job into your own helper and test it with five messages.
- [Solution types](guide/SOLUTION-TYPES.md): seven levels, from tools you already have to automation. Use the lowest one that does the job.
- [Setups with no AI](guide/NO-AI-SETUPS.md): quick replies, labels, a form, a sheet and reminders that do most of the daily work.
- [Project recipes](guide/PROJECT-RECIPES.md): save a helper and your business facts as a Claude Project (paid plan).
- [Page recipes](guide/PAGE-RECIPES.md): small pages for staff that hold no customer data, with [example pages](examples/pages/).
- [Automation](guide/AUTOMATION.md): what automatic sending involves, and why a qualified person reviews it first.

## What these helpers will and won't do

- They draft. You check and send everything yourself. Nothing here sends a message, posts, or books anything on its own.
- They use only the facts you give and write `[blank]` where something is missing. They don't invent prices, dates, reviews or results.
- They never ask for, and tell you to remove: customers' names or phone numbers, Aadhaar, PAN or passport details, bank, UPI or card details, passwords or OTPs, health details.
- They don't give legal, tax or medical advice.
- They never rank or score staff or job applicants. The lead check only answers the fit questions you write.

## What these helpers don't do

Money records, invoices, GST, licenses, registrations, contracts, and labor or consumer law. These need your accountant, a lawyer or the official government portal for that rule. An AI draft from these helpers never replaces them. Get paid on time writes kind reminder words and an empty list layout; amounts, names and payment details stay with you.

## For builders and contributors

- [At the table](guide/AT-THE-TABLE.md): one screen for a volunteer sitting with an owner.
- [Coaching](guide/COACHING.md): helping an owner make, test and save a helper of their own.
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

## Who looks after this

- Maintained by volunteers, on a best-effort basis. Report a problem or suggest a change in [GitHub Issues](https://github.com/jfk-cil/small-business-ai-helpers/issues).
- No organization, program or government body endorses or reviews these helpers.
- Provided as is, with no warranty of any kind (see [LICENSE](LICENSE)).
- Releases are tagged. The pages change when the main branch changes, so fork the repo if you need to control your own copy (see [DEPLOY.md](guide/DEPLOY.md), path g).
- WhatsApp, Instagram, Facebook, Google, Claude, ChatGPT and Gemini are trademarks of their owners. This project is not affiliated with or endorsed by them.

## License

CC0 1.0: public domain. Copy, change and share it, even commercially, without asking. Translations are drafts; please have a fluent reader check them before relying on them.
