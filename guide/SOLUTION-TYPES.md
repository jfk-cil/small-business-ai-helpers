# Solution types: from no AI to automation

For builders and curious owners. Seven levels, from tools an owner already has to systems that act on their own. Each level up costs more to set up, more to keep up, and moves more data around. **Use the lowest level that does the job.**

Plans, prices and menu names below are as of October 2026. They change often. Check current plans before anyone pays.

## Pick a level

| The job | Level | Guide |
|---|---|---|
| The same answers, reminders or lists, over and over | 0. No-AI tools | [NO-AI-SETUPS.md](NO-AI-SETUPS.md) |
| New wording each time: replies, posts, checklists, quotes | 1. Phone helper | the [phone pages](https://jfk-cil.github.io/small-business-ai-helpers/), [MAKE-YOUR-OWN.md](MAKE-YOUR-OWN.md) |
| One helper used daily, with facts that rarely change | 2. Claude Project | [PROJECT-RECIPES.md](PROJECT-RECIPES.md) |
| Several jobs, longer rules, on a laptop | 3. Skill or plugin | [README.md](../README.md), [DEPLOY.md](DEPLOY.md) |
| Staff tick a list, or the owner adds up a quote | 4. Small Claude page | [PAGE-RECIPES.md](PAGE-RECIPES.md) |
| Claude needs to read the owner's own sheet or calendar | 5. Connectors | this page only |
| Messages or records that should move without a person | 6. Automation | [AUTOMATION.md](AUTOMATION.md) (no recipes) |

If two levels fit, pick the lower one. Levels 0 and 1 together cover most owners.

## Level 0: no-AI tools

**What it is.** Features the owner already has: WhatsApp Business quick replies, labels, greeting and away messages, a Google Form, a Google Sheet, phone calendar reminders, a Google Business Profile. AI only helps write the words once.

**Who it suits.** Everyone, first. Especially owners who answer the same questions all day or forget follow-ups.

**Plan or cost.** Free.

**Data and privacy.** Customer data stays in the owner's own apps. Nothing goes to an AI unless the owner pastes it.

**Effort.** 15 to 30 minutes to set up. A few minutes a week to keep answers current.

**Examples here.** The "Set up once" steps in each package's `PLAYBOOK.md`; the [customer messages](../skills/customer-messages-routine/), [weekly posts](../skills/weekly-posts-routine/), [staff checklists](../skills/staff-checklist-routine/) and [get paid on time](../skills/get-paid-routine/) routines.

**When not to use it.** When each answer really is different (a custom quote, a post) and typing it from scratch takes too long. Then add level 1.

## Level 1: phone helper

**What it is.** A short plain-text instruction the owner pastes into a new AI chat, then pastes the job. Made on a phone page in two minutes, or written by hand.

**Who it suits.** Owners on any phone and any plan, including free plans of Claude, ChatGPT or Gemini (tested so far in Claude only).

**Plan or cost.** Free plans work, with message limits. If the limit is reached, the same helper works in another AI.

**Data and privacy.** Whatever is pasted goes to that AI company and follows its rules. The never-type list ([PRIVACY.md](PRIVACY.md)) is the protection. The phone pages themselves send nothing anywhere.

**Effort.** 2 to 20 minutes to make. Remake it when prices or hours change.

**Examples here.** Every package's phone page, the [make-your-own page](https://jfk-cil.github.io/small-business-ai-helpers/make-your-own/) and the [get-paid page](https://jfk-cil.github.io/small-business-ai-helpers/get-paid/).

**When not to use it.** When the owner would have to paste customer details to get any use from it. Fix the job first (use Customer 1 and [blank]) or stay at level 0.

## Level 2: Claude Project

**What it is.** A Claude workspace with saved instructions (the helper) and files (the owner's public business facts). Every chat inside it starts with both.

**Who it suits.** An owner who uses the same helper every day and is tired of pasting it.

**Plan or cost.** A paid Claude plan (check current plans). The paid individual plan was about US$20 a month in the US; prices differ by country.

**Data and privacy.** The instructions and files are stored in the owner's Claude account until they delete them. Only public facts go in the files. Chats inside the Project follow the same never-type list.

**Effort.** 10 minutes to set up. Update the facts file when anything changes.

**Examples here.** [PROJECT-RECIPES.md](PROJECT-RECIPES.md) turns any phone helper into a Project.

**When not to use it.** On a free plan. When the owner works only from a phone and pasting is quick. When several people share one login (never share logins).

## Level 3: Skill or plugin

**What it is.** A folder of instructions, references and examples that Claude loads by itself when the job comes up. Uploaded as a zip on claude.ai, or installed as a plugin in Claude Code or Cowork.

**Who it suits.** Owners or builders with a laptop who use several helpers and want the fuller rules: refusals, output formats, references.

**Plan or cost.** A paid Claude plan with code execution on, for claude.ai upload. Claude Code and Cowork need a plan that includes them.

**Data and privacy.** The Skill holds no customer data. Its rules repeat the never-type list. Chats follow the same rules as level 1.

**Effort.** 5 minutes per Skill to install. Reinstall to update. Writing a new Skill well takes hours, with tests first ([CONTRIBUTING.md](../CONTRIBUTING.md)). The [helper-builder Skill](../skills/helper-builder/) drafts an owner's own Skill from their helper.

**Examples here.** The Skills in `skills/` and the [downloads](../docs/downloads/). Whether uploaded Skills work in the Claude phone app is not documented; test first.

**When not to use it.** Phone-only owners. Owners who use one helper once a week. Anywhere a level 1 helper already does the job.

## Level 4: small Claude pages people use

**What it is.** A small web page Claude makes on request (an "artifact"), shared by link: a staff checklist with tick boxes, a quote worksheet, a today's jobs board.

**Who it suits.** Owners with staff who need the same list every day, or owners who add up quotes often.

**Plan or cost.** Making and sharing pages worked on free and paid Claude plans (check current plans).

**Data and privacy.** The pages hold no customer data: no names, numbers or payment details. Any saved state (ticks) lives only on each viewer's own phone, so the owner never sees who ticked what. The phone pages in this collection can also be published as Claude pages ([DEPLOY.md](DEPLOY.md), path b).

**Effort.** 10 to 20 minutes with a copy-paste prompt. Ask Claude to change it when the list changes, then check the shared link shows the new version.

**Examples here.** [PAGE-RECIPES.md](PAGE-RECIPES.md) and the example pages in [examples/pages/](../examples/pages/).

**When not to use it.** As a record of who did the work (it isn't one, and should never be used to watch staff). For anything that must be shared between phones in real time. For bookings or payments.

## Level 5: connectors to the owner's own Google Sheet, Calendar or Gmail

**What it is.** Claude, in the owner's own account, connected to the owner's own Google account so it can read (and, for some connectors, create drafts or events) without copy and paste.

**Who it suits.** A few owners with a paid plan, a laptop, and data already organized with no customer names in it: for example a jobs sheet with job types, times and areas only.

**Plan or cost.** Connectors were on paid Claude plans (check current plans). Google's free tools are fine.

**Data and privacy.** This is the big change. Claude reads whatever the connection reaches, not just what the owner chooses to paste. A Gmail inbox or a calendar full of customer names sends those names to the AI. So:

- Connect only from the owner's own account, and only to files and calendars that hold no names, numbers, payment details or health details.
- **Gmail: not recommended** for customer mail, because it brings names and addresses into the AI.
- Every draft or event Claude makes is reviewed by the owner before it is sent or kept.
- The owner can disconnect at any time from Claude's settings and from the Google account's security page.

**Effort.** 15 minutes to connect, plus real care to keep the data clean. Someone must check every few weeks that no names crept into the sheet.

**Examples here.** None. The [tracker-sheet-builder Skill](../skills/tracker-sheet-builder/) designs a sheet the owner builds and fills by hand.

**When not to use it.** When the data has customer names (almost always true for inboxes). When the owner isn't confident turning it off. When copy and paste of a cleaned list works fine.

## Level 6: automation

**What it is.** Systems that send messages, move data or react to events without a person in the loop each time: the WhatsApp Business Platform through a provider, workflow tools, email or calendar rules.

**Who it suits.** Businesses with high, steady volume and someone qualified to set it up and keep it running.

**Plan or cost.** Provider and per-message fees, hosting, and ongoing paid time. Rarely small.

**Data and privacy.** Customer data leaves the phone and passes through other services. Consent and notice duties may apply (in India, the Digital Personal Data Protection Act, 2023, with phased start dates); check with a qualified person. Numbers can be banned.

**Effort.** Weeks to set up, and ongoing care.

**Examples here.** None, on purpose. [AUTOMATION.md](AUTOMATION.md) explains what is involved. This repo gives no automation recipes.

**When not to use it.** Before levels 0 and 1 are working by hand. Without a qualified person who has reviewed the setup. Never with unofficial apps that read WhatsApp or ask for a QR scan.

## Honest limits

- Every level drafts. People check and send.
- Higher levels don't make the AI more accurate. Better facts and tests do.
- No level replaces an accountant, a lawyer or the official portal for money records, tax, GST, licenses or contracts.

Free to use and adapt (CC0).
