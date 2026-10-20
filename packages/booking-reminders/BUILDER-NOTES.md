# Bookings and reminders: builder notes

For a volunteer sitting with an owner at a table. Aim: the owner leaves with their own booking messages saved as quick replies, a simple booking sheet started on their phone, and a daily reminder in their calendar.

## Before you sit down

- Open https://jfk-cil.github.io/small-business-ai-helpers/booking-reminders/ on your own phone, ready to demo.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner.
- Know the owner's preparation steps matter most. If they haven't written them down, that's the first job.
- The owner uses their own phone and their own AI account. Not yours.

## 20-minute table script

| Time | What you do |
|---|---|
| 0:00 to 2:00 | Say what it is: "It writes the confirmation, reminders and follow-up messages for each booking. You save them once and send them in two taps. It can't send or schedule anything by itself." Ask what people book and what usually goes wrong. If you want to take notes, ask out loud first: paper only, with no names or numbers. No photos or recordings. |
| 2:00 to 5:00 | Demo on your phone with the made-up example below. Show the full set, the [blank]s, and the weekday check. |
| 5:00 to 9:00 | The owner opens the page and answers the 4 questions. Spend most of the time on "What must the customer do or bring beforehand". Their exact words, not yours. |
| 9:00 to 13:00 | Owner copies the helper, opens their AI, pastes and sends. Then describes one real booking without a name: service, day, date, time. Read every message together. Check the preparation lines are exactly the owner's. |
| 13:00 to 17:00 | WhatsApp Business: save the confirmation (`booked`) and the day-before reminder (`tomorrow`) as quick replies. Make the three labels. If time allows, start the booking sheet in the Google Sheets app with the column names from the playbook. |
| 17:00 to 19:00 | Add a daily Google Calendar event for the owner: "Send tomorrow's reminders". Save the helper in "Message yourself". Walk through "Every day" on the playbook. |
| 19:00 to 20:00 | Agree one move for this week (for example: save the other six quick replies). Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. |

## Demo with a made-up example

Answers to type on your phone:
- What people book: "Deep cleaning visits"
- Where: "We go to their home"
- Prep: "Keep water and power on. Clear the kitchen counters."
- Timing: "The evening before and 2 hours before"

Then type this booking (the weekday is wrong on purpose):

```
Deep cleaning, 3BHK, Friday October 24, 10 am.
```

What to point out:
- October 24, 2026 is a Saturday. The helper should say the day and date don't match and let the owner pick.
- The preparation lines are exactly what was typed. Nothing added.
- The confirmation ends with [your business name]. Where the owner's facts are missing, it leaves a [blank].
- The no-show message is one kind line, with no blame and no fee.

Don't use a medical or testing example with made-up preparation steps in the demo. Real steps must come from the owner.

## Common snags

- **Wrong language.** Change the language on the page and make the helper again, or type "Write to me in Marathi" in the chat. Customer messages can be in the customer's language. Translations are drafts; check with someone who reads it well.
- **The owner pastes names, numbers or ID.** Stop. Delete that chat (three dots > Delete) and type the booking again with a code. If they want names in the sheet, they add that column themselves, in their own sheet.
- **The AI promises things** (a slot, "results in 2 days", "the water is safe"). The helper tells it not to. If a draft still does, the owner removes it before saving. Results meaning goes to a qualified person.
- **The AI adds its own preparation steps.** It shouldn't. If it does, delete them and use the owner's words only.
- **Dates look wrong in the sheet.** Set the sheet's locale to India in a browser (File > Settings > Locale) before pasting, so dates read day/month/year.
- **Tours and pickups.** Ask the full version for the pickup version: pickup time, meeting point, what to bring, and "To reach the driver: [blank]" that the owner fills in when sending. Times come only from the owner. If the booking came through an app, the owner sends it in that app's own chat and follows its rules on phone numbers and links.
- **Owner wants a second or third nudge.** The helper writes one. After that, a phone call or let it go.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. It should work there too, though so far it has been tested in Claude only. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turning a working helper into the owner's own Skill (laptop)

Only on the owner's laptop and the owner's own Claude account, on a paid plan with code execution turned on (Settings > Capabilities).

Easiest: download booking-confirmations and tracker-sheet-builder from the package page and upload each in Settings > Capabilities > Skills. booking-confirmations includes a template for writing preparation steps; fill it in once with the owner.

To make a Skill that already knows the owner's business:
1. Make a folder with a short lowercase name, for example `my-booking-messages`.
2. Inside it, make a text file called `SKILL.md` that starts like this:
   ```
   ---
   name: my-booking-messages
   description: Writes confirmation and reminder messages for deep cleaning visits for my business. Use when I describe a booking or say "booking messages".
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
3. Under that, paste the helper text from the phone page and the owner's preparation steps. Hours, days and rules are fine. No customer names, phone numbers, UPI ID, address or passwords.
4. Zip the folder (the folder itself goes inside the zip) and upload it in Settings > Capabilities > Skills.
5. Test it in a new chat with the made-up booking above.

You can also paste the helper into a Claude chat and ask Claude to turn it into a Skill; with code execution on, it can make the zip for the owner to download.

## Going further (builder projects)

Be clear with the owner about size and cost before you start any of these.

- **Booking sheet with formulas** (Google Sheets, owner's account). Tab "Bookings", columns A to I: Booking code, Service, Date, Time, Where, Confirmed?, Reminder sent?, Done?, Notes. Then:
  - Tab "Tomorrow", row 1 copies the headers, A2: `=IFERROR(FILTER(Bookings!A2:I, Bookings!C2:C=TODAY()+1),"No bookings tomorrow")`
  - Tab "Today", A2: `=IFERROR(FILTER(Bookings!A2:I, Bookings!C2:C=TODAY()),"No bookings today")`
  - Color tomorrow's unconfirmed bookings: select columns A to I on "Bookings", custom formula `=AND($C1=TODAY()+1,$F1<>"Yes")`, orange fill.
  - Dropdowns for Confirmed? (Yes, No, Waiting). The tracker-sheet-builder Skill can write the full build with phone steps.
- **Google Calendar.** One event per booking in the owner's own calendar, with a notification to the owner (not the customer). Some Google accounts also offer appointment booking pages; check what the owner's account has.
- **Automatic WhatsApp reminders.** This needs the WhatsApp Business Platform, usually through an approved provider, in the owner's own business account. It needs each customer's opt-in, approved message templates for the reminders, a way to read YES replies and update the sheet, and a person to handle anything else. There are per-message costs. Bookings data stays in the owner's systems. This is weeks of work plus ongoing care.
- **SMS reminders.** Business SMS in India has its own registration rules. Check with a qualified person before building anything.
- **Never** set up unofficial apps that send WhatsApp messages from the owner's phone or ask them to scan a WhatsApp QR code in another app. They can get the number banned.

## Do not

- Put the owner's data in your own accounts. No bookings, customer names or numbers in your Claude, your sheets or your phone.
- Record audio, video or screens, or photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- Post the owner's name, business, phone or booking details anywhere public, including GitHub issues and social media.
- Ask for or touch the owner's passwords or OTPs. They log in themselves.
- Write preparation, health or results advice for the owner. That comes from them or a qualified person.
- Promise results.
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
