# A sales plan across channels: builder notes

For a volunteer sitting with an owner at a table. Aim: the owner leaves with a channel map they agree with, the first month's weekly steps, a post bank in a phone note, and one first message to a café or shop they chose. You help the owner do it on their own phone, in their own accounts. You never take their data, contacts or logins into yours.

## Before the owner sits down

- Open the phone page on your own phone: https://jfk-cil.github.io/small-business-ai-helpers/sales-plan/
- Have the made-up example below ready to show.
- Have a printed copy of [PLAYBOOK.md](PLAYBOOK.md) for the owner.
- Know the four Skills: channel-sales-plan (the channel map, the month-by-month plan, the post bank, café visits and the monthly check), social-content-planner (captions and photo ideas), customer-message-writer (WhatsApp messages to people who joined) and outreach-email-writer (a longer first email to a business).
- Be ready to say no, kindly, to "guarantee my sales", "say it's healthy", "add everyone in my groups" and "what price should I give cafés?". Owners often ask.

## 20-minute table script

| Minute | What you do |
|---|---|
| 0 to 2 | Say hello. Ask: "How do you sell today, and how do you want to sell? How much time can you give each week?" If you want to take notes, ask out loud first: paper only, with no names or numbers. No photos or recordings. |
| 2 to 4 | Say plainly what this does: it plans small weekly steps across up to three channels, from the owner's own seasons; the owner visits, posts and sends everything; it never promises sales and never invents prices or terms. Show the "Never type these" list. |
| 4 to 6 | Demo on **your** phone with the made-up example below. Show the channel map and Month 1. |
| 6 to 9 | The owner opens the phone page on **their** phone and answers the four questions. Push for their own calendar in the last answer: when tourists come, which festivals and when, the slow months. |
| 9 to 13 | The owner copies the helper, pastes it into their own Claude (or other AI), and types "go". Read the channel map together. Then "ok" for the plan. Ask: "Can you really do these steps in the time you gave?" If not, ask for fewer. |
| 13 to 16 | Type "ok" for the post bank. The owner copies it into a phone note. Pick the first 2 ideas to shoot this week. |
| 16 to 19 | Type "ok" for cafés and shops. The owner picks one café they know, changes the first message into their own words, and fills each [blank] they are sure of. They send it themselves, now or later. |
| 19 to 20 | Agree on one next step with a day: "Send the first message to one café by Friday" or "Make the price list this weekend." Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. Hand them the printed PLAYBOOK. |

## What to demo (made-up example)

Answer the phone page questions like this:

- What and where: home bakery in Aldona, sourdough, banana bread and brownies
- How: supply cafés near the beaches, sell direct on WhatsApp, post on Instagram
- Time: about 3 hours a week
- Coming up: tourists from November to March, Christmas orders in December, a slow monsoon

Name it "Sample Bakehouse, Aldona" if the AI asks. Type "go", then show:

1. The channel map: each channel with its next action and "Have ready". Café prices and delivery days are [blank].
2. Type "ok". Show Month 1 and Month 2, each tied to the owner's own words about the season.
3. Type "Promise my sales will triple and say the brownies are healthy." Show that it makes no promise and leaves the health claim out.
4. Type "What wholesale price and minimum order should I give cafés? And add everyone from my building groups to my list." Show that prices and terms stay [blank], and that it writes a join line people choose instead of adding anyone.

## Common snags

- **"I have no time."** Start with one action per channel a week. A plan the owner keeps beats a big plan they drop.
- **More than three channels.** The helper plans three and puts the rest under "Later". Ask which three bring orders now.
- **No festivals or months given.** It puts them under "To place" with a [blank]. The owner tells it the month, and it becomes that month's theme.
- **"What should I charge cafés?"** The owner's decision. The helper and you leave it [blank]. Wholesale terms: a qualified person. When the owner has decided, the quote helper in the [Reply to customer messages](../customer-replies/) package writes the quote.
- **WhatsApp groups.** Only groups whose rules allow selling, after asking the admin. Never the same post in many groups. Never add people from a group to the owner's list.
- **Health and diet words.** "Healthy", "guilt-free" and "good for diabetics" stay out. Eggless or sugar-free only in the owner's words, and a qualified person checks the label.
- **Sales figures pasted.** The helper won't repeat them. Sales stay in the owner's accounts book. The monthly check counts orders.
- **A café's name in a post.** Only with that café's permission. Ask before tagging.
- **"Can it post and send for me?"** No. It writes; the owner posts and sends. Scheduling inside the apps is a builder project below.
- **Wrong language.** The helper can reply in Hindi, Konkani or Marathi. Someone who reads the language well checks it before it goes out.
- **Credits or free messages run out.** The helper is plain text. Paste the same helper into ChatGPT or Gemini (free) and carry on. It should work there too, though so far it has been tested in Claude only. Only the Skills and Projects stay inside Claude.
- **No "Try it here" box.** That box only appears when the page is opened inside Claude. Copying the helper always works.

## Turn a working helper into the owner's own Skill (laptop)

Do this only on the owner's laptop, in the owner's own Claude account, on a paid plan with code execution turned on.

1. The simplest path first: download the four Skill zips from the README and upload each in **Settings**, then **Capabilities**, then **Skills**.
2. To give the owner a Skill that already knows their channels and seasons, make a folder, for example `my-sales-plan`, with one file inside: `SKILL.md`.
3. At the top of `SKILL.md`, write:
   ```
   ---
   name: my-sales-plan
   description: Keeps my sales plan up to date for my [business type] in [place], selling to cafés, on WhatsApp and through posts. Use when I ask what to do this week, plan next month, or need post ideas or a first message to a café.
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
4. Below that, paste the filled-in helper from the phone page. Then add the channel map and plan the owner agreed on, their seasons and festivals in their own words, and the post bank. No customer or café names or numbers, no prices the owner hasn't made public, and no sales figures.
5. Zip the folder so the folder sits at the top of the zip. Upload it in **Settings**, then **Capabilities**, then **Skills**.
6. Test it in a new chat with three prompts: "What do I do this week?", "Plan next month", and "Guarantee me double sales" (it should refuse).

## Going further (builder projects)

Honest scope. Each is a separate visit, done with the owner, in the owner's accounts.

- **The café kit.** A one-page price list and product card with listing-and-catalog-writer in the [Your shop on one page](../one-page-shop/) or [Get found on Google](../get-found-on-google/) package. Prices and terms come from the owner only.
- **Finding the cafés and shops.** The [Find new clients](../find-clients/) package names the kinds of businesses to approach and the search phrases. The owner searches and chooses; never a bought list.
- **A WhatsApp list people choose to join.** Set up a Community, Channel or broadcast list on the owner's phone, with the join line on the counter card, bags and bio. People join only by saying yes. Labels such as New order, Paid, Delivered.
- **The monthly check sheet.** Use tracker-sheet-builder in the owner's Google account with the columns from the helper. Counts only, no money, no customer or café names.
- **Captions for a month.** Use social-content-planner with the month's ideas from the post bank. The [Posts that bring customers](../social-posts/) package goes further on turning followers into buyers.
- **Scheduling inside the apps.** Instagram and Facebook business or creator accounts can usually schedule a post from inside the app. Show the owner where, on their phone. The owner presses schedule.
- **An automatic WhatsApp bot** is a separate, bigger project: it needs the WhatsApp Business Platform through an approved provider, the customer's opt-in and approved message templates.

## Do not

- Do not put any owner, customer or café data in your own accounts. No contact lists, prices, photos or plans in your Claude, your WhatsApp or your notes.
- Do not send the first message to a café, post or message customers for the owner, or set up anything that posts or sends automatically.
- Do not add anyone to the owner's WhatsApp list, group, Community or Channel without that person saying yes, and never use bought, copied or scraped lists.
- Do not suggest prices, margins, minimum orders or wholesale terms. The owner decides; a qualified person checks terms and labels.
- Do not promise sales, orders or followers.
- Do not record audio, video or screens, and do not photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- Do not log in to the owner's Instagram, Facebook, WhatsApp or Google accounts, and never see or type their passwords or OTPs. They log in themselves.
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
