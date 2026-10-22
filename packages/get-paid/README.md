# Get paid on time

Friendly payment reminders and a simple private list, so deposits and balances come in on time. Amounts, names and payment details stay out of the AI.

## The problem

Many small businesses are paid by an advance or after the job: homestays, cake orders, cleaners, repair services, studios. Some customers pay late. Some forget. The owner forgets too, because the list of who still owes lives in their head or in old chats. Chasing feels awkward, so it waits, and the money comes in weeks late or not at all. What the owner wants is a kind, simple way to remind people, a list they trust, and one short weekly habit.

This package has no numbered owner problem. It serves the money and paperwork need that many owners named, kept to the part a helper can do safely: the words and the routine, never the records.

## What you get

The phone helper works in four steps, one per message, and asks before moving on:

1. **Two reminder texts** to save as WhatsApp quick replies: /pay1 (friendly) and /pay2 (final and polite), with the blanks [amount] [job] [due date] [your UPI ID]. You fill them in on your phone, only when you send.
2. **A deposit line** for your booking confirmations, with [amount] and [due date] as blanks.
3. **Columns for a private list** on paper or a sheet shared with no one: Date, Job (the work, never the customer's name), Due date, Paid?
4. **A 10-minute weekly check:** who gets /pay1, who gets /pay2 a week later, and when to call or talk in person instead.

The full version (Skills) also:
- adds a "Payment due" label for WhatsApp Business, a routine card and a short "my helper" prompt to save in "Message yourself";
- gives a paper version for normal WhatsApp, with the reminders kept in your pinned "Message yourself" chat;
- runs your weekly check by step only (send /pay1, send /pay2, call, tick Paid), with no amounts or names;
- writes a short, kind reply when a customer answers a reminder (already paid, needs more time, a problem with the job);
- builds your list as a Google Sheet in your own account, shared with no one, with a color rule for what is due this week.

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/get-paid/
2. Answer 4 short questions: what kind of business it is; how people pay you; how you like to sound; where you remind people. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Type "go" to start with your reminder texts.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [get-paid-routine.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/get-paid-routine.zip)
   - [customer-message-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/customer-message-writer.zip)
   - [tracker-sheet-builder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/tracker-sheet-builder.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "Customers pay late. Set up my get-paid routine." Then say how people pay you, with no amounts or names.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install get-paid@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **get-paid** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [get-paid-routine](../../skills/get-paid-routine/SKILL.md) | Sets up a kind, tool-first routine: empty list columns, a Payment due label, /pay1 and /pay2 quick replies with blanks, a deposit line, a weekly 10-minute check, then a call or a talk in person. Also writes kind replies when a customer answers a reminder. | "Customers pay late." "I forget who owes me." "A deposit line for my booking message." "It's my weekly payment check." |
| [customer-message-writer](../../skills/customer-message-writer/SKILL.md) | Writes short WhatsApp messages for customers who agreed to hear from you: a one-off reminder, a reorder reminder or a thank-you. Amounts stay as [amount]. | "Remind a client their payment is due." "A thank-you after they paid." |
| [tracker-sheet-builder](../../skills/tracker-sheet-builder/SKILL.md) | Designs one simple Google Sheet with sample rows, formulas, color rules and 5 phone setup steps. Here: your payment list, with no amounts or names. | "Make my payment list a sheet." "Show me what's due this week." |

Owner cards (one page each, plain words): [get-paid-routine](../../skills/get-paid-routine/OWNER-CARD.md), [customer-message-writer](../../skills/customer-message-writer/OWNER-CARD.md), [tracker-sheet-builder](../../skills/tracker-sheet-builder/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **Drafts only.** You fill in every blank and send every reminder yourself. It can't send messages, check whether someone paid, or set reminders. One weekly phone alarm does that job.
- **Blanks stay blank.** [amount], [job], [due date] and [your UPI ID] stay as written in every draft and language. You fill them in on your phone, just before sending.
- **No money records in the AI.** It never handles a real amount tied to a person, a customer's name, a UPI ID, bank details, a GST number, an invoice or a payment screenshot. It never lists who owes, checks a payment or adds anything up. Your public prices and your general deposit rule ("50% advance") are fine.
- **Kind and private.** No late fees, interest, penalties, threats, "legal action" or recovery agents. No group, Status or public posts about who owes, and no messages to anyone else about it. One person, one private chat, never a broadcast.
- **Your terms.** It never suggests a deposit size, a due date, or a refund or cancellation term. Anything you didn't give stays [blank].
- **No legal, tax or collection advice.** After /pay2, the next step is a call or a talk in person. Invoices, GST, accounting, a dispute or getting money back by law: check with your accountant or a qualified person.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Customers' names and phone numbers (the list says the job, not the name)
- Amounts someone owes you, invoices, GST numbers or payment screenshots
- Bank, UPI and card details (the drafts use [your UPI ID])
- Passport, Form C, Aadhaar or PAN details
- Passwords and OTPs, including your UPI or banking app PIN
- Sales or money figures (your public prices are fine)
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

Your real list stays on paper or in a sheet shared with no one. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([GPR.json](../../evals/testbank/GPR.json), [CMW.json](../../evals/testbank/CMW.json), [TSB.json](../../evals/testbank/TSB.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you fill in the blanks and send everything yourself.
