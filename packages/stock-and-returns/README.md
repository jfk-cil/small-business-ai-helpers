# Stock checks and returns

A monthly routine for expiry checks and supplier returns, with each step given to a role and a day, so staff can do it without hand-holding.

## The problem

Shops that sell packaged goods with expiry dates, such as a pet supplies shop, a grocery or a cosmetics counter, have the same job every month. Someone has to find the expired and near-expiry stock, check it against the count, make a purchase return in the billing software, pack the products and follow up with the supplier until they are picked up. Staff need hand-holding at each step, and the owner ends up chasing it. The steps live in the owner's head and in a sheet or notebook. What the owner wants is each step assigned, with a timeline, and a way to train new staff once.

## What you get

The phone helper works in four steps, one per message, and asks before moving on:

1. **The monthly routine:** each step with the role that does it, the day of the month, about how long it takes, what "done" looks like and a sign-off line.
2. **A first-time how-to** for a new staff member: what to check, common mistakes, and the billing-software steps written as [menu name in your billing software], because the AI can't see your software.
3. **Columns for a tracker sheet:** item, batch, expiry date, quantity, status, supplier, return date and follow-up date. Quantities and dates only, no money.
4. **A message to your supplier** asking for a return or pickup, and one polite follow-up.

The full version (Skills) also:
- covers damaged stock and slow stock, not only expiry;
- says what to do if the supplier still doesn't reply;
- writes daily opening and closing checklists and a short wall card for the routine;
- builds the tracker as a Google Sheet with formulas, color warnings for items close to expiry, and 5 phone setup steps.

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/stock-and-returns/
2. Answer 4 short questions: what you sell and where; the steps today; who does it and when (roles, not names); what counts as near expiry for you. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Type "go" to start with your monthly routine.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [stock-check-and-returns.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/stock-check-and-returns.zip)
   - [sop-and-checklist-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/sop-and-checklist-writer.zip)
   - [tracker-sheet-builder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/tracker-sheet-builder.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "Monthly expiry check and supplier returns. My staff needs hand holding." Then describe your steps.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install stock-and-returns@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **stock-and-returns** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [stock-check-and-returns](../../skills/stock-check-and-returns/SKILL.md) | Turns a monthly stock job (expiry and near-expiry check, supplier returns, damaged or slow stock) into a routine with a role, a day, "done when" and a sign-off for each step, a first-time how-to, tracker columns, and a return request with one polite follow-up. | "Monthly expiry check." "Purchase return to the vendor." "Assign this task with a timeline." |
| [sop-and-checklist-writer](../../skills/sop-and-checklist-writer/SKILL.md) | Turns how you do a job into numbered steps for a new person, or a checklist to print and tick. | "Make a wall card for the expiry check." "Write the closing steps for the counter." |
| [tracker-sheet-builder](../../skills/tracker-sheet-builder/SKILL.md) | Designs one simple Google Sheet with sample rows, formulas, color rules and 5 phone setup steps. | "Build the expiry tracker." "Show me what expires this month." |

Owner cards (one page each, plain words): [stock-check-and-returns](../../skills/stock-check-and-returns/OWNER-CARD.md), [sop-and-checklist-writer](../../skills/sop-and-checklist-writer/OWNER-CARD.md), [tracker-sheet-builder](../../skills/tracker-sheet-builder/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **Drafts only.** You check every step, share the routine with your team, and send or call the supplier yourself. It can't send messages, call anyone or set reminders.
- **It can't see your billing software.** Every menu is left as [menu name in your billing software]. Ask whoever set up the software to show the menu once.
- **It never decides safety.** It won't say whether expired or near-expiry food, pet food, medicine, supplements or cosmetics are safe to sell, use, donate, discount or throw away, or how to dispose of them. It writes no message selling expired items. Check with a qualified person and your supplier's terms.
- **Your numbers, your terms.** It uses your near-expiry window exactly and never suggests one. It never invents supplier return windows, deadlines, fees or credit notes. Anything you didn't give stays [blank].
- **Quantities yes, money no.** The tracker keeps quantities and dates, and a "Credit note received" yes or no column. No prices, stock value or credit-note amounts.
- **Tasks, not people.** Steps go to roles. A sign-off means the step is done, not how well. It will not add columns for mistakes, fines, warnings or scores.
- **No legal, tax or licensing advice.** A dispute with a supplier, GST on returns, or rules for medicines and vet products: check with a qualified person.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Customers' names and phone numbers
- Staff names, ID numbers or wages (write "store assistant", not a name)
- The supplier contact's name and phone number (write "the supplier")
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details
- Passwords and OTPs, including your billing software login
- Sales or money figures (your public prices are fine)
- Stock value and credit-note amounts (quantities and dates are fine)
- Health information
- Family members' details
- Photos of people

Your real counts stay in your own sheet or billing software. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([SCR.json](../../evals/testbank/SCR.json), [SOP.json](../../evals/testbank/SOP.json), [TSB.json](../../evals/testbank/TSB.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you check, share and send everything yourself.
