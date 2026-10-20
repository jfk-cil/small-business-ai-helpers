# Start here

Not sure yet? Find one job AI can help with this week.

## The problem

Many small business owners know their week is too full, but can't say which job to hand to AI first. Long lists of "things AI can do" make it worse: everything sounds possible, so nothing gets started. This package asks a few short questions about your business and your week, then names one job, one helper for it, and a first message you can send today.

## What you get

- A few short questions, one at a time (the phone helper asks at most 6; the full Skill asks at most 5, all in one message). You can answer "pass".
- One job, in one line.
- What you could make for that job today.
- Which helper fits it, from the list below.
- A short success checklist in your own words (phone helper).
- A ready first message to copy, with [blank] wherever a fact is missing.

Where the answer leads:

| If your time goes on | Open this helper |
|---|---|
| Replying to the same customer questions | [Reply to customer messages](../customer-replies/) |
| Confirming bookings, people forgetting or not coming | [Bookings and reminders](../booking-reminders/) |
| Following up with many people who don't reply | [Follow-ups that get replies](../follow-ups/) |
| Not knowing who to sell to or how to reach them | [Find new clients](../find-clients/) |
| Not showing up when people search nearby | [Get found on Google](../get-found-on-google/) |
| Staff doing jobs differently when you're away | [Staff checklists](../staff-checklists/) |
| Finding and welcoming new staff | [Hire and welcome staff](../hire-and-onboard/) |
| Posts and captions | [Posts that bring customers](../social-posts/) |

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/start-here/
2. Answer 2 questions: what kind of business it is, and which part of your week takes the most time. Both are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Answer its questions. Short is fine.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a Claude Skill. It knows more and checks its own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skill: [first-task-finder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/first-task-finder.zip)
2. In Claude, open Settings > Capabilities > Skills and upload the zip file.
3. In a new chat, type: "I'm not sure where AI can help my business."

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install start-here@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **start-here** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [first-task-finder](../../skills/first-task-finder/SKILL.md) | Asks up to 5 short questions, then names one first task, the helper that fits, and a ready first message with [blank]s. | "I'm not sure where to start." "What can AI do for my shop?" "Which helper should I use?" |

Owner card (one page, plain words): [OWNER-CARD.md](../../skills/first-task-finder/OWNER-CARD.md)

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- It picks a job and drafts a first message. It does not do the job itself; the helper it names does that.
- It names one job and one helper, not a menu. That is on purpose.
- It does not help with bookkeeping, cash records, payroll and wages, tax or GST, or judging, ranking or hiring decisions about staff. For money and tax, ask a qualified person such as your accountant. A polite payment reminder message is fine.
- It never promises results. It says what the helper drafts, nothing more.
- Drafts only. You check everything and send it yourself. Nothing is sent automatically.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Customers' or guests' names and phone numbers
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

If you paste one by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

The Skill has written test cases in [evals/testbank/FTF.json](../../evals/testbank/FTF.json), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0).
