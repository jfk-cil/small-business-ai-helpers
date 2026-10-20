# Privacy and safety rules

These rules apply to owners, to the people who help them at a table, and to anyone who changes this repo. The Skills, the phone pages and the package docs all repeat them.

## Never paste into any AI

- Guest or customer names and phone numbers (also email addresses)
- Passport scans, Form C (foreign-guest registration) details, Aadhaar or PAN numbers
- Bank, UPI or card details
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Sales, takings, expenses, loans or money owed (your public prices are fine)
- Family members' details
- Photos of people

Change people to "Customer 1", "Customer 2" before pasting. Where a detail is needed in the final message (a UPI ID, a name), the helper writes `[your UPI ID]` or `[blank]` and the owner types it in when they send.

**If something slips in:** stop, delete that chat, and type it again with a `[blank]`. The Skills are written to do the same: they name only the kind of detail ("a customer's phone number"), never repeat it, and ask the owner to delete the chat.

## What the page scans for

Before the phone page makes a helper, it scans the answers. It scans the "Try it here" box too. It looks for:

- a phone number: Indian mobiles (with +91, 91 or a leading 0, spaced or not), landlines like 0832 numbers, foreign numbers, and numbers spelled out in words
- an email address
- a UPI ID
- an Aadhaar-like number (12 digits)
- a PAN-like number (in capitals or small letters)
- a card number, a bank account number written after "account" or "A/c", or an IFSC code
- a passport number written near the word "passport" or "Form C"
- a password or OTP written after a word like "password", "OTP" or "PIN"

Devanagari digits are read as ordinary digits before the scan. If it finds one, it names the kind and won't make the helper until it is taken out.

**The scan is a safety net, not a guarantee.** It runs on patterns, so it misses things and sometimes flags things that are fine. It does not catch names, addresses, health details, other Form C details, photos, or details split across lines. It may flag a harmless long order or ticket number. The owner's own check, before pasting, is the real protection.

## Drafts only

Every helper drafts. The owner reads, checks and sends or publishes everything themselves. Nothing in this repo sends a WhatsApp message, posts, books, emails or charges anyone on its own. The Skills say so when asked. An automatic WhatsApp bot needs the WhatsApp Business Platform through an approved provider, each customer's opt-in and approved message templates; that is a separate builder project, not one of these helpers. Never set up unofficial apps that send messages from an owner's phone or ask them to scan a WhatsApp QR code in another app; they can get the number banned.

## At a table with an owner

One-screen version for builders: [AT-THE-TABLE.md](AT-THE-TABLE.md).

- **No recordings, photos or screenshots.** Do not record audio, video or screens, and do not photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers, and only after you ask out loud.
- **No owner data in builders' own accounts.** The owner uses their own phone and their own AI account. Builders and volunteers never type an owner's facts, messages, customer lists or applicant details into their own Claude, ChatGPT, WhatsApp, email or notes. Demos use the made-up examples in each package's `BUILDER-NOTES.md`.
- **No logins.** Do not log in to the owner's accounts, and never see or type their passwords or OTPs. They log in themselves.
- **When something goes wrong.** If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
- **End clean.** Before leaving the table, save the helper in "Message yourself". Look through the owner's AI chat together. If a name, number or ID got in, delete that chat together.

## Consent for stories

An owner's story (what they tried, what changed, a quote) is used only with their consent.

- Ask before writing anything about their business, and say where it will appear.
- Remove their name, their business's name and anything that identifies them. Describe the business by type and area only (for example, "a cleaning service in South Goa").
- Show them the text before it is shared. They can say no at any time, including later.
- Keep a short note of the consent: the date, what was agreed and where it will appear. Not their contact details in a public file.

The owner problems in [catalog/problems.md](../catalog/problems.md) are general examples written from what owners described. They were generalized so no business can be identified.

## "Help improve Claude" and other AIs

Owners who prefer that their chats are not used to improve Claude's models can turn this off: in Claude, open **Settings**, then **Privacy**, and switch off **Help improve Claude**. In ChatGPT or Gemini, open **Settings** and look for the data or activity control that lets chats train the model; switch it off if you prefer. Menus change. It is the owner's choice; show them where it is and let them decide. It does not replace the never-paste list.

## Special care: health and hiring

Health and hiring involve the most sensitive data, and some owners work in both (for example, a home healthcare service bringing on nurses and attendants).

- **Patients never go into any AI**, not even a first name, a condition or an address. If patient details come up at the table, stop and start the example again without them.
- **Applicants and staff:** no names, numbers, CVs, photos, documents, certificates, police verification, registration numbers, ID numbers or individual wages in any AI. Form responses go in the owner's own spreadsheet and stay out of AI.
- **Fair hiring:** job posts and sign-up forms ask only what the job needs. No age, religion, caste, marital status or health questions.
- **No ranking of people.** The helpers never rank, score, screen out or discipline staff or applicants. They sort messages by what the message asks, not by who sent it. The lead check only answers the fit questions the owner writes.
- **No clinical or medical advice.** Clinical steps (injections, collecting samples, moving a patient) come from a qualified person on the owner's team. No helper writes that a product, food, class or treatment cures, treats or prevents anything.
- **No legal or tax advice.** The helpers say "check with a qualified person."

## In this repo

- Test cases, examples and demos use fictional "Sample" businesses and the fake values listed in `scripts/check.py`. Never put a real owner's message, a business name or a row from owner notes into a prompt, a test bank or an example.
- `scripts/check.py` scans the repo for phone, Aadhaar, PAN, email and UPI-like values. A hit fails the check.
- It also scans for names of private people, organizations, programs and events, read from a local plain-text list that the maintainer keeps and never commits. Without that file, `check.py` prints a warning and skips this scan, so it does not run in CI or for contributors. The maintainer runs it before every release.
