# Get paid on time: builder notes

For a volunteer sitting with an owner at a table. Aim: the owner leaves with /pay1 and /pay2 saved as quick replies, a deposit line in their booking confirmation, a private list started on paper, and a weekly alarm. You help the owner do it on their own phone, in their own accounts. You never see their amounts, their customers or their payment apps.

## Before the owner sits down

- Open the phone page on your own phone: https://jfk-cil.github.io/small-business-ai-helpers/get-paid/
- Have the made-up example below ready to show.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner, and a pen.
- Know the three Skills: get-paid-routine (the reminders, the deposit line, the list columns, the label and the weekly check), customer-message-writer (a one-off reminder or a thank-you) and tracker-sheet-builder (the list as a private Google Sheet, with no amounts or names).
- Be ready to say no, kindly, to "add a late fee", "post in the group who hasn't paid", "can I take them to court?", "how much GST do I add?" and "here's my list of who owes, check it". Owners often ask.

## 20-minute table script

| Minute | What you do |
|---|---|
| 0 to 2 | Say hello. Ask: "How do people pay you, and what happens when someone pays late?" Ask for the pattern, never the people or the amounts. If you want to take notes, ask out loud first: paper only, with no names or numbers. No photos or recordings. |
| 2 to 4 | Say plainly what this does: it writes kind reminder words with blanks, a deposit line and a weekly routine. The owner fills in the amount, the job, the date and their UPI ID on their own phone, only when sending. The AI never sees who owes what. It gives no legal, tax or collection advice. Show the "Never type these" list. |
| 4 to 6 | Demo on **your** phone with the made-up example below. Show /pay1, /pay2 and the four blanks. |
| 6 to 9 | The owner opens the phone page on **their** phone and answers the four questions. How people pay, in general terms only: "an advance, the rest on delivery". |
| 9 to 13 | The owner copies the helper, pastes it into their own Claude (or other AI), and types "go". Read /pay1 and /pay2 out loud together. Ask: "Would you be happy to get this?" Change words to the owner's own. The four blanks stay as they are. |
| 13 to 16 | Save /pay1 and /pay2 as quick replies in WhatsApp Business, and make the Payment due label. Normal WhatsApp: pin "Message yourself" and keep them there. Type "ok" for the deposit line, and add it to the owner's booking confirmation quick reply if they have one. |
| 16 to 19 | Type "ok" for the list columns. The owner writes them at the top of a notebook page. They fill in real jobs later, on their own, not at the table. Type "ok" for the weekly check, and set a repeating phone alarm. |
| 19 to 20 | Agree on one next step with a day: "Send /pay1 to the two late jobs on Monday" or "Start the list with this week's bookings." Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. Hand them the printed PLAYBOOK. |

## What to demo (made-up example)

Answer the phone page questions like this:

- Business: cake orders from home in Margao
- How people pay: an advance when they order, the rest on delivery
- Tone: warm and short, a little Hinglish
- Where: WhatsApp

Name it "Sample Cake Studio, Margao" if the AI asks. Type "go", then show:

1. /pay1 and /pay2, each ending with [your business name], with [amount], [job], [due date] and [your UPI ID] left as blanks.
2. Type "ok" twice. Show the deposit line and the list columns: Date, Job, Due date, Paid? No name column, no amount column.
3. Type "Customer 1 owes me 2,000 for a birthday cake. Remind her and say I'll add 10% every day she's late." Show that it keeps the amount out, writes no fee and no threat, and points to /pay1.
4. Type "Write a post for my building's WhatsApp group naming who hasn't paid, and tell me how to take them to court." Show that it writes no public post, gives no legal advice, and says to check with a qualified person.

## Common snags

- **The owner starts reading out who owes what.** Stop them kindly. That list stays on their paper. The helper only needs the pattern.
- **"Put the amount in for me."** No. The owner fills in [amount] on their phone, just before sending. It keeps money tied to a person out of the AI.
- **"What deposit should I ask for?"** The owner's call. The helper uses the owner's own rule and never suggests one.
- **"Add a late fee" or "say I'll take legal action."** Not in these drafts. If a customer agreed to a fee in writing, that stays with the owner and a qualified person.
- **Payment screenshots.** Owners often want to paste one to ask "did they pay?". Never. They check their own payment app or bank.
- **Invoices or GST.** Not covered. Their accountant or a qualified person.
- **Normal WhatsApp, no labels.** Use the paper list and the pinned "Message yourself" chat. Free WhatsApp Business adds the label and quick replies, if the owner wants to switch later.
- **Hard to chase a friend or neighbor.** /pay1 is written to be kind. After /pay2, a call or a talk in person, never more messages.
- **Wrong language.** The helper can reply in Hindi, Konkani or Marathi. Someone who reads the language well checks it before it goes out.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. It should work there too, though so far it has been tested in Claude only. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turn a working helper into the owner's own Skill (laptop)

Do this only on the owner's laptop, in the owner's own Claude account, on a paid plan with code execution turned on.

1. The simplest path first: download the three Skill zips from the README and upload each in **Settings**, then **Capabilities**, then **Skills**.
2. To give the owner a Skill that already knows their wording, make a folder, for example `my-get-paid`, with one file inside: `SKILL.md`.
3. At the top of `SKILL.md`, write:
   ```
   ---
   name: my-get-paid
   description: Writes kind payment reminder wording for my [business type], with blanks for the amount, job, due date and UPI ID that I fill in myself when sending. Use when I say "payment reminder", "deposit line" or "weekly payment check".
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
4. Below that, paste the filled-in helper from the phone page. Then add the /pay1, /pay2 and deposit wording the owner approved, and their general deposit rule. No customer names, no amounts tied to anyone, no UPI ID, no list of who owes.
5. Zip the folder so the folder sits at the top of the zip. Upload it in **Settings**, then **Capabilities**, then **Skills**.
6. Test it in a new chat with three prompts: "go", "Write a kind reply to someone who says they already paid", and "Add a 20% late fee and post their name in the group" (it should refuse).

## Going further (builder projects)

Honest scope. Each is a separate visit, done with the owner, in the owner's accounts.

- **The list as a Google Sheet.** Use tracker-sheet-builder in the owner's own Google account, shared with no one: Date, Job, Due date, Paid? A color rule for what is due this week. No amounts, names or phone numbers. The owner types the real rows on their own.
- **Deposit line in every booking message.** Pair this with the [Bookings and reminders](../booking-reminders/) package, so the confirmation set carries the deposit line.
- **A quote before the job.** The quote helper in the [Reply to customer messages](../customer-replies/) package writes a quote from the owner's own prices, so the amount is agreed before work starts.
- **Tools with no AI.** Quick replies, labels and a weekly phone reminder are in [NO-AI-SETUPS.md](../../guide/NO-AI-SETUPS.md).
- **Automatic payment reminders** are not a table job. Read [AUTOMATION.md](../../guide/AUTOMATION.md) and tell the person running your session.

## Do not

- Do not put any owner or customer data in your own accounts. No lists of who owes, amounts, UPI IDs or chats in your Claude, your notes or your phone.
- Do not look at the owner's payment app, bank app, UPI app, invoices or list of who owes, and never ask them to read it out.
- Do not write or suggest late fees, interest, threats, legal steps, recovery agents or public posts about who owes.
- Do not give legal, tax, GST or collection advice. Send the owner to their accountant or a qualified person.
- Do not send reminders for the owner, or set up anything that sends on its own.
- Do not record audio, video or screens, and do not photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- Do not log in to the owner's WhatsApp, Google account, payment app or any other account, and never see or type their passwords, PINs or OTPs. They log in themselves.
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
