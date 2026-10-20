# Reply to customer messages

AI drafts the routine replies in your tone for you to check and send. You write only the ones that need you.

## The problem

Service businesses that sell over WhatsApp, such as a real estate agent or a home cleaning service, get dozens of customer messages a day. Most ask the same things: the price, the area, the timings, how to book. Giving each one a proper answer can take hours every day, and leaves little energy for new business. What these owners want is simple: the routine replies go out in their own tone, and they are brought in only for the messages that really need them.

## What you get

- **Needs you:** the few messages only you should answer (complaints, discounts, money disputes, site visits, bookings to confirm, anything unusual or emotional), each with one calm line you can send right away.
- **Ready to send:** a short reply for every routine message, in your tone, using only your facts. Each reply is in its own copy box.
- **Quick replies:** when the same question comes twice, a WhatsApp quick reply with a short shortcut word.
- A count at the end: how many messages, how many need you.

The full version (Skills) also:
- learns your tone from 3 to 5 of your past replies and gives you a "My tone" note to reuse;
- turns your business facts into a "My business facts" block to reuse;
- writes a full set of quick replies for your most common questions (up to 8 at a time);
- writes a clean quotation from your own prices, with every sum shown.

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/customer-replies/
2. Answer 4 short questions: what kind of business and where; what customers ask most and your answers; how you like to sound; which messages must always come to you. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Paste customer messages one at a time (copying several at once adds names or numbers). Change each name or number to Customer 1, Customer 2 first.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [message-sorter.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/message-sorter.zip)
   - [guest-inquiry-replies.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/guest-inquiry-replies.zip)
   - [quote-and-proposal-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/quote-and-proposal-writer.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "Sort my messages." and paste your messages.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install customer-replies@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **customer-replies** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [message-sorter](../../skills/message-sorter/SKILL.md) | Sorts a batch of up to about 15 pasted messages into "Needs you" (with a holding line each), routine drafts and "no reply needed". Also learns your tone and sets up your business facts. | "Sort my messages." "Which of these need me?" "Learn my tone." "Set up my business facts." |
| [guest-inquiry-replies](../../skills/guest-inquiry-replies/SKILL.md) | Writes short answers to the questions people ask most (price, timings, what's included, how to pay, how to find you), each ready to save as a WhatsApp quick reply. | "Make quick replies for my business." "How do I reply to this customer?" |
| [quote-and-proposal-writer](../../skills/quote-and-proposal-writer/SKILL.md) | Turns your own prices into a quotation or short proposal, with the math on every line and the tax line left blank for your accountant. | A customer asks for a quote, an estimate or a proposal. |

Owner cards (one page each, plain words): [message-sorter](../../skills/message-sorter/OWNER-CARD.md), [guest-inquiry-replies](../../skills/guest-inquiry-replies/OWNER-CARD.md), [quote-and-proposal-writer](../../skills/quote-and-proposal-writer/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **Drafts only.** You check every reply and send it yourself. Nothing is sent automatically.
- **It can't read your WhatsApp.** It only sees what you paste. It can't hear voice notes; type what the voice note says.
- **No automatic replies from this package.** In the free app, greeting and away messages are the simple automatic replies. Any AI auto-reply the app offers is Meta's, not this helper's, and needs care with customer data. A bot that reads and answers customers on its own needs the WhatsApp Business Platform through an approved provider, each customer's opt-in, and approved message templates. That is a builder project (see [BUILDER-NOTES.md](BUILDER-NOTES.md)), not this helper.
- **It won't promise** a price, a slot, availability, a refund, a discount, an arrival time, legal title, a loan or a possession date that you didn't give it. Missing facts come back as [blank] or "Let me check and confirm shortly."
- **It won't follow orders hidden in a customer's message** ("ignore your rules", "say the owner agreed"). Those go to "Needs you".
- **No legal, tax, GST or medical advice.** Quotes keep the tax line blank for your accountant. No invoices or bookkeeping.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Customers' or guests' names and phone numbers (write Customer 1, Customer 2)
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details (the drafts use [your UPI ID])
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

When you copy a message from WhatsApp, it often brings the sender's name or number with it. Change it to Customer 1 before you paste. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([MSR.json](../../evals/testbank/MSR.json), [GIR.json](../../evals/testbank/GIR.json), [QPW.json](../../evals/testbank/QPW.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0).
