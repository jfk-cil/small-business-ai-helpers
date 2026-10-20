# Follow-ups: builder notes

For a volunteer sitting with an owner at a table. Aim: the owner leaves with a 3-message sequence saved as quick replies, a coded tracker started in their own sheet, and the daily "who is due" and "report" habits tried once.

Owners often arrive asking for "a bot that follows up 2 or 3 times and sends me a report". Be honest early: this package is the manual version that works today. The real bot is a bigger project with rules and costs (see "Going further").

## Before you sit down

- Open https://jfk-cil.github.io/small-business-ai-helpers/follow-ups/ on your own phone, ready to demo.
- Copy the made-up tracker rows below into a note on your phone.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner.
- The owner uses their own phone, their own sheet and their own AI account. Not yours.

## 20-minute table script

| Time | What you do |
|---|---|
| 0:00 to 2:00 | Say what it is: "It writes your follow-up messages, tells you who is due each day, and makes your daily report. You send every message. It is not a bot." Ask who they follow up and how many people. If you want to take notes or record, say so out loud and ask first. Only go ahead on a clear yes. |
| 2:00 to 5:00 | Demo on your phone: type "sequence", then paste the made-up tracker rows below. Show the date math and the Stop list. |
| 5:00 to 8:00 | The owner opens the page and answers the 4 questions. Make sure "days between follow-ups" is their number, not yours. |
| 8:00 to 12:00 | Owner copies the helper, opens their AI, pastes, sends, and types "sequence". Read the 3 messages together. Remove anything that sounds like pressure or guilt. Fill the [blank]s. |
| 12:00 to 15:00 | WhatsApp Business: save the 3 messages as quick replies (`fu-first`, `fu-second`, `fu-last`). Make the labels. |
| 15:00 to 18:00 | Start the tracker in the Google Sheets app with the column names from the playbook. The owner gives 3 real people codes (S1, S2, S3). Names, if any, go only in the owner's sheet. Then paste those 3 coded rows into the AI to see "who is due today". |
| 18:00 to 20:00 | Try the end-of-day report with made-up notes. Add the daily calendar reminder. Agree one move for this week. Check the AI chat has no names or numbers; if it does, delete that chat together. |

## Demo with a made-up example

Answers to type on your phone:
- Who: "Past donors of a small animal shelter in Mapusa"
- Ask: "Join our winter food drive. Drop food at the shelter or give by UPI."
- Gap: "3 days"
- Sign: "[your name], [group name]"

Then type:

```
Today is October 19, 2026. Wait 3 days between messages.
S14 | last message Oct 12 | step 1 | no reply
S15 | last message Oct 17 | step 1 | no reply
S16 | last message Oct 16 | step 2 | no reply
S18 | last message Oct 15 | step 2 | replied
S19 | step 1 | asked to stop
```

What to point out:
- S14 is due (October 15 has passed): send step 2 today, once.
- S16 is due today: send step 3, the last message.
- S15 is coming up on Tuesday, October 20.
- S18 replied: no message; the owner answers personally.
- S19 asked to stop: no message, mark Do not contact.

Then try the report with: "Sent 12, S3 said yes, S7 call back Friday, S9 asked to stop. Report."

## Common snags

- **Wrong language.** Change the language on the page and make the helper again, or type "Write to me in Konkani (Romi)" in the chat. Messages can go out in the supporter's language. Translations are drafts; check with someone who reads it well.
- **The owner pastes names, numbers or their contact list.** Stop. Delete that chat (three dots > Delete). Give each person a code in the owner's own sheet and paste only codes.
- **The AI promises or invents things** (a number of families helped, a deadline, a tax benefit). The helper tells it not to. If a draft still does, the owner removes it. Real numbers come only from the owner.
- **Dates read the wrong way.** The helper reads 10/12 as day/month. Writing "Oct 12" avoids confusion. In Google Sheets, set the locale to India in a browser (File > Settings > Locale) so dates match.
- **Owner wants a fourth message or daily chasing.** The helper stops at 3. Explain that more can feel like pressure and gets numbers blocked or reported.
- **Broadcast lists don't reach everyone.** In WhatsApp Business, a broadcast only reaches people who saved the owner's number. Follow-ups work best one chat at a time with quick replies.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turning a working helper into the owner's own Skill (laptop)

Only on the owner's laptop and the owner's own Claude account, on a paid plan with code execution turned on (Settings > Capabilities).

Easiest: download the four Skills from the package page (follow-up-planner, lead-reply-and-follow-up, tracker-sheet-builder, customer-message-writer) and upload each in Settings > Capabilities > Skills.

To make a Skill that already knows the owner's group:
1. Make a folder with a short lowercase name, for example `my-follow-ups`.
2. Inside it, make a text file called `SKILL.md` that starts like this:
   ```
   ---
   name: my-follow-ups
   description: Writes follow-up messages, the daily "who is due" list and the end-of-day report for our winter food drive. Use when I say "sequence", paste tracker rows with codes, or paste my day's notes.
   ---
   ```
3. Under that, paste the helper text from the phone page and the owner's final 3 messages. No names, phone numbers, UPI ID or passwords.
4. Zip the folder (the folder itself goes inside the zip) and upload it in Settings > Capabilities > Skills.
5. Test it in a new chat with the made-up tracker rows above.

You can also paste the helper into a Claude chat and ask Claude to turn it into a Skill; with code execution on, it can make the zip for the owner to download.

## Going further (builder projects)

Be clear with the owner about size and cost before you start any of these.

- **Tracker formulas** (Google Sheets, owner's account). Tab "Tracker", columns A to H as in the playbook. Put the waiting days in J2 (after step 1) and J4 (after step 2); the owner types their own numbers.
  - Next follow-up date, F2 (copy down): `=IF(OR(E2="",G2<>"Waiting",D2>=3),"",E2+IF(D2=1,$J$2,$J$4))`. It goes empty once someone replies, says no, asks to stop, or has had step 3.
  - Tab "Due today", row 1 copies the headers, A2: `=IFERROR(FILTER(Tracker!A2:H, Tracker!F2:F<>"", Tracker!F2:F<=TODAY(), Tracker!G2:G="Waiting"),"Nothing due today")`
  - Count due: `=COUNTIFS(Tracker!F2:F,"<="&TODAY(),Tracker!G2:G,"Waiting")`
  - Colors: select columns A to H, custom formula `=AND($F1<>"",$F1<=TODAY(),$G1="Waiting")`, orange fill. `=$G1="Stop"`, grey text.
  - Dropdowns: Step (1, 2, 3), Status (Waiting, Replied, Yes, No, Stop).
- **Email follow-ups.** Gmail's Schedule send lets the owner schedule each email. It does not cancel if the person replies first, so check before it goes. Gmail templates (on a computer) save each step's text.
- **Truly automatic WhatsApp follow-ups.** This needs the WhatsApp Business Platform, usually through an approved provider, in the group's own business account. Before building: a record of each person's opt-in, approved message templates for every message the group starts, per-message costs (get current prices in writing), a stop that works at once and forever, and a person to read and answer replies. India has rules on promotional messages and personal data; check with a qualified person what applies. Moving the number to the Platform can change how it works in the phone app. Names and numbers stay in the group's own system, never in an AI chat. This is weeks of work plus ongoing care.
- **Never** set up unofficial apps that send WhatsApp messages from the owner's phone or ask them to scan a WhatsApp QR code in another app. They can get the number banned.

## Do not

- Put the owner's data in your own accounts. No contact lists, names, numbers or tracker rows in your Claude, your sheets or your phone.
- Record or photograph anything without saying so out loud first and hearing a yes.
- Post the owner's name, group, phone, screenshots or reports anywhere public, including GitHub issues and social media.
- Ask for or touch the owner's passwords or OTPs. They log in themselves.
- Help message people who never agreed, or reach someone through their family or friends.
- Promise results.
