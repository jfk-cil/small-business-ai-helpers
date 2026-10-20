# Posts that bring customers

A week of posts and captions in your own voice, with photo ideas you can shoot yourself.

## The problem

The job owners ask for most often is a post calendar with captions. The reason is familiar to anyone running a café, a homestay, a shop or a studio. You know you should post. Your customers look for you on Instagram, WhatsApp Status, Facebook and Google. But after a full day of work there is no time left to think of what to say, which photo to take, or which hashtags to use. So posting stops for weeks, then starts again in a rush.

## What you get

- A weekly post calendar: the day, the idea in one line, and the kind of post (behind the scenes, how it's made, your place, a tip, a question, and now and then an offer).
- A ready caption for each post, in your voice, each in its own copy box.
- 3 to 5 hashtags per post, at least two tied to your place.
- A photo or short video idea for each post that you can shoot on your phone in a few minutes.
- 3 caption options when you describe one thing you want to share.
- For Google Business posts, use the [Get found on Google](../get-found-on-google/) package.
- A one-page, 4-week plan: one goal, who to reach, what to offer, which channels, small steps each week, and simple counts to see if it worked.

## Use it in 2 minutes on your phone

Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/social-posts/

1. Answer four short questions: your business and where, where you post, what makes you special, and anything happening this week. Every question is optional.
2. Tap **Make my helper**, then **Copy helper**.
3. Open Claude, or the AI you already use, start a new chat, paste the helper and send it.
4. Type "week". It writes a plan for 3 posts (ask for more). Or describe one thing to share and get 3 caption options.

If you open the page inside Claude, a **Try it here** box lets you run it on the page itself. It runs on your own Claude account. This page saves nothing.

Send the helper to yourself on WhatsApp ("Message yourself") so you can copy it again every week.

## Install the full version

The full version also plans a whole month, writes reel ideas shot by shot, and makes a one-page marketing plan. It comes as two Skills.

**Claude on the web or desktop app** (paid plan, code execution turned on)

Download each Skill:

- [social-content-planner.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/social-content-planner.zip)
- [simple-marketing-plan.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/simple-marketing-plan.zip)

Then in Claude open **Settings**, then **Capabilities**, then **Skills**, and upload each zip. Start a new chat and say "What should I post this week?"

**Claude Code**

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install social-posts@small-business-ai-helpers
```

**Cowork**

Open **Customize**, then **Plugins**, then **Add marketplace**. Enter `jfk-cil/small-business-ai-helpers`, then install **social-posts**.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| social-content-planner | Plans a week (3 posts unless you ask for more) or a month (12 posts) with captions, photo and reel ideas, and local hashtags. | "What should I post this week?" "Write captions for my café." "Make a content calendar for November." |
| simple-marketing-plan | Makes a one-page, 4-week plan: one goal, who to reach, what to offer, at most two free channels, weekly steps, and how to tell if it worked. | "How do I sell more?" "These items just sit on the shelf." "Plan a campaign for next month." |

The phone helper writes 5 posts for a week; the full Skill starts at 3 so the plan is one you can keep. Ask either one for more or fewer.

## Limits

- **Drafts only, no auto-posting.** It cannot log in to Instagram, Facebook, WhatsApp or Google, and it cannot post or schedule for you. You check every word and post it yourself.
- **Only true claims.** It uses only what you tell it. It will not invent offers, prices, discounts, awards, reviews, customer quotes or urgency, and it will not say "best" or "No. 1" unless you say you can show it.
- **No health claims.** It will not write that a food, drink, class or treatment cures or prevents anything.
- **People in photos need permission.** It suggests hands, food, rooms, views and you. For a customer's or staff member's face, ask first. For children, a parent must agree.
- **No promised results.** No one can promise a number of likes, followers, customers or bookings. The plan gives you simple counts so you can see for yourself.
- **Paid ads are optional.** It never makes ads the whole plan and never predicts reach or sales.
- **Free and paid plans.** The phone helper works on any Claude plan, including free, and in ChatGPT or Gemini too. Uploading Skills needs a paid Claude plan with code execution turned on.

## Privacy

Never type these into any AI chat, this one included:

- Customers' or guests' names and phone numbers, or your contact list
- Aadhaar, PAN or passport details
- Bank, UPI and card details (it writes [your UPI ID])
- Passwords and OTPs, including your Instagram, Facebook or Google login
- Sales figures, money totals or customer lists
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

You don't need to upload your photos either. Describe the photo in words. If you paste something by mistake, stop, delete that chat, and type it again with a [blank].

## Tested

Each Skill has behavior cases with made-up businesses in [`evals/`](../../evals/) at the repo root: `evals/testbank/SCP.json` (social-content-planner) and `evals/testbank/SMP.json` (simple-marketing-plan). The checker is in `evals/harness/`. Results are in [`evals/RESULTS.md`](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you check and post everything yourself.
