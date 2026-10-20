# Start here: builder notes

For a volunteer sitting with an owner at a table. Your job is to help the owner leave with one job, one working helper on their own phone, and a first draft they made themselves.

## Before you sit down

- Open https://jfk-cil.github.io/small-business-ai-helpers/start-here/ on your own phone, ready to demo.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) to give the owner.
- Know the other helper pages (the hub at https://jfk-cil.github.io/small-business-ai-helpers/ lists them all).
- The owner uses their own phone and their own AI account. Not yours.

## 20-minute table script

| Time | What you do |
|---|---|
| 0:00 to 2:00 | Say hello. Explain in two lines: "This helps you pick one job for AI this week. It writes drafts; you always check and send." If you want to take notes, ask out loud first: paper only, with no names or numbers. No photos or recordings. |
| 2:00 to 5:00 | Demo on your phone with the made-up example below. Show the questions, the one job, and the first message with [blank]s. |
| 5:00 to 8:00 | The owner opens the page on their phone and answers the 2 questions. Point out the language picker and the mic. Remind them: no names, numbers or ID. |
| 8:00 to 13:00 | Owner taps **Make my helper**, **Copy helper**, opens their AI, pastes and sends. They answer its questions. You help with words, not answers. |
| 13:00 to 17:00 | Read the result together. Is the job right? If yes, open the named helper's page and make that helper too. Run it once on something real (with names removed). |
| 17:00 to 19:00 | Save both helpers to "Message yourself". Hand over the playbook. Point at "Every day". |
| 19:00 to 20:00 | Agree one move for this week, in the owner's words. Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. |

## Demo with a made-up example

Answers to type on your phone:
- Business: "Small clothes and bags shop near the beach road in Morjim."
- Week: "Tourists ask on Instagram if things are in stock and the price. I answer the same thing all day."

What to point out in the reply:
- It asks short questions one at a time and accepts "pass".
- It names one job ("ready-made replies to the questions tourists ask most") and one helper (Reply to customer messages).
- Facts it doesn't know (timings, prices) come back as [blank]. It never fills them in.

## Common snags

- **Wrong language.** Change the language on the page and tap **Make my helper** again. Or type "Write to me in Konkani (Romi)" in the chat. Drafts for customers can stay in the customer's language. Translations are drafts; check with someone who reads it well.
- **The owner pastes names, numbers or ID.** Stop. Delete that chat (three dots > Delete) and start again with "Customer 1" or a [blank]. The page checks the answers for numbers, but it can't catch names, and it doesn't see what goes into the AI later.
- **The AI promises things.** It should never promise prices, dates or results. If a draft does, the owner edits it before sending. Point to the [blank]s: the owner fills those, not the AI.
- **The owner names a job that isn't covered** (bookkeeping, payroll, tax, judging staff). Say so kindly, suggest a qualified person for that, and ask: "Which other job takes a lot of your time?"
- **Too many jobs at once.** Help them pick the one that happens every week and uses a tool they already have.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. It should work there too, though so far it has been tested in Claude only. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turning a working helper into the owner's own Skill (laptop)

Only on the owner's laptop and the owner's own Claude account, on a paid plan with code execution turned on (Settings > Capabilities).

For this package the best next step is usually to install the Skills of the helper it named. Each helper page has download links under "On a laptop? Install the full version". Upload each zip in Settings > Capabilities > Skills.

To make a Skill that already knows the owner's business:
1. Make a folder with a short lowercase name, for example `my-shop-helper`.
2. Inside it, make a text file called `SKILL.md` that starts like this:
   ```
   ---
   name: my-shop-helper
   description: Helps me with [the one job] for my [kind of business] in [town]. Use when I say [the words the owner uses].
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
3. Under that, paste the helper text the owner copied from the phone page. Business facts only: no customer names, phone numbers, UPI ID or passwords.
4. Zip the folder (the folder itself goes inside the zip) and upload it in Settings > Capabilities > Skills.
5. Test it in a new chat with a made-up example.

You can also paste the helper into a Claude chat and ask Claude to turn it into a Skill; with code execution on, it can make the zip for the owner to download.

## Going further (builder projects)

- **A Claude Project** on the owner's own paid account, with their business facts and tone as the instructions. Small job, about 15 minutes. Then every chat in that Project already knows the business.
- **The next helper.** Once the first job is a habit, come back and run Start here again, or open the next package. One at a time.
- **A simple time log** the owner keeps in their own notebook or sheet: date, job, minutes spent. It helps them judge if a helper is worth keeping. Don't collect it yourself and don't publish it.

## Do not

- Put the owner's data in your own accounts. No owner messages in your Claude, your notes app or your phone's photos.
- Record audio, video or screens, or photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- Post the owner's name, business, phone or results anywhere public, including GitHub issues and social media.
- Ask for or touch the owner's passwords or OTPs. They log in themselves.
- Promise results ("this will double your bookings").
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
