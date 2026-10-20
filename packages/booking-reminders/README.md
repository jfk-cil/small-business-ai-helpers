# Bookings and reminders

Confirmation and reminder messages that tell customers exactly what to do.

## The problem

Appointment businesses, such as a testing lab, find that customers book and then forget what to bring, bring the wrong thing, or don't turn up. Reminder phone calls take time and often don't get through. What the owner wants is for the customer to confirm, follow the preparation steps, and arrive ready, without the owner chasing each booking by phone.

## What you get

A full set of booking messages, each in its own copy box, under 500 characters, ready to save as a WhatsApp quick reply:

1. Confirmation, with what to bring or do and how to reschedule
2. Reminder the day before
3. Reminder on the day
4. A "Please reply YES to confirm" nudge (one only)
5. A reschedule reply and a cancellation reply
6. A kind no-show message offering a new slot
7. A thank-you after the visit (or a results-ready note, if you want one)

The full version (Skills) also gives:
- a 5-step daily booking routine;
- the shortcut for each quick reply;
- columns for a simple Google Sheet booking sheet that uses booking codes, not names;
- the full sheet with formulas, color rules and phone setup steps, if you ask for it;
- for tours and activities, a pickup version with pickup time, meeting point and what to bring, to send in the booking app's own chat when the booking came through an app.

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/booking-reminders/
2. Answer 4 short questions: what people book; whether they come to you or you go to them; what the customer must do or bring beforehand (your own instructions); when reminders should go out. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Describe one booking: the service, the day and date, and the time. No names or numbers.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [booking-confirmations.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/booking-confirmations.zip)
   - [tracker-sheet-builder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/tracker-sheet-builder.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "Write my booking messages" and describe your service.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install booking-reminders@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **booking-reminders** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [booking-confirmations](../../skills/booking-confirmations/SKILL.md) | Writes the eight booking messages as quick replies, a daily routine and booking sheet columns. Or just one message for one booking. Includes a template for writing your own preparation steps. | "Write my booking messages." "Confirm this booking." "Customers forget their appointment." "Reminder calls don't work." |
| [tracker-sheet-builder](../../skills/tracker-sheet-builder/SKILL.md) | Designs a simple Google Sheet: columns, made-up sample rows, formulas, color rules and 5 phone setup steps. | "Make me a booking sheet." "Show me tomorrow's bookings." "Stop double bookings." |

Owner cards (one page each, plain words): [booking-confirmations](../../skills/booking-confirmations/OWNER-CARD.md), [tracker-sheet-builder](../../skills/tracker-sheet-builder/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **Drafts only.** You check every message and send it yourself. It can't send, schedule or read anything.
- **No automatic reminders from this package.** Automatic WhatsApp reminders need the WhatsApp Business Platform through an approved provider, each customer's opt-in and approved message templates. That is a builder project (see [BUILDER-NOTES.md](BUILDER-NOTES.md)). The routine here uses quick replies, labels and a Google Calendar reminder for you.
- **It never confirms a slot you haven't confirmed.** It writes "Let me check and confirm shortly." The reschedule reply never promises the new time.
- **Preparation steps come from you only.** It never adds amounts, containers, storage, fasting or "come early". Missing steps come back as [blank].
- **No results meaning.** It won't say what a test result means, or that water, food or a place is safe. That's for a qualified person.
- **No ID photos.** It never asks customers to send Aadhaar, passport or other ID on WhatsApp.
- **No fees or pressure you didn't state.** No no-show charges, no "only 1 slot left". One nudge only.
- **Sheets are not cash books.** No money, invoice or wage columns.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Customers' or guests' names and phone numbers (use a booking code)
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details (the drafts use [your UPI ID])
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people
- Your full address (say "our lab" or "their home"; the drafts use [location link])

If you want a name or phone column in your booking sheet, add it yourself in your own sheet. Never type those into the chat. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([BKC.json](../../evals/testbank/BKC.json), [TSB.json](../../evals/testbank/TSB.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0).
