# Automation: what it involves

For builders. **This repo gives no automation recipes.** This page explains what each kind of automation can do, what it needs and what can go wrong, so a builder can be honest with an owner who asks "Can't it just reply for me?"

Every helper in this repo drafts. The owner checks and sends. That stays true here.

## The rule

**No automatic sending to customers before a qualified person has reviewed the setup.**

A qualified person has set up this kind of system before, has read the current terms of the platform and any provider, understands the data-protection duties that apply, and will be around to fix it when it breaks. A volunteer at a table is usually not that person, and a table session is never the place to start. If an owner asks for automation, write down what they need in plain words, build the manual version (quick replies, labels, reminders: [NO-AI-SETUPS.md](NO-AI-SETUPS.md)), and tell the person running your session.

Never set up unofficial apps that read phone notifications, send WhatsApp messages from the owner's phone, or ask the owner to scan a WhatsApp QR code in another app. They break WhatsApp's terms, can get the number banned, and expose customers' messages.

Details below are as of October 2026. Platforms change their rules and prices often; check the current terms before any project.

## 1. Meta's own business AI in the WhatsApp Business app

**What it can do.** In some countries and languages, the WhatsApp Business app offers an AI from Meta that can suggest or send answers to customers' questions, using the business's profile, catalog and other information the owner gives it. Where and how it works depends on the market and the app version.

**What it needs.** The owner switches it on in their own app and accepts Meta's terms. Good, current business information for it to draw on.

**Risks.**
- It is Meta's AI, not this repo's helpers. None of this repo's rules or tests apply to it.
- It can answer wrongly: a price, a slot, availability, a promise the owner never made. Customers will hold the owner to it.
- Customers' messages are handled under Meta's terms. Check what it reads and what customers are told.
- Customers may not realize they are talking to an AI.

**Before anything is switched on:** read what it will say, in what situations, with the owner. Prefer a mode where it suggests and the owner sends, if the app offers one. Test with made-up messages. Decide which messages must always come to the owner.

## 2. The WhatsApp Business Platform through an approved provider

**What it can do.** A real automated WhatsApp setup: replies from a system, booking confirmations and reminders, handing a chat to a person. Usually through an approved provider (a company Meta approves to connect businesses), or directly through Meta's own platform.

**What it needs.**
- The owner's own business account with Meta, often with business verification and an approved display name.
- A phone number registered on the Platform. Moving a number can change how it works in the phone app; some setups allow both, some don't. Check before moving the owner's main number.
- **Opt-in:** each customer agrees to get messages from the business on WhatsApp, and the business keeps a record of it.
- **Approved templates:** messages the business starts (reminders, confirmations, offers) must use message templates that Meta approves first. Free-form replies are generally allowed only for a limited time after the customer last wrote.
- **Per-message costs:** Meta charges per template message, by category (for example marketing, utility, authentication) and by country, plus the provider's own fees.
- A person who takes over anything the system shouldn't answer, and who watches it every day.
- Meta's policies limit what AI can do on the Platform (for example, general-purpose chatbots that aren't about the business's own service). Check the current policy.

**Risks.**
- **Quality ratings and bans.** When customers block or report a business's messages, its quality rating drops. Templates can be paused, sending limits cut, and the number restricted or banned. Marketing messages to people who didn't really opt in are the usual cause.
- **Data leaving the phone.** Customer messages and numbers pass through the provider's systems and any AI connected to them.
- **Cost surprises.** A loop or a bulk send can run up charges quickly.
- **Lock-in.** Leaving a provider can be hard. Agree in writing who controls the account and the number. It should always be the owner.

## 3. Workflow tools (apps that connect other apps)

**What it can do.** Connect apps so that one event triggers another: a new form answer adds a sheet row, sends the owner an email, or creates a calendar entry. Some workflows add an AI step.

**What it needs.** An account on a hosted service, or a server to run it (self-hosting needs real technical care: updates, backups, security). Credentials (passwords, keys or app permissions) for every app it connects. Someone to maintain it.

**Risks.**
- **Data leaving the phone and the owner's apps.** Everything in the workflow passes through the tool. An AI step sends that data to an AI company, often with customer names in it, which breaks the never-type list in [PRIVACY.md](PRIVACY.md).
- **Credentials.** The tool holds keys to the owner's accounts. A leak exposes everything it connects.
- **Silent failures.** A workflow can stop working and nobody notices, or run twice and send twice.
- **Sending to customers** from a workflow falls under every rule in this page.

## 4. Email and calendar automations

**What it can do.** Simple, built-in automations: an email auto-reply when the owner is away, email filters and labels, saved reply templates, calendar reminders, and booking pages where customers pick a free slot.

**What it needs.** The owner's own Google (or other) account, set up by the owner. Most of these are free and are the safest kind of automation, because they stay inside the owner's account.

**Risks.**
- An auto-reply answers everyone, including spam, and can confirm the address is active. Keep it short, with no promises.
- Booking pages show when the owner is free, and confirmation emails can contain wrong facts. Test with made-up bookings first.
- Calendar invitations send customers' email addresses to each other if added to one event. Never put several customers on one invitation.
- Reminders to the owner are fine. Automatic messages to customers follow the rule at the top of this page.

## Risks that apply to all of them

- **Bans.** Platforms can restrict or ban a number or account that sends unwanted messages, and getting it back is slow or impossible. The owner's main number is often their whole business.
- **Data leaving the phone.** Every automation copies customer data into another system. Know where it goes, who can see it, and how to delete it.
- **Notice and consent under India's Digital Personal Data Protection Act, 2023.** A business that collects and uses customers' personal data digitally will generally need to tell people what it collects and why, get clear consent where consent is the basis, let them withdraw consent as easily as they gave it, protect the data and delete it when it is no longer needed. Rules under the Act have phased start dates. This is not legal advice: a qualified person must check what applies to the owner's setup, and when.
- **Impersonation.** An automated system must not pretend to be the owner or a person. Tell customers when they are talking to an automated assistant. Scammers also copy businesses' names and profiles; a verified, well-kept official account helps customers tell them apart.
- **Who answers when it breaks.** Every setup needs a named person (by role, in the owner's own records) who checks it daily and can switch it off.

## What a reviewer should see before anything sends

Not a recipe; a list of what the qualified person checks:

- Where each customer's opt-in is recorded, and how they opt out.
- Every message a customer could receive, word for word, with no invented prices or promises.
- What goes to a person, and how fast a person answers.
- A map of where customer data goes, who can see it, and when it is deleted.
- The notice customers see, and whether consent is needed.
- What it costs per month at the owner's real volume.
- How to switch it off in one step, and who does that.
- A test with made-up customers only, before any real customer is included.

Free to use and adapt (CC0).
