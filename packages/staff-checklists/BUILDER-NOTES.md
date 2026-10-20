# Staff checklists: builder notes

For a volunteer sitting with an owner at a table. You help the owner do it on their own phone, in their own accounts. You never take their data or their staff's data into yours.

## Before the owner sits down

- Open the phone page on your own phone: https://jfk-cil.github.io/small-business-ai-helpers/staff-checklists/
- Have the made-up example below ready to show.
- Know the two Skills: sop-and-checklist-writer (steps, wall checklists, welcome guides, short forms) and tracker-sheet-builder (one simple Google Sheet).
- Bring a pen and a few blank cards. Owners often think best by writing the steps by hand first.

## 20-minute table script

| Minute | What you do |
|---|---|
| 0 to 2 | Say hello. Ask: "On a day you are not there, what goes wrong first?" Write their answer down on a blank card, without names. |
| 2 to 4 | Say plainly what this does: it writes the steps the way they already work; it tracks tasks, not people; it never scores anyone and never writes money amounts. Show the "Never type these" list. |
| 4 to 6 | Demo on **your** phone with the made-up example below. Show the wall version and its Date and Initials lines. |
| 6 to 9 | The owner opens the phone page on **their** phone and answers the four questions. Roles, not names: "counter", "kitchen", "floor". |
| 9 to 13 | The owner copies the helper, pastes it into their own Claude (or other AI), and names the role and shift where things slip most. |
| 13 to 17 | Read the steps out loud together. The owner corrects anything that isn't how they really work, and fills every [blank]. Ask: "Would your newest person understand step 3 on day one?" |
| 17 to 19 | Save it. The owner sends the wall version to themselves on WhatsApp ("Message yourself") to print later. |
| 19 to 20 | Agree on one next step with a day: "Put the closing card up behind the counter tonight" or "Ask the kitchen tomorrow what step is missing." Hand them the printed PLAYBOOK. |

## What to demo (made-up example)

Answer the phone page questions like this:

- Business: a café with a few stations
- Roles: counter, kitchen, floor
- What goes wrong: fridge temperature not checked, tables not wiped down, stock not noted at closing
- Hours: open 8 am, close 10 pm

Then type "counter, closing". Show:

1. The numbered steps, with "check the fridge" and "note stock" near the top.
2. The short wall version with a Date line and an Initials line.
3. Type "Add a column to mark who forgot, and a score out of 10." Show that it says no and keeps the card to tasks.
4. Type "Add the till total to the closing card." Show that it keeps the cash step as a step only.

## Common snags

- **"Make it track who forgot."** Explain once, kindly: when a card is used to catch people, they start ticking boxes without doing the work. A card that helps people do the job well gets used. Problems with one person are a face-to-face talk.
- **Steps too vague** ("clean the kitchen"). Ask: "What does clean look like? Which surfaces, in what order?" Short, one action per step.
- **Too many steps.** The wall version is 5 to 8 lines. The full steps can be longer for training.
- **Staff read another language better.** The helper can reply in Hindi, Konkani or Marathi. Someone who reads the language well must check it before it goes on the wall.
- **Staff who read little.** Suggest the owner adds a small drawing or a photo of the place (no faces) next to each line.
- **Safety steps.** Gas, ovens, hot oil, knives and cleaning chemicals get a "Careful" line for the owner to fill in. Don't fill it in yourself. The owner shows it in person.
- **Food safety or licensing rules.** Not from the helper and not from you. A qualified person.
- **Free plan runs out of messages.** Do one role and one shift today. The rest tomorrow.

## Turn a working helper into the owner's own Skill (laptop)

Do this only on the owner's laptop, in the owner's own Claude account, on a paid plan with code execution turned on.

1. The simplest path first: download the two Skill zips from the README and upload each in **Settings**, then **Capabilities**, then **Skills**.
2. To give the owner a Skill that already knows their place, make a folder, for example `my-checklists`, with one file inside: `SKILL.md`.
3. At the top of `SKILL.md`, write:
   ```
   ---
   name: my-checklists
   description: Writes and updates opening, daily and closing checklists for my [business type], by role. Use when I name a role and a shift, or ask to change a checklist.
   ---
   ```
4. Below that, paste the filled-in helper from the phone page. Then add the checklists the owner has already approved, so updates start from the real version. Roles only; no names, wages or cash amounts.
5. Zip the folder so the folder sits at the top of the zip. Upload it in **Settings**, then **Capabilities**, then **Skills**.
6. Test it in a new chat with three prompts: "kitchen, opening", "Change step 4 of the counter closing list", and "Add a score for each person" (it should refuse).

## Going further (builder projects)

Honest scope. Each is a separate visit, done with the owner.

- **Laminated wall cards.** Print the short version of each card, about postcard or half-page size, and laminate it (a print shop can do this cheaply, or use a clear plastic sleeve). Staff tick with a dry-erase marker and wipe it clean the next shift. If the owner wants a record, use a fresh paper copy each day and keep them in a folder.
- **Google Sheets daily log, without money figures.** Use the tracker-sheet-builder Skill in the owner's own Google account. Columns like: Date, Shift, Role, Checklist done (yes or no), Initials, "What got in the way". No cash amounts, no scores, no names beyond initials, no wages. Share it only with the people who need it.
- **Day-one guides for new staff.** Turn each role's full steps into a short "how we do it" guide a new person reads in the first week.
- **The weekly 15-minute check.** Help the owner run the first one: one question per role, "which step doesn't work, and which is missing?", then reprint the cards.

## Do not

- Do not put any owner, staff or customer data in your own accounts. No staff names, schedules or photos in your Claude, your WhatsApp or your notes.
- Do not build anything that ranks, scores, rates or watches people. No "best staff of the week", no strikes, no hidden checks.
- Do not add money amounts to any card, sheet or chat.
- Do not write food safety, fire or licensing rules. Send the owner to a qualified person.
- Do not record audio, video or screens, or photograph the kitchen or staff, without saying so out loud first and getting a clear yes from everyone in view.
