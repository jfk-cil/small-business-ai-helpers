# Staff checklists

Clear opening, closing and daily checklists for each role, so the work runs the same way whether you are there or not.

## The problem

A café owner has staff in a few different roles. The owner wants each person's tasks clearly set out, wants them engaged and growing in the job, and wants the café to run well on the days the owner is away. Right now the way each job is done lives in the owner's head. Each person does it a little differently, and small things slip: a fridge not checked, a counter not closed properly, stock not noted. Many small businesses with a few staff are in the same place.

## What you get

- One checklist per role and shift (opening, during the day, closing), in short numbered steps, in the order the work happens.
- The things that go wrong when you are away, placed near the top.
- What "done" looks like at the end of each shift.
- A short version (5 to 8 lines) to print and stick on the wall, with a Date line and an Initials line.
- A weekly 15-minute check: a quick look at the checklists with your team to fix steps that don't work.
- If you want it: a simple Google Sheet to note daily tasks, stock or deliveries, with setup steps for your phone.

## Use it in 2 minutes on your phone

Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/staff-checklists/

1. Answer four short questions: your business, your roles, what goes wrong when you are away, and your hours. Every question is optional.
2. Tap **Make my helper**, then **Copy helper**.
3. Open Claude, or the AI you already use, start a new chat, paste the helper and send it.
4. Name a role and a shift, for example "counter, closing". It writes the steps and a wall version.

If you open the page inside Claude, a **Try it here** box lets you run it on the page itself. It runs on your own Claude account. This page saves nothing.

Send the helper to yourself on WhatsApp ("Message yourself") so you can copy it again any day.

## Install the full version

The full version also writes step-by-step guides for new staff, guest welcome guides and short intake forms, and designs tracker sheets with formulas and color rules. It comes as two Skills.

**Claude on the web or desktop app** (paid plan, code execution turned on)

Download each Skill:

- [sop-and-checklist-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/sop-and-checklist-writer.zip)
- [tracker-sheet-builder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/tracker-sheet-builder.zip)

Then in Claude open **Settings**, then **Capabilities**, then **Skills**, and upload each zip. Start a new chat and say "Write a closing checklist for my café counter."

**Claude Code**

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install staff-checklists@small-business-ai-helpers
```

**Cowork**

Open **Customize**, then **Plugins**, then **Add marketplace**. Enter `jfk-cil/small-business-ai-helpers`, then install **staff-checklists**.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| sop-and-checklist-writer | Turns how you do a job into numbered steps for a new person, a checklist to print and tick, a guest welcome guide or a short intake form. | "Write the opening steps for the kitchen." "Make a closing checklist for the wall." |
| tracker-sheet-builder | Designs one simple Google Sheet (stock, orders, deliveries, daily tasks) with sample rows, formulas, color rules and 5 phone setup steps. | "We keep running out of butter." "A daily job sheet for my staff." |

## Limits

- **Drafts only.** You check every step, fix what's wrong, and print or share it yourself.
- **Tasks, not people.** Checklists track jobs. Initials and a date only. It will not add scores, ratings, warnings or "who forgot", and it will not help judge, watch or discipline anyone.
- **No money amounts.** Cash steps are steps only ("count the till, write it in the book"). It never asks for or writes money figures, and it will not build a cash book, sales ledger, payroll or tax sheet.
- **No safety or legal rules of its own.** It does not write food safety, fire or licensing rules. Where a step involves gas, electricity, hot liquids, knives or cleaning chemicals, it marks it so you can add how to do it safely. Check with a qualified person.
- **Free and paid plans.** The phone helper works on any Claude plan, including free, and in ChatGPT or Gemini too. Uploading Skills needs a paid Claude plan with code execution turned on.

## Privacy

Never type these into any AI chat, this one included:

- Staff names, phone numbers, ID numbers or wages (write "kitchen" or "morning helper", not a name)
- Customers' or guests' names and phone numbers
- Aadhaar, PAN or passport details
- Bank, UPI and card details
- Cash totals, sales figures or till counts
- Passwords and OTPs, including wifi passwords
- Health information
- Family members' details
- Photos of people

Your real lists stay in your own sheet or notebook. If you paste something by mistake, stop, delete that chat, and type it again with a [blank].

## Tested

Each Skill has behavior cases with made-up businesses in [`evals/`](../../evals/) at the repo root: `evals/testbank/SOP.json` (sop-and-checklist-writer) and `evals/testbank/TSB.json` (tracker-sheet-builder). The checker is in `evals/harness/`. Results are in [`evals/RESULTS.md`](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you check and share everything yourself.
