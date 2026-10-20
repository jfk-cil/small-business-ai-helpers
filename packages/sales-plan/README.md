# A sales plan across channels

One plan for the next few months when you sell in more than one way: to cafés or shops, direct to people on WhatsApp, and through posts. With a bank of post ideas you can reuse.

## The problem

Small food businesses and other makers often sell in three ways at once. They supply cafés or shops, they sell direct to customers who order on WhatsApp, and they post on Instagram or Facebook. Each channel needs something different: samples and a price list for a café, a regular list for WhatsApp, photos and ideas for posts. With baking or making every day, there is no time to plan, so marketing never starts. What the owner wants is a simple plan for the next six months that ties the three together, with weekly steps that fit their time and a store of posts they can come back to.

## What you get

The phone helper works in five steps, one per message, and asks before moving on:

1. **A channel map:** for each channel, who buys, what they buy, the one next action, what you need ready (a price list, samples, a menu card) and how orders come in.
2. **A 6-month plan** (or the months you ask for): a theme for each month from your own seasons and festivals, and weekly actions for each channel that fit your time. Festivals you didn't place go under "To place" with a [blank].
3. **A bank of 12 to 24 post ideas**, grouped by theme, one line each.
4. **For cafés and shops:** a short first message and a plan for a tasting or sample visit.
5. **A monthly check** with simple counts: orders per channel, new business customers, WhatsApp sign-ups and messages from posts. Your target stays yours to fill in.

The full version (Skills) also:
- sizes a weekly rhythm to your hours, and says what to drop first in a busy week;
- gives a monthly refresh for the post bank and a WhatsApp join line for people who choose to join;
- writes captions, hashtags and photo ideas for the posts you pick;
- writes the weekly WhatsApp message to the people on your list;
- writes a longer first email to a café, shop or hotel, with polite follow-ups.

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/sales-plan/
2. Answer 4 short questions: what you sell and where; how you sell or want to sell (up to 3 ways); how much time you can give each week; what's coming up in the next few months. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Type "go" to start with your channel map.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [channel-sales-plan.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/channel-sales-plan.zip)
   - [social-content-planner.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/social-content-planner.zip)
   - [customer-message-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/customer-message-writer.zip)
   - [outreach-email-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/outreach-email-writer.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "I need a six month sales plan: cafés, WhatsApp and Instagram." Then say what you sell and how much time you have.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install sales-plan@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **sales-plan** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [channel-sales-plan](../../skills/channel-sales-plan/SKILL.md) | Builds a 3 to 12 month plan (6 by default) across up to 3 channels: a channel map, monthly themes from your own calendar, a weekly rhythm sized to your time, a post bank with a monthly refresh, a first message and tasting visit plan for cafés and shops, and a monthly check with counts. | "Six month marketing plan." "Sell to cafés and direct on WhatsApp." "A repository of posts." |
| [social-content-planner](../../skills/social-content-planner/SKILL.md) | Plans a week or month of posts with captions, photo and reel ideas, and local hashtags. | "Write captions for these post ideas." "What should I post this week?" |
| [customer-message-writer](../../skills/customer-message-writer/SKILL.md) | Writes short WhatsApp messages for customers who agreed to hear from you: this week's list, new items, reorder reminders and thank-yous. | "Write this week's bake list message." "Message my customers about Christmas orders." |
| [outreach-email-writer](../../skills/outreach-email-writer/SKILL.md) | Writes a short, honest first email to a business you'd like to supply, and polite follow-ups if asked. | "Email a café about supplying them." "They never replied." |

Owner cards (one page each, plain words): [channel-sales-plan](../../skills/channel-sales-plan/OWNER-CARD.md), [social-content-planner](../../skills/social-content-planner/OWNER-CARD.md), [customer-message-writer](../../skills/customer-message-writer/OWNER-CARD.md), [outreach-email-writer](../../skills/outreach-email-writer/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **Drafts only, nothing sent or posted.** It can't post, schedule, send messages or run a bot. You check every word, visit the cafés, post and send everything yourself. Automatic WhatsApp messages need the WhatsApp Business Platform through an approved provider, each customer's opt-in and approved message templates: a separate builder project.
- **People choose to join.** WhatsApp messages go only to people who said yes. It never adds anyone without asking, never uses bought or copied lists, and treats STOP as stop, at once. In other people's groups, post only where the rules allow selling, and ask the admin first.
- **No promised results.** It never says the plan will bring sales, orders or followers. No fake urgency ("only a few left") unless it's true. The monthly check lets you count for yourself.
- **Your seasons, your terms.** Months, festivals and busy seasons come only from you. It never invents or suggests prices, discounts, margins, minimum orders, delivery terms, credit or shelf life. Anything you didn't give stays [blank].
- **No health claims.** It writes about taste, your ingredients and how you make it. No "healthy", "guilt-free" or "good for diabetics".
- **No legal or labeling advice.** Food safety and licensing, food labels, wholesale terms and GST: check with a qualified person.
- **The cafés are yours to pick.** It never names a real business. Tag a café only with its permission.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Customers' names and phone numbers, or your contact list
- Café or shop owners' names and phone numbers (write "the café owner")
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details (the drafts use [your UPI ID])
- Passwords and OTPs, including your Instagram, Facebook or Google login
- Sales or money figures (your public prices are fine)
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

Your real sales stay in your own accounts book. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([CSP.json](../../evals/testbank/CSP.json), [SCP.json](../../evals/testbank/SCP.json), [CMW.json](../../evals/testbank/CMW.json), [OEW.json](../../evals/testbank/OEW.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you check, visit, post and send everything yourself.
