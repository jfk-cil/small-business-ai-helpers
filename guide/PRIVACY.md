# Privacy and safety rules

These rules apply to owners, to the people who help them at a table, and to anyone who changes this repo. The Skills, the phone pages and the package docs all repeat them.

## Never paste into any AI

- Guest or customer names and phone numbers (also email addresses)
- Passport scans, Form C (foreign-guest registration) details, Aadhaar or PAN numbers
- Bank, UPI or card details
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

Change people to "Customer 1", "Customer 2" before pasting. Where a detail is needed in the final message (a UPI ID, a name), the helper writes `[your UPI ID]` or `[blank]` and the owner types it in when they send.

**If something slips in:** stop, delete that chat, and type it again with a `[blank]`. The Skills are written to do the same: they name only the kind of detail ("a customer's phone number"), never repeat it, and ask the owner to delete the chat.

## What the page scans for

Before the phone page makes a helper, it scans the answers. It scans the "Try it here" box too. It looks for:

- a phone number (Indian mobile format, with or without +91)
- an email address
- a UPI ID
- an Aadhaar-like number (12 digits)
- a PAN-like number
- a card or account number (13 to 19 digits)
- a password or OTP written after a word like "password", "OTP" or "PIN"

If it finds one, it names the kind and won't make the helper until it is taken out.

**The scan is a safety net, not a guarantee.** It runs on patterns, so it misses things and sometimes flags things that are fine. It does not catch names, addresses, health details, passport or Form C details, photos, landline or foreign numbers, numbers written in words or in Devanagari digits, or details split across lines. It may flag a harmless 12-digit order number. The owner's own check, before pasting, is the real protection.

## Drafts only

Every helper drafts. The owner reads, checks and sends or publishes everything themselves. Nothing in this repo sends a WhatsApp message, posts, books, emails or charges anyone on its own. The Skills say so when asked. An automatic WhatsApp bot needs the WhatsApp Business Platform through an approved provider, each customer's opt-in and approved message templates; that is a separate builder project, not one of these helpers. Never set up unofficial apps that send messages from an owner's phone or ask them to scan a WhatsApp QR code in another app; they can get the number banned.

## At a table with an owner

- **No recording without a spoken notice and a yes.** Before taking notes, recording audio or taking a photo, say so out loud and ask. Go ahead only on a clear yes. A "no" ends it, with no follow-up.
- **No owner data in builders' own accounts.** The owner uses their own phone and their own AI account. Helpers never type an owner's facts, messages, customer lists or applicant details into their own Claude, ChatGPT, WhatsApp, email or notes, and never take screenshots of them. Demos use the made-up examples in each package's `BUILDER-NOTES.md`.
- **End clean.** Before leaving the table, look through the owner's AI chat together. If a name, number or ID got in, delete that chat together.

## Consent for stories

An owner's story (what they tried, what changed, a quote) is used only with their consent.

- Ask before writing anything about their business, and say where it will appear.
- Remove their name, their business's name and anything that identifies them. Describe the business by type and area only (for example, "a cleaning service in South Goa").
- Show them the text before it is shared. They can say no at any time, including later.
- Keep a short note of the consent: the date, what was agreed and where it will appear. Not their contact details in a public file.

The owner problems in [catalog/problems.md](../catalog/problems.md) are general examples written from what owners described. They were generalized so no business can be identified.

## "Help improve Claude"

Owners who prefer that their chats are not used to improve Claude's models can turn this off: in Claude, open **Settings**, then **Privacy**, and switch off **Help improve Claude**. It is the owner's choice; show them where it is and let them decide. It does not replace the never-paste list.

## Special care: health and hiring

Health and hiring involve the most sensitive data, and some owners work in both (for example, a home healthcare service bringing on nurses and attendants).

- **Patients never go into any AI**, not even a first name, a condition or an address. If patient details come up at the table, stop and start the example again without them.
- **Applicants and staff:** no names, numbers, CVs, photos, documents, certificates, police verification, registration numbers, ID numbers or individual wages in any AI. Form responses go in the owner's own spreadsheet and stay out of AI.
- **Fair hiring:** job posts and sign-up forms ask only what the job needs. No age, religion, caste, marital status or health questions.
- **No ranking of people.** The helpers never rank, score, screen out or discipline staff, applicants or customers. They sort messages by what the message asks, not by who sent it.
- **No clinical or medical advice.** Clinical steps (injections, collecting samples, moving a patient) come from a qualified person on the owner's team. No helper writes that a product, food, class or treatment cures, treats or prevents anything.
- **No legal or tax advice.** The helpers say "check with a qualified person."

## In this repo

- Test cases, examples and demos use fictional "Sample" businesses and the fake values listed in `scripts/check.py`. Never put a real owner's message, a business name or a row from owner notes into a prompt, a test bank or an example.
- `scripts/check.py` scans the repo for phone, Aadhaar, PAN, email and UPI-like values, and for names of private people or organizations (matched by hash, so the list itself is not published). A hit fails the check.
