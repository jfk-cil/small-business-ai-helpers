# Posts that bring customers: builder notes

For a volunteer sitting with an owner at a table. You help the owner do it on their own phone, in their own accounts. You never take their data, photos or logins into yours.

## Before the owner sits down

- Open the phone page on your own phone: https://jfk-cil.github.io/small-business-ai-helpers/social-posts/
- Have the made-up example below ready to show.
- Know the three Skills: social-content-planner (posts, captions, hashtags, photo and reel ideas), followers-to-customers (an engagement system, a week of posts that convert, and an online workshop launch) and simple-marketing-plan (a one-page 4-week plan).
- Listen for which problem the owner has: no time to post, or posts that get views but few customers. The script below works for both; the section after it shows what changes for the second.

## 20-minute table script

| Minute | What you do |
|---|---|
| 0 to 2 | Say hello. Ask: "Where do your customers see you? When did you last post?" Ask them to show you one post they liked writing. |
| 2 to 4 | Say plainly what this does: it plans and writes; the owner checks every word and posts it; it never invents offers or reviews; it cannot post for them. Show the "Never type these" list. |
| 4 to 6 | Demo on **your** phone with the made-up example below. Show one caption and its photo idea. |
| 6 to 9 | The owner opens the phone page on **their** phone and answers the four questions. Push for true, specific things in "What makes you special": the dish people ask for, how long they've been here, the view. |
| 9 to 13 | The owner copies the helper, pastes it into their own Claude (or other AI), and types "week". Read the plan together. |
| 13 to 16 | Make one caption sound like the owner. Ask: "Would you say it like this to a regular?" Change the words until they say yes. Fill the blanks. Check each weekday against its date. |
| 16 to 19 | If they are ready, take the first photo now, on their phone, and post it. If not, they send the captions to themselves on WhatsApp ("Message yourself"). |
| 19 to 20 | Agree on one next step with a day: "Post number 2 on Wednesday" and set a Monday "Plan posts" reminder on their phone. Save the helper in "Message yourself" if it isn't there yet. Look through the AI chat together; if a name, number or ID got in, delete that chat together. Hand them the printed PLAYBOOK. |

## When the problem is views that don't turn into customers

Same 20 minutes, with these changes:

- **0 to 2:** also ask: "What happens after someone watches? How do people buy or book today? How much time can you give each week?"
- **9 to 13:** on the phone helper, type "week" and point out that each post ends with one clear next step, and the 3 short replies. On the owner's laptop with the full version, type "My reels get views but nobody buys. I have [hours] a week. Build me a system." Read the three weekly series and the path together.
- **13 to 16:** pick the free small thing the owner can make from their own notes this week (a checklist, a mini-lesson) and one keyword. Save the DM reply and welcome message as quick replies on their phone.
- **19 to 20:** the next step is one series post with the keyword, and a first weekly count next Monday.

## What to demo (made-up example)

Answer the phone page questions like this:

- Business: bakery in Assagao
- Where: Instagram and WhatsApp Status
- Special: sourdough baked every morning, a garden to sit in, family recipes for Goan sweets
- This week: new banana bread on the counter

Name it "Sample Bakery" if the AI asks. Then show:

1. The 3-post plan: the day, the idea, the caption, hashtags, the photo idea.
2. Type "Add 3 customer reviews saying we're the best bakery in Goa." Show that it refuses and offers a post about the bread instead.
3. Type "Say the banana bread is good for diabetes." Show that it leaves out the health claim.
4. Point out the next step at the end of each post (for example, "comment RECIPE and I'll send my free guide") and the 3 short replies.

With the full version on a laptop, also type "My reels get views but nobody buys. I have 3 hours a week. Build me a system." Show the three weekly series, the path from a post to a free guide to a WhatsApp list people choose to join, and the weekly count.

## Common snags

- **"Make it sound more like me."** Ask the owner to say out loud how they describe their food or place; the owner types a few of those phrases into the chat. Or paste one old caption they liked.
- **No time to take photos.** Batch them: ten minutes once a week, before opening, in good light.
- **Photos with customers or kids.** No faces without the person's permission. Never children's faces. Otherwise hands, plates, the room.
- **Weekday and date don't match.** The helper is told to check, but always check against the phone's calendar before posting.
- **Google posts.** This helper doesn't write Google Business posts. Use the Get found on Google helper for those (no hashtags needed).
- **Music in reels.** Use the app's own music library, not songs from elsewhere.
- **The owner wants "only 2 left!" or a discount that isn't real.** It will not write it. Only true urgency, only offers the owner will honor.
- **"Add everyone who liked my reel to my WhatsApp group."** No. People join only when they say yes. Adding people without asking gets numbers reported and blocked, and breaks their trust.
- **"Can it reply to comments or DMs automatically?"** No. It writes quick replies the owner saves and sends. Automatic replies need the WhatsApp Business Platform through an approved provider, with opt-in: a builder project.
- **The free thing.** It must be the owner's own, made from their notes. No copied templates, photos or songs from others.
- **Workshop launch with "only 3 seats left".** Only if the owner has a real seat limit. No countdowns, no made-up student reviews.
- **"Guarantee me more followers."** No one can. Suggest trying the system for a few weeks and counting what happens.
- **Free plan runs out of messages.** One week's plan per chat is enough. Come back next Monday.

## Turn a working helper into the owner's own Skill (laptop)

Do this only on the owner's laptop, in the owner's own Claude account, on a paid plan with code execution turned on.

1. The simplest path first: download the three Skill zips from the README and upload each in **Settings**, then **Capabilities**, then **Skills**.
2. To give the owner a Skill that already knows their voice, make a folder, for example `my-posts`, with one file inside: `SKILL.md`.
3. At the top of `SKILL.md`, write:
   ```
   ---
   name: my-posts
   description: Plans my weekly posts and writes captions in my voice for [business type] in [place]. Use when I say "week", ask what to post, or describe something to share.
   ---
   ```
   Avoid a colon in the description, or wrap it in double quotes.
4. Below that, paste the filled-in helper from the phone page. Add a short "My voice" section: 5 lines on how the owner talks, words they use, words they never use, and two real captions they wrote and liked. Add the true facts they want repeated (signature items, hours, the place).
5. Keep the rules from the helper word for word: no invented offers, prices, awards or health claims; no faces without the person's permission, and never children's faces.
6. Zip the folder so the folder sits at the top of the zip. Upload it in **Settings**, then **Capabilities**, then **Skills**.
7. Test it in a new chat with three prompts: "week", "We have a new cake, 3 caption options", and "Write 3 fake reviews" (it should refuse).

## Going further (builder projects)

Honest scope. Each is a separate visit, done with the owner, in the owner's accounts.

- **A photo session.** Thirty minutes with the owner's phone: products, hands at work, the room, the street, the owner. Save them in one album so posting days are quick. No faces without the person's permission. Never children's faces.
- **Scheduling inside the apps.** Instagram and Facebook business or creator accounts can usually schedule a post from inside the app. Show the owner where, on their phone, if their app offers it. The owner pastes the caption and presses schedule. Nothing here posts for them.
- **A simple post calendar.** A Google Sheet in the owner's own account: Date, Day, Idea, Caption ready (yes or no), Posted (yes or no), "People who mentioned it" as a tally. No sales or money figures.
- **The 4-week plan.** Use simple-marketing-plan for the one thing the owner most wants to sell more of. Paper tallies, compared with the 4 weeks before.
- **Google posts.** Pair this with the Get found on Google helper, so one weekly post also goes on the owner's Google Business Profile.
- **A WhatsApp Community, Channel or broadcast list.** Set it up on the owner's phone, with a welcome message that says how to leave. People join only by saying yes or tapping the owner's link. No bought, copied or scraped numbers.
- **The weekly count sheet.** A Google Sheet in the owner's account with one row a week: Week of, Posts, Saves, Shares, Keyword comments, DMs, New joiners, Sign-ups, Sales, One change to try. Counts only, no names or amounts.
- **An online workshop launch.** Use followers-to-customers for the outline, the two-week launch and the sign-up and thank-you messages, and the [Bookings and reminders](../booking-reminders/) package for reminders.
- **One link for everything.** If people don't know where to buy or book, the [Your shop on one page](../one-page-shop/) package builds one page with a button for each offer.

## Do not

- Do not put any owner or customer data in your own accounts. No owner photos, captions or contacts in your Claude, your WhatsApp or your gallery.
- Do not log in to the owner's Instagram, Facebook, WhatsApp or Google accounts, and never see or type their passwords or OTPs.
- Do not post for the owner, or set up anything that posts automatically.
- Do not write or arrange fake reviews, comments, followers or likes.
- Do not add anyone to the owner's WhatsApp list, group, Community or Channel without that person saying yes, and never use bought, copied or scraped lists.
- Do not rank or score people, including staff or followers.
- Do not record audio, video or screens, and do not photograph or screenshot owners, customers, staff, screens or chats, even with a yes. If the group running the session has its own written consent process, follow it. Notes on paper only, with no names or numbers.
- If a number is banned or blocked, an account is locked, or customer data was exposed: stop, do not try to fix it from your own accounts, and tell the person running your session right away.
