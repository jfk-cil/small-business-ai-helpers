# Follow-ups that get replies

A polite 3-step follow-up, a daily "who to message today" list, and an end-of-day report.

## The problem

Groups and businesses that reach out to many people, such as a nonprofit or membership group contacting past supporters, can manage the first message but lose track of the follow-ups. Calls go unanswered, messages get no reply, and a warm contact goes cold. What they want is a polite follow-up two or three times, each with a purpose, until the person answers, plus a clear list of who is due and a short report at the end of each day.

This package is the honest, semi-manual version of a "follow-up bot". The AI drafts the messages and does the date math. You send.

## What you get

- **A 3-message sequence:** the first message, follow-up 2, and a polite last message that makes "no thanks" easy and leaves the door open. Each in its own copy box, under 500 characters.
- **Stop rules:** stop when someone replies, says no or asks to stop. Never more than 3 messages per person.
- **Who to message today:** paste tracker rows that use codes, not names, plus today's date. You get who gets which message, who to stop, and each next date.
- **End-of-day report:** paste your short notes. You get counts (sent, replied, yes, no, call back, asked to stop) and tomorrow's first 3 actions.

The full version (Skills) also gives:
- a tracker sheet layout with a "Due today" view;
- replies and follow-ups for one new inquiry;
- one-off messages to people who already agreed to hear from you (a renewal notice, an event reminder, a thank-you).

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/follow-ups/
2. Answer 4 short questions: who you follow up with; what your first message asks for; how many days between follow-ups; how you sign your messages. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Type "sequence" to get your 3 messages.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [follow-up-planner.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/follow-up-planner.zip)
   - [lead-reply-and-follow-up.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/lead-reply-and-follow-up.zip)
   - [tracker-sheet-builder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/tracker-sheet-builder.zip)
   - [customer-message-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/customer-message-writer.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "Make my follow-up messages" and say who they are for.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install follow-ups@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **follow-ups** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [follow-up-planner](../../skills/follow-up-planner/SKILL.md) | Writes a polite sequence of up to 3 messages with stop rules, works out who to follow up today from coded tracker rows, and turns end-of-day notes into a report. Explains what real automation would need. | "I can't follow up everyone." "Who do I follow up today?" "Make today's report." "Renewal reminders." |
| [lead-reply-and-follow-up](../../skills/lead-reply-and-follow-up/SKILL.md) | Writes the first reply to one new inquiry, plus up to 3 follow-ups ending in a polite close. | "Someone inquired. What do I reply?" "They went quiet after I answered." |
| [tracker-sheet-builder](../../skills/tracker-sheet-builder/SKILL.md) | Designs a simple Google Sheet with columns, sample rows, formulas, colors and phone setup steps. | "Make me a follow-up tracker." "Show me who is due today." |
| [customer-message-writer](../../skills/customer-message-writer/SKILL.md) | Writes one message for many people who already agreed to hear from you, with a way to stop getting messages. | "Message all our members about the new date." "Thank-you after the event." |

Owner cards (one page each, plain words): [follow-up-planner](../../skills/follow-up-planner/OWNER-CARD.md), [lead-reply-and-follow-up](../../skills/lead-reply-and-follow-up/OWNER-CARD.md), [tracker-sheet-builder](../../skills/tracker-sheet-builder/OWNER-CARD.md), [customer-message-writer](../../skills/customer-message-writer/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **Not a bot.** It can't send, schedule or read WhatsApp or email. You send every message.
- **Truly automatic follow-ups** need the WhatsApp Business Platform through an approved provider, each person's opt-in, approved message templates, and a way to stop at once when someone replies or says stop. That is a builder project (see [BUILDER-NOTES.md](BUILDER-NOTES.md)).
- **Three messages at most** per person. No fourth, no daily chasing, never two steps on one day.
- **Same channel only.** It never helps you reach someone through a family member, a friend or another number.
- **No guilt, pressure or invented facts.** No "we're counting on you", no made-up numbers, deadlines, matching gifts or event dates.
- **No tax-benefit claims** for donations unless you state them, and then check with a qualified person before sending.
- **Only people who agreed.** No bought, copied or scraped lists.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Names and phone numbers of supporters, members or customers (use codes like S1, S2, M3)
- Your contact list
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details (the drafts use [your UPI ID])
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

Keep names and numbers only in your own sheet, next to each person's code. Type only the codes into the AI. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([FUP.json](../../evals/testbank/FUP.json), [LRF.json](../../evals/testbank/LRF.json), [TSB.json](../../evals/testbank/TSB.json), [CMW.json](../../evals/testbank/CMW.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0).
