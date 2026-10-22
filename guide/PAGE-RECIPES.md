# Page recipes: small Claude pages that hold no customer data

For owners and builders. Claude can make a small web page for you (Claude calls it an "artifact") and give you a link to share. These three recipes make pages your staff can use on their own phones:

- (a) a staff checklist with tick boxes that clear each day
- (b) a quote worksheet that adds up the line items you type
- (c) a "today's jobs" board with job types and times only

None of them holds customer names, phone numbers, addresses or payment details. Tested examples of all three are in [examples/pages/](../examples/pages/): [checklist.html](../examples/pages/checklist.html), [quote-worksheet.html](../examples/pages/quote-worksheet.html), [todays-jobs.html](../examples/pages/todays-jobs.html).

**Plans.** Making and sharing pages worked on free and paid Claude plans (as of October 2026; check current plans). Menu names below may change.

## Rules for every page

- **No people's details.** No names (customers or staff), phone numbers, email addresses, addresses, ID numbers, UPI IDs, bank details or payment amounts tied to anyone.
- **No forms that send anything.** The page must not send, email, upload or post anything anywhere.
- **No outside files.** No scripts, fonts, images or trackers from other websites.
- **Storage only on the viewer's own phone, and only if needed.** A checklist may remember ticks on that phone until the next day. Nothing else is saved. The page must still work if the phone won't save.
- **Not for watching staff.** Each phone has its own ticks. The page can't show who did what, and must never be used to judge, score or check on anyone.
- **Drafts and tools only.** A quote worksheet adds up; it doesn't decide prices, tax or discounts.

## How to make one (all three recipes)

1. Open Claude in your own account and start a new chat.
2. Copy the prompt for the page you want (below). Replace the parts in square brackets with your own steps, items or job types. No names or numbers.
3. Send it. Claude makes the page and shows it beside the chat (on a phone, tap to open it).
4. Try it yourself: tick, add, remove, add up. Use the checks below.
5. Want a change? Ask in the same chat: "Make the text bigger", "Add a step after step 3", "Put it in Konkani in Roman letters." Check it again after each change.
6. Share it (below).

**Builders:** you can also give Claude one of the example files from [examples/pages/](../examples/pages/) in the owner's own chat and say "Make a page like this one, with these steps: ...". The examples hold made-up "Sample" businesses only.

## (a) Staff checklist with daily tick boxes

**Prompt to copy:**

```
Make a small, phone-first web page: a daily checklist for my staff at my [kind of business].
Sections and steps (job steps only, no names):
Opening: [step]; [step]; [step]
During the day: [step]; [step]
Closing: [step]; [step]; [step]

Requirements:
- Each step is a large tick box with its text as the label. Every tap target at least 44px tall.
- Show "X of Y done" at the top, and a "Start again" button that asks before clearing.
- Remember ticks only on this phone (localStorage, inside try/catch). Clear them automatically when the date changes. If the phone can't save, still work and show a short note.
- Light and dark themes that follow the phone. Readable at 360px wide. No horizontal scrolling.
- Self-contained: no outside scripts, fonts, images or links. No forms. Nothing is ever sent anywhere.
- A short note at the bottom: ticks stay on this phone, clear each day, and the page can't show who did what.
- Never add names, phone numbers or money amounts.
```

**Check before sharing:**
- Every step is right, in the order the work happens. A staff member who reads the language well has read it.
- Tick two boxes, close the page, open it again: the ticks are still there. (In some apps they may not be; the page should say so.)
- "Start again" asks first, then clears.
- No names anywhere. Cash steps say what to do ("count the till, write it in the book"), never amounts.

## (b) Quote worksheet

**Prompt to copy:**

```
Make a small, phone-first web page: a quote worksheet for my [kind of business].
- Each line has: what (the work or product), how many (defaults to 1 if empty), and price for one in Rs.
- Show each line's total, a "Total before tax" and a line "Tax: [blank: ask your accountant]". Don't calculate any tax or discount.
- Buttons: "Add an item", "Remove" on each line, "Clear all" (asks first), and "Copy as text" that copies the lines and total so I can paste them into a message. If copying is blocked, show the text selected so I can copy it myself.
- Add up money exactly (work in paise), and show amounts like Rs 9,751.50. Show a short error if a box has something that isn't a number.
- Save nothing: closing the page clears it. No localStorage.
- Labels on every box, tap targets at least 44px, light and dark themes, readable at 360px wide.
- Self-contained: no outside scripts, fonts or links. No forms. Nothing is ever sent anywhere.
- A note at the top: "Your own prices only. No customer names."
```

**Check before sharing:**
- Type two lines you know the answer to (for example 2 x 4,500 and 3 x 250.50) and check the total yourself (Rs 9,751.50).
- Type a letter in a price box: it shows an error and adds nothing.
- Close and reopen: everything is gone. That's correct.
- Copy as text, paste into "Message yourself", and read it. Fill the tax line with your accountant's answer before you send a quote.

## (c) Today's jobs board

**Prompt to copy:**

```
Make a small, phone-first web page: today's jobs board for my [kind of business].
Job types (for a dropdown): [job type]; [job type]; [job type]
Today's jobs (time and job type only): [9:00 job type]; [11:30 job type]; [2:00 pm job type]

Requirements:
- Show today's date at the top, then the jobs sorted by time, each with a large "done" tick box. Mark the next job not yet done as "Next". Show "X of Y done".
- An "Add a job" area with a time picker and the job-type dropdown only (no free text). Added jobs show on this phone only and are not saved.
- Remember ticks for the listed jobs only on this phone (localStorage, inside try/catch), cleared when the date changes. If the phone can't save, still work and show a short note.
- Tap targets at least 44px, light and dark themes, readable at 360px wide, nothing spilling off the screen.
- Self-contained: no outside scripts, fonts or links. No forms. Nothing is ever sent anywhere.
- Never show names, phone numbers, addresses or payments. A note at the bottom says so.
```

**Check before sharing:**
- Times and job types are right, and sorted.
- No names, house numbers, addresses or phone numbers, not even inside a job type. "2BHK deep clean" is fine; "deep clean at a named house" is not.
- Tick one, close, reopen: the tick is still there. Add a job, close, reopen: it's gone. That's correct.
- To change tomorrow's jobs, ask Claude in the same chat: "Replace today's jobs with: [times and job types]." Share again (below) and check the link shows the new list.

## Share the link with staff

1. On the page, look for **Publish** or **Share** (as of October 2026, menu names may change). Pages start private. Turn on link sharing only when the page is ready.
2. Copy the link. Open it yourself in a private browser window, or on another phone, to see what staff will see.
3. Send the link to your staff WhatsApp group, and pin the message. Never post it publicly; anyone with the link can open the page.
4. After a change, publish again and check the link shows the new version.
5. To stop sharing, turn link sharing off or delete the page.

Each staff member's ticks stay on their own phone. That's on purpose.

## What these pages won't do

- Keep records, bookings, invoices or money owed. Use your accounts book or software, with your accountant.
- Share ticks between phones, or show who did a job.
- Send reminders or messages. For reminders to yourself, see [NO-AI-SETUPS.md](NO-AI-SETUPS.md).

More levels and their limits: [SOLUTION-TYPES.md](SOLUTION-TYPES.md).

Free to use and adapt (CC0).
