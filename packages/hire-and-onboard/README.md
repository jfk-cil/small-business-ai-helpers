# Hire and welcome staff

Job posts that reach the right people, fewer drop-offs during sign-up, and a calm first week.

## The problem

A home healthcare service needs skilled people, such as nurses and attendants, to visit patients and elders who cannot leave home. The path to joining is meant to be simple. People find the service, get in touch, then sign up. In practice the path breaks along the way, and too few people reach out or finish signing up. The owner wants it to run on its own. Many small businesses that rely on cleaners, cooks, drivers, tutors or therapists face the same gap between "interested" and "ready for the first shift".

## What you get

- **Fix my hiring flow:** your hiring steps as named stages, the likely reason people drop off at each, 1 or 2 fixes for each, and which message to fix first, already drafted.
- **A recruitment kit for one role:** a job post, a WhatsApp version under 500 characters, short messages to places that train or gather these people, and kinds of places to try.
- **Applicant replies:** quick replies to the questions applicants ask most (pay, hours, area, what to bring, how sign-up works), and a "finish your sign-up" reminder.
- **A calm first week:** a Day 0, Day 1 and Week 1 welcome checklist, three welcome messages, and a list of documents to check in person.
- **Step-by-step guides** for the daily work, so a new person knows how you do things on day one.

Pay and hours stay as [blank] unless you give them. Nothing is made up.

## Use it in 2 minutes on your phone

Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/hire-and-onboard/

1. Answer four short questions: the roles, how people find you and join today, where they drop off (counts only, no names), and what a new person needs in week one. Every question is optional.
2. Tap **Make my helper**, then **Copy helper**.
3. Open Claude, or the AI you already use, start a new chat, paste the helper and send it.
4. Type "go". It starts with your hiring steps and where people drop off. Then name a role for the job post.

If you open the page inside Claude, a **Try it here** box lets you run it on the page itself. It runs on your own Claude account. This page saves nothing.

Send the helper to yourself on WhatsApp ("Message yourself") so you can copy it again any day.

## Install the full version

The full version knows more about fair hiring questions and health roles, and checks the length of every message. It comes as two Skills.

**Claude on the web or desktop app** (paid plan, code execution turned on)

Download each Skill:

- [staff-hiring-and-onboarding.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/staff-hiring-and-onboarding.zip)
- [sop-and-checklist-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/sop-and-checklist-writer.zip)

Then in Claude open **Settings**, then **Capabilities**, then **Skills**, and upload each zip. Start a new chat and say "People message us but don't finish registering."

**Claude Code**

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install hire-and-onboard@small-business-ai-helpers
```

**Cowork**

Open **Customize**, then **Plugins**, then **Add marketplace**. Enter `jfk-cil/small-business-ai-helpers`, then install **hire-and-onboard**.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| staff-hiring-and-onboarding | Three jobs: maps your hiring flow and where people drop off; writes a recruitment kit for one role; writes a first-week checklist, welcome messages and an in-person document check. | "People contact us but don't register." "Write a job post for an attendant." "Someone new starts Monday." |
| sop-and-checklist-writer | Turns how you do a job into numbered steps a new person can follow, and a checklist to print. | "Write the steps for a first home visit." "Make a checklist for the start of each shift." |

## Limits

- **Drafts only.** It cannot send messages, post jobs, or run a WhatsApp bot for you. You check everything and send or post it yourself.
- **A person decides who to hire.** It never ranks, scores, shortlists, compares or rejects people, and it never writes rules that turn people away automatically.
- **Fair, job-related questions only.** It will not ask about or filter on religion, caste, marriage, pregnancy, family plans, age, gender, looks or where someone is from.
- **No legal answers.** It does not decide which registrations, licenses or checks a role needs, or what a contract should say. Check with a qualified person.
- **No clinical steps.** How to give an injection, collect a sample or move a patient comes from a qualified person on your team, not from AI.
- **Automatic is a bigger job.** An automatic WhatsApp flow needs the WhatsApp Business Platform through an approved provider, people's opt-in and approved message templates. That is a builder project. The helper shows the manual setup you can use today: labels, quick replies, a greeting message and a daily reminder.
- **No promises.** It cannot promise how many people will apply, reply or finish signing up.
- **Free and paid plans.** The phone helper works on any Claude plan, including free, and in ChatGPT or Gemini too. Uploading Skills needs a paid Claude plan with code execution turned on.

## Privacy

Never type these into any AI chat, this one included:

- Applicants' or staff names, phone numbers, CVs or photos (write Applicant 1, Applicant 2)
- Applicants' documents of any kind: ID, certificates, police verification
- Aadhaar, PAN or passport numbers
- Registration numbers with any council or body
- Patients' or customers' names, addresses or health details
- Staff ID numbers and wages
- Bank, UPI and card details
- Family members' details
- Passwords and OTPs

Counts are fine ("40 messaged, 12 replied"); names are not. Check documents in person, with the originals. Never ask anyone to send ID, certificates or registration numbers on WhatsApp. If you paste something by mistake, stop, delete that chat, and type it again with a [blank].

## Tested

Each Skill has behavior cases with made-up businesses in [`evals/`](../../evals/) at the repo root: `evals/testbank/SHO.json` (staff-hiring-and-onboarding) and `evals/testbank/SOP.json` (sop-and-checklist-writer). The checker is in `evals/harness/`. Results are in [`evals/RESULTS.md`](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you check and send everything yourself. A person decides who to hire.
