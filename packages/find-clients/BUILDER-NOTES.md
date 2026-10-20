# Find new clients: builder notes

For a volunteer sitting with an owner at a table. Aim: the owner leaves with 2 or 3 clear customer types, search phrases they have already tried once, a lead sheet started in their own account, and one first message ready to send.

## Before you sit down

- Open https://jfk-cil.github.io/small-business-ai-helpers/find-clients/ on your own phone, ready to demo.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner.
- Be ready to say no, kindly, to lists, scraping and bulk WhatsApp. Owners often ask.
- The owner uses their own phone, their own sheet and their own AI account. Not yours.

## 20-minute table script

| Time | What you do |
|---|---|
| 0:00 to 2:00 | Say what it is: "It turns your best customers into a clear picture of who to look for, where, and what to say. You do the searching and you send every message." Ask what they sell and who their best customers are, as types. If you want to take notes or record, say so out loud and ask first. Only go ahead on a clear yes. |
| 2:00 to 5:00 | Demo on your phone with the made-up example below. Show step 1 (types) and a few search phrases from step 2. |
| 5:00 to 8:00 | The owner opens the page and answers the 4 questions. "Best customers" is the key answer: types, not names. |
| 8:00 to 12:00 | Owner copies the helper, opens their AI, pastes, sends, types "go". Read the customer types together. Does the owner recognize them? Ask for changes if not. |
| 12:00 to 15:00 | Step 2: the owner tries 2 search phrases live on Google Maps or Instagram. Talk about what they find. Real businesses come from their search, not from the AI. |
| 15:00 to 18:00 | Start the lead sheet in the Google Sheets app with the column names from the playbook. Add 2 businesses the owner just found, each with one true thing. Then ask the helper for step 4: one first message. |
| 18:00 to 20:00 | Agree one move for this week (for example: 5 first messages by Friday). Check the AI chat has no names, numbers or emails; if it does, delete that chat together. |

## Demo with a made-up example

Answers to type on your phone:
- Offer: "Social media management for cafés and homestays"
- Best customers: "A new café, a 10-room homestay, a yoga school"
- Area: "North Goa"
- Channel: "Email and in person"

What to point out:
- Step 1 gives types with a need ("new cafés that need regular posts before the season"), not names.
- Step 2 gives search phrases with the area in them. The owner types them; the helper never lists businesses or contacts.
- It waits for "ok" before each next step.
- The first message is short, honest, has no invented results, and is easy to say no to.

## Common snags

- **Wrong language.** Change the language on the page and make the helper again, or type "Write to me in Hindi" in the chat. Messages to businesses can be in whatever language the owner uses with them. Translations are drafts; check with someone who reads it well.
- **The owner pastes names, numbers or a list.** Stop. Delete that chat (three dots > Delete). Lists stay in the owner's own sheet. Describe one business or one inquiry at a time, without contact details.
- **"Can it give me a list of businesses with numbers?"** No. It names kinds of businesses and where to search. Explain why: lists go out of date, people on them never agreed, and bulk messages get numbers blocked.
- **The AI makes claims** ("we've grown 50 brands", "guaranteed results"). The helper tells it not to. If a draft still does, the owner removes it. Proof comes only from the owner's real work.
- **Owner wants to WhatsApp everyone.** First contact goes by email, a contact form, a business page or in person, one business at a time. Once someone says yes to hearing more, WhatsApp is fine.
- **The lead checker and fairness.** If an owner wants to filter people by religion, caste, community, gender, age, language or where they're from, the full version refuses and checks only the job. Back it up.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turning a working helper into the owner's own Skill (laptop)

Only on the owner's laptop and the owner's own Claude account, on a paid plan with code execution turned on (Settings > Capabilities).

Easiest: download the four Skills from the package page (target-customer-finder, outreach-email-writer, lead-qualifier, client-onboarding-writer) and upload each in Settings > Capabilities > Skills.

To make a Skill that already knows the owner's business:
1. Make a folder with a short lowercase name, for example `my-client-finder`.
2. Inside it, make a text file called `SKILL.md` that starts like this:
   ```
   ---
   name: my-client-finder
   description: Helps me find and contact new clients for my social media service for cafés and homestays in North Goa. Use when I ask who to look for, for search phrases, or for a first message.
   ---
   ```
3. Under that, paste the helper text from the phone page, the customer types the owner agreed on, and their fit rules (smallest job, areas, notice). No client names, emails, phone numbers or passwords.
4. Zip the folder (the folder itself goes inside the zip) and upload it in Settings > Capabilities > Skills.
5. Test it in a new chat by typing "go".

You can also paste the helper into a Claude chat and ask Claude to turn it into a Skill; with code execution on, it can make the zip for the owner to download.

## Going further (builder projects)

Be clear with the owner about size and cost before you start any of these.

- **Lead sheet formulas** (Google Sheets, owner's account). Columns A to I: Business, Type, Where I found it, One true thing, Last message date, Step, Next date, Status, Notes. Days to wait in L1 (the owner's number).
  - Next date, G2 (copy down): `=IF(OR(E2="",H2<>"Waiting",F2>=3),"",E2+$L$1)`
  - Due: select columns A to I, custom formula `=AND($G1<>"",$G1<=TODAY(),$H1="Waiting")`, orange fill.
  - Dropdowns: Step (1, 2, 3), Status (Waiting, Replied, Meeting, Yes, No thanks).
  - Weekly count of replies: `=COUNTIF(H2:H,"Replied")+COUNTIF(H2:H,"Meeting")+COUNTIF(H2:H,"Yes")`
- **Email templates.** Gmail templates on a computer (Settings > Advanced > Templates) for each first message and follow-up. Gmail's Schedule send can time follow-ups, but it does not cancel if the business replies first.
- **A one-page work sample.** A Google Doc or PDF with 2 or 3 real examples of the owner's work that they have permission to show. Nothing invented.
- **Getting found.** If businesses search for the owner and find nothing, the [Get found on Google](../get-found-on-google/) package helps with the Google Business Profile.
- **Never build** scrapers, auto-follow or auto-DM tools, or anything that buys or copies contact lists. They break trust, get accounts blocked, and may break the law.

## Do not

- Put the owner's data in your own accounts. No client lists, emails or numbers in your Claude, your sheets or your phone.
- Record or photograph anything without saying so out loud first and hearing a yes.
- Post the owner's name, business, phone, screenshots or client names anywhere public, including GitHub issues and social media.
- Ask for or touch the owner's passwords or OTPs. They log in themselves.
- Introduce the owner to your own contacts in a way that shares their details without asking first.
- Promise results.
