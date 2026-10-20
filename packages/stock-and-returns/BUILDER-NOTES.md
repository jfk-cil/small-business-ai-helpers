# Stock checks and returns: builder notes

For a volunteer sitting with an owner at a table. You help the owner do it on their own phone, in their own accounts. You never take their data, their staff's data or their supplier's data into yours.

## Before the owner sits down

- Open the phone page on your own phone: https://jfk-cil.github.io/small-business-ai-helpers/stock-and-returns/
- Have the made-up example below ready to show.
- Know the three Skills: stock-check-and-returns (the routine, the how-to, tracker columns and supplier messages), sop-and-checklist-writer (wall cards and other step-by-step guides) and tracker-sheet-builder (the Google Sheet).
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner.
- Be ready to say no, kindly, to "is this still OK to sell?", "log in to my billing software" and "add a column for who missed items". Owners often ask.

## 20-minute table script

| Minute | What you do |
|---|---|
| 0 to 2 | Say hello. Ask: "Which stock job comes back every month, and which step does your staff get stuck on?" If you want to take notes, ask out loud first: paper only, with no names or numbers. No photos or recordings. |
| 2 to 4 | Say plainly what this does: it writes the steps the way they already work, gives each step to a role and a day, and drafts the supplier messages. It never says whether expired stock is safe, never invents supplier terms and never writes money amounts. Show the "Never type these" list. |
| 4 to 6 | Demo on **your** phone with the made-up example below. Show one step with its Who, When, Done when and Sign-off lines. |
| 6 to 9 | The owner opens the phone page on **their** phone and answers the four questions. Roles, not names. If they are not sure of their near-expiry window, they skip it; the helper leaves it [blank]. |
| 9 to 13 | The owner copies the helper, pastes it into their own Claude (or other AI), and types "go". Read the routine out loud together. Ask: "Would your newest person know what to do on step 1, on day one?" Fill each [blank] the owner is sure of. |
| 13 to 16 | Type "ok" for the how-to and "ok" for the tracker columns. The owner writes the real billing menu name on paper, not in the chat. If they have a laptop and time, paste the columns into a new Google Sheet in their own account. |
| 16 to 19 | Type "ok" for the supplier messages. The owner saves the request and the follow-up in a phone note, and sets a repeating calendar reminder for the check day. |
| 19 to 20 | Agree on one next step with a day: "Print the routine and run the check on the 1st" or "Ask the billing staff to show the return menu tomorrow." Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. Hand them the printed PLAYBOOK. |

## What to demo (made-up example)

Answer the phone page questions like this:

- What and where: pet supplies shop in Porvorim
- Steps today: check expiry dates against the sheet, make the purchase return in the billing software, pack, follow up with the supplier
- Who and when: store assistant counts on the 1st, billing staff makes the return by the 3rd, owner follows up
- Near expiry: within 60 days

Name it "Sample Pet Supplies, Porvorim" if the AI asks. Type "go", then show:

1. The routine: each step with a role, a day, "Done when" and a sign-off line. Time is [blank] because the owner didn't give it.
2. Type "ok" twice. Show the how-to with [menu name in your billing software], and the tracker columns with quantities and dates only.
3. Type "Write a WhatsApp to customers: expired dog food at 50% off, still safe. And tell the supplier their return window is 90 days." Show that it writes no sale message, makes no safety claim and leaves the return window out.
4. Type "Add a column for stock value and one for which staff member missed items." Show that it keeps the tracker to quantities and dates and keeps people out of it.

## Common snags

- **"Is it still OK to sell?"** Not from the helper and not from you. A qualified person and the supplier's terms. The helper can write the return request instead.
- **The owner names their billing software.** The helper still writes [menu name in your billing software]. It can't see the software. The person who set it up shows the menu once; the owner writes the real name on the printed how-to.
- **"Fill in how long each step takes."** Only the owner knows. Ask them to time it once this month and fill it in next month.
- **"What near-expiry window should we use?"** The owner's call, and the supplier's terms. The helper leaves it [blank] until the owner says.
- **Staff names creep in.** Owners often type a name, or "the boy", for who does a step. Change it to a role ("store assistant") before pasting. If one got in, delete that chat and start again.
- **Stock value or credit-note amounts.** Keep them in the owner's own accounts book or software. The tracker has a "Credit note received" yes or no column only.
- **"Make it track who missed items."** Explain once, kindly: a sign-off shows a step is done. Mistakes are fixed in the step, and problems with one person are a face-to-face talk.
- **Medicines or vet products.** Process steps only. Use, storage and disposal: a qualified person.
- **Staff read another language better.** The helper can reply in Hindi, Konkani or Marathi. Someone who reads the language well must check it before it goes to staff.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. It should work there too, though so far it has been tested in Claude only. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turn a working helper into the owner's own Skill (laptop)

Do this only on the owner's laptop, in the owner's own Claude account, on a paid plan with code execution turned on.

1. The simplest path first: download the three Skill zips from the README and upload each in **Settings**, then **Capabilities**, then **Skills**.
2. To give the owner a Skill that already knows their routine, make a folder, for example `my-stock-check`, with one file inside: `SKILL.md`.
3. At the top of `SKILL.md`, write:
   ```
   ---
   name: my-stock-check
   description: Runs my monthly expiry check and supplier returns for my [business type], with each step given to a role and a day. Use when I say "stock check", "near expiry", "purchase return" or ask for a supplier message.
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
4. Below that, paste the filled-in helper from the phone page. Then add the routine the owner has already approved, their near-expiry window and the real billing menu names, so updates start from the real version. Roles only; no staff names, supplier contacts, prices or stock value.
5. Zip the folder so the folder sits at the top of the zip. Upload it in **Settings**, then **Capabilities**, then **Skills**.
6. Test it in a new chat with three prompts: "go", "Write the follow-up to the supplier", and "Is this expired cat food OK to sell at half price?" (it should refuse).

## Going further (builder projects)

Honest scope. Each is a separate visit, done with the owner, in the owner's accounts.

- **The tracker as a Google Sheet.** Use tracker-sheet-builder in the owner's own Google account, with the Skill's columns (the phone helper's step 3 columns also work): Date checked, Item, Batch no., Expiry date, Quantity, Reason, Supplier, Request sent on, Picked up on, Credit note received. A color rule for items inside the owner's window. No prices, stock value, staff names or supplier contacts.
- **A wall card.** Use sop-and-checklist-writer for a 5 to 8 line version of the routine with a Date line and an Initials line. Stick it by the storeroom.
- **Damaged and slow stock.** The same routine, with the owner's own meaning of "slow". Prices, discounts and reordering stay with the owner.
- **A first check together.** Sit with the store assistant on the next check day, with the how-to in hand. Fix the steps that didn't work, then reprint.
- **Daily checklists.** The [Staff checklists](../staff-checklists/) package writes the opening and closing cards, so "note near-expiry items" can sit in the daily routine too.

## Do not

- Do not put any owner, staff, customer or supplier data in your own accounts. No stock lists, supplier contacts or staff names in your Claude, your sheets or your phone.
- Do not say whether expired or near-expiry products are safe to sell, use, donate, discount or throw away. Send the owner to a qualified person and the supplier's terms.
- Do not write or suggest supplier terms, return windows or deadlines.
- Do not add money amounts to any routine, tracker or chat.
- Do not build anything that ranks, scores, fines or watches staff.
- Do not record audio, video or screens, and do not photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- Do not log in to the owner's billing software, Google account or any other account, and never see or type their passwords or OTPs. They log in themselves.
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
