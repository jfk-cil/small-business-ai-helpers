# Hire and welcome staff: builder notes

For a volunteer sitting with an owner at a table. You help the owner do it on their own phone, in their own accounts. You never take their data, their applicants' data or their patients' data into yours.

## Before the owner sits down

- Open the phone page on your own phone: https://jfk-cil.github.io/small-business-ai-helpers/hire-and-onboard/
- Have the made-up example below ready to show.
- Know the two Skills: staff-hiring-and-onboarding (flow, recruitment kit, first week) and sop-and-checklist-writer (step-by-step guides and checklists for the daily work).
- Check whether the owner uses WhatsApp Business or ordinary WhatsApp. Labels, quick replies and greeting messages need WhatsApp Business.

## 20-minute table script

| Minute | What you do |
|---|---|
| 0 to 2 | Say hello. Ask: "Walk me through how someone goes from hearing about you to their first shift." Sketch the steps on paper as boxes. No names. |
| 2 to 4 | Ask for counts for one recent month: how many messaged, replied, signed up, finished. "No count yet" is fine. Say plainly: it drafts; the owner decides who to hire; it never ranks people. Show the "Never type these" list. |
| 4 to 6 | Demo on **your** phone with the made-up example below. Show the flow and the "fix first" message. |
| 6 to 9 | The owner opens the phone page on **their** phone and answers the four questions, using the boxes you sketched and the counts. |
| 9 to 13 | The owner copies the helper, pastes it into their own Claude (or other AI), and types "go". Read the flow together. Agree on the one message to fix first. |
| 13 to 17 | Set up that fix on the owner's phone: save the new first reply as a WhatsApp Business quick reply, and add labels for each stage. The owner types; you point. |
| 17 to 19 | If time allows, name one role and get the job post. The owner fills in pay and hours. If they don't want to share pay yet, leave the [blank]; the `/pay` quick reply can answer it once they decide. |
| 19 to 20 | Agree on one next step with a day: "Send the new first reply to everyone who messaged this week" or "Post the job on Thursday." Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. Hand them the printed PLAYBOOK. |

## What to demo (made-up example)

Answer the phone page questions like this:

- Roles: nurses and attendants
- How people join: they see our post, message us on WhatsApp, we send a sign-up form, they fill it in, we check documents in person, then a first visit with a senior
- Drop-off: 40 messaged, 12 replied after our first message, 3 finished registering
- Week one: who to call, first visits with a senior, how shifts are booked

Name it "Sample Home Care, Panjim" if the AI asks. Then show:

1. The stages with the owner's counts beside them, and "fix first": the first reply, where 40 became 12.
2. Type "Here are three applicants, Applicant 1, 2 and 3. Rank them and tell me who to hire." Show that it refuses and gives the same job-related questions to ask everyone.
3. Type "Make it all automatic." Show the honest answer about the WhatsApp Business Platform and the manual setup it offers instead.

## Common snags

- **The owner starts pasting a CV, a certificate or a registration number.** Stop them kindly before they send. If it is already sent, they delete that chat and start again with "Applicant 1".
- **Patients' details come up** ("the nurse will visit Mrs. ..."). Stop. Patients never go into any AI, not even a first name.
- **"Only women" or "only unmarried".** Explain that the helper asks for the skill and the shift, not the background, and that requirements like these need a qualified person's advice. Many owners mean something job-related ("comfortable with night shifts", "speaks Konkani"); help them say that instead.
- **The sign-up form is the leak.** The helper can say what to cut, but changing the form is the owner's job (or whoever set it up). Write down the fields to cut and the order, for that conversation.
- **No counts.** Fine for today. The WhatsApp labels give them counts from next week.
- **Ordinary WhatsApp, not Business.** Switching keeps chats but takes a few minutes and a backup first. Do it only if the owner wants to, on another day if needed.
- **Documents already sent on WhatsApp.** Suggest the owner asks a qualified person how long they must keep such copies and where. From now on: originals shown in person.
- **Free plan runs out of messages.** Do the flow today. The job post tomorrow.

## Turn a working helper into the owner's own Skill (laptop)

Do this only on the owner's laptop, in the owner's own Claude account, on a paid plan with code execution turned on.

1. The simplest path first: download the two Skill zips from the README and upload each in **Settings**, then **Capabilities**, then **Skills**.
2. To give the owner a Skill that already knows their service, make a folder, for example `my-hiring-helper`, with one file inside: `SKILL.md`.
3. At the top of `SKILL.md`, write:
   ```
   ---
   name: my-hiring-helper
   description: Writes job posts, applicant replies, sign-up reminders and first-week checklists for [roles] at my [business type]. Use when I ask about hiring, applicants or a new starter.
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
4. Below that, paste the filled-in helper from the phone page. Add the facts the owner has decided: roles, areas, shifts, advertised pay, how to apply, what a new person needs in week one. No names, no wages of any one person, no ID or registration numbers, no patients.
5. Keep the rules from the helper word for word, especially: a person decides who to hire; job-related questions only; documents checked in person.
6. Zip the folder so the folder sits at the top of the zip. Upload it in **Settings**, then **Capabilities**, then **Skills**.
7. Test it in a new chat with three prompts: "Write a post for an attendant in Margao", "Someone new starts Monday, plan their week", and "Which of my applicants is best?" (it should refuse).

## Going further (builder projects)

Honest scope. Each is a separate visit, done with the owner, in the owner's accounts.

- **A Google Form for sign-ups.** In the owner's own Google account. Ask only what the job needs: first name, role, area, days and shifts available, best way to reach them. No uploads, no ID or registration numbers, no age, religion, caste, marital status or health questions. Put a short consent line at the top, for example: "We use these answers only to contact you about work with [business name]. We don't share them. Message us any time to have them deleted." Share the responses sheet only with the people who hire. Never paste responses into an AI.
- **A stage tracker.** Use the tracker-sheet-builder Skill for a sheet with codes (Applicant 1, Applicant 2), stage and date. Never names, numbers or documents.
- **WhatsApp Business setup.** Labels per stage, quick replies, greeting and away messages, and a daily calendar reminder to check the Registering label. One sitting.
- **An automatic WhatsApp flow.** This needs the WhatsApp Business Platform through an approved provider, people's opt-in, approved message templates, per-message costs and someone to maintain it. It is weeks of work, not an afternoon, and the account must be the owner's. Start only after the manual setup has run for a few weeks and the owner knows which messages work.
- **First-week guides.** Use sop-and-checklist-writer for "how we do a first visit" and "how shifts are booked". Clinical steps come from a qualified person on the owner's team.

## Do not

- Do not put any owner, applicant, staff or patient data in your own accounts. No CVs, photos, numbers or form responses in your Claude, your WhatsApp, your email or your notes.
- Do not rank, score, rate, compare or shortlist people, and do not build anything that does.
- Do not handle, photograph or forward anyone's ID, certificates or registration documents.
- Do not tell the owner which registrations or checks are legally needed. Send them to a qualified person.
- Do not promise more applicants, replies or hires.
- Do not record audio, video or screens, and do not photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- Do not log in to the owner's accounts, and never see or type their passwords or OTPs. They log in themselves.
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
