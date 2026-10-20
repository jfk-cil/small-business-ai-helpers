# Find new clients

Turn your best customers into a clear picture of who to look for, where, and what to say.

## The problem

Small service businesses that sell to other businesses, such as a marketing agency, often get work by word of mouth and then hit slow patches. When work is slow, it is hard to say who exactly needs you, where to find them, or what to say first. The goal is a steady list of good leads, found and contacted the right way.

## What you get

The phone helper works in four steps, one per message, and asks before moving on:

1. **2 or 3 customer types**, built from your best customers: who they are, what problem they have, what makes them say yes.
2. **10 search phrases per type** that you type yourself into Google, Google Maps, Instagram or LinkedIn. It never invents business names or contacts.
3. **Local businesses that could refer customers to you**, and a short intro message for each kind.
4. **A first message for each customer type** in your voice, under 120 words, plus one polite follow-up.

The full version (Skills) also:
- writes an honest first email to one business, with up to 3 follow-ups if you ask;
- helps you write 4 to 6 yes/no "fit questions", then checks one inquiry as Good fit, Maybe or Not now;
- writes the welcome message, next steps and your first-week checklist when a new client says yes.

## Use it in 2 minutes on your phone

1. Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/find-clients/
2. Answer 4 short questions: what you sell and to whom; your 3 best customers (types, not names); where your clients are; how you'd like to reach out. All are optional. You can tap the mic on your keyboard and speak. The page has English, Hindi, Marathi and Konkani (Devanagari and Romi).
3. Tap **Make my helper**, then **Copy helper**.
4. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste and send.
5. Type "go" to start with step 1.

Keep it for next time: send the helper to yourself in WhatsApp ("Message yourself").

If you open the page inside Claude, a **Try it here** box lets you test the helper on the page. It runs on your own Claude account. This page saves nothing.

## Install the full version

The full version is a set of Claude Skills. They know more and check their own work.

**claude.ai (web or desktop app)**
You need a paid Claude plan with code execution turned on (Settings > Capabilities), as of October 2026.
1. Download the Skills:
   - [target-customer-finder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/target-customer-finder.zip)
   - [outreach-email-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/outreach-email-writer.zip)
   - [lead-qualifier.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/lead-qualifier.zip)
   - [client-onboarding-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/client-onboarding-writer.zip)
2. In Claude, open Settings > Capabilities > Skills and upload each zip file.
3. In a new chat, type: "Who should I be selling to?" and say what you sell.

**Claude Code**
```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install find-clients@small-business-ai-helpers
```

**Cowork**
Open Customize > Plugins > Add marketplace (as of October 2026) and enter `jfk-cil/small-business-ai-helpers`. Then install **find-clients** from that marketplace.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| [target-customer-finder](../../skills/target-customer-finder/SKILL.md) | Names 2 or 3 customer types, the kinds of public places to find them, and 10 search phrases. Types, never named people or contacts. | "Who should I sell to?" "How do I find more clients?" "I need more leads." |
| [outreach-email-writer](../../skills/outreach-email-writer/SKILL.md) | Writes a short, honest first email to one business, with an easy "no thanks" line, and up to 3 follow-ups when asked. | "Write a first email to a hotel." "They never replied. What do I send next?" |
| [lead-qualifier](../../skills/lead-qualifier/SKILL.md) | Helps you write 4 to 6 yes/no fit questions about the job (need, budget, timing, area, who decides), then checks one inquiry. Business facts only. | "Is this lead worth it?" "Which inquiries should I chase first?" |
| [client-onboarding-writer](../../skills/client-onboarding-writer/SKILL.md) | Writes a welcome message, what happens next, what you need from the client, and your first-week checklist. | "They said yes!" "New client starts Monday." |

Owner cards (one page each, plain words): [target-customer-finder](../../skills/target-customer-finder/OWNER-CARD.md), [outreach-email-writer](../../skills/outreach-email-writer/OWNER-CARD.md), [lead-qualifier](../../skills/lead-qualifier/OWNER-CARD.md), [client-onboarding-writer](../../skills/client-onboarding-writer/OWNER-CARD.md).

For the owner: [PLAYBOOK.md](PLAYBOOK.md). For a volunteer at the table: [BUILDER-NOTES.md](BUILDER-NOTES.md).

## Limits

- **You do the searching.** It gives types and search phrases. It never lists named people, phone numbers, emails or home addresses, and it doesn't name specific businesses: your own search will be current, its guesses might not be.
- **No lists, no scraping.** It won't collect, buy, copy or use contact lists or follower lists.
- **No cold WhatsApp in bulk.** First contact goes by email, a business's own contact form or business page, or in person, one business at a time. WhatsApp can block numbers that message strangers in bulk.
- **No made-up proof or urgency.** No invented clients, numbers, reviews or "only 2 spots left". No promise of results.
- **Fair checks only.** The lead checker looks at the job (need, budget, timing, area, who decides), never at religion, caste, community, gender, age, language or where someone is from. You make the call.
- **Drafts only.** You check and send every message yourself, from your own email or phone.
- **No contracts or tax advice.** For contract terms, billing details and tax, check with a qualified person.
- **Plans:** the phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. Claude Projects (saving the helper as instructions) also need a paid plan. Claude Code and Cowork need a plan that includes them. Free plans have message limits; if you reach one, paste the same helper into another AI.
- The Hindi, Marathi and Konkani versions of the page are draft translations. Check them with someone who reads the language well.

## Privacy

Never type these into the page or into any AI chat:

- Clients' or leads' names, phone numbers and emails (describe types, not people)
- Contact lists or follower lists, bought or copied
- Passport, Form C, Aadhaar or PAN details
- Bank, UPI and card details (the drafts use [your UPI ID])
- Passwords and OTPs
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

Keep the businesses you find in your own sheet, not in the AI chat. If you paste a private detail by mistake, delete that chat and type it again with a [blank].

The phone page checks your answers for phone numbers, email addresses, UPI IDs, Aadhaar-like and PAN-like numbers, card numbers and passwords before it makes the helper. It does not check what you paste into the AI afterward. Each AI company has its own rules about keeping chats, so check the privacy settings in the app you use.

## Tested

Each Skill has written test cases in [evals/testbank/](../../evals/testbank/) ([TCF.json](../../evals/testbank/TCF.json), [OEW.json](../../evals/testbank/OEW.json), [LQ.json](../../evals/testbank/LQ.json), [COW.json](../../evals/testbank/COW.json)), checked with the scripts in [evals/harness/](../../evals/harness/). Results, and what they do and don't show, are in [evals/RESULTS.md](../../evals/RESULTS.md).

Free to use and adapt (CC0).
