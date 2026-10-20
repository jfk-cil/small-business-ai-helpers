# Get found on Google

A complete Google profile, the right words, and honest steps to earn genuine reviews.

## The problem

An equipment hire business in Goa doesn't show up when people search Google for equipment rental. Many local businesses are in the same place. Their Google Business Profile is missing, unverified or half filled in, and their name, address and phone are written differently on every site.

## What you get

- A short checklist to claim, verify and complete your free Google Business Profile: categories to search for, hours, address or service area, and photos.
- A business description in Google's 750-character limit, using your real services and towns.
- Your services, each with a description in Google's 300-character limit.
- Four weekly Google posts, each with a photo idea you can take yourself.
- A WhatsApp message asking customers for an honest review, and how to find your review link.
- 10 to 15 search phrases people use (service plus town), and a checklist to keep your name, address and phone the same everywhere.
- If you have a website: page titles and a code block for your web person.
- Calm replies to your Google reviews, good or bad.
- Clean text for menus, product lists, catalogs and website pages.

Every text sits in its own box, with a character count, ready to copy.

## Use it in 2 minutes on your phone

Open the phone page: https://jfk-cil.github.io/small-business-ai-helpers/get-found-on-google/

1. Answer five short questions about your business. Every question is optional.
2. Tap **Make my helper**, then **Copy helper**.
3. Open Claude, or the AI you already use (it should also work in ChatGPT and Gemini; tested so far in Claude only), start a new chat, paste the helper and send it.
4. Type "go". It writes your kit one part at a time and asks before the next part.

If you open the page inside Claude, a **Try it here** box lets you run it on the page itself. It runs on your own Claude account. This page saves nothing.

Send the helper to yourself on WhatsApp ("Message yourself") so you can copy it again any day.

## Install the full version

The full version knows more of Google's rules, checks its own character counts and handles more cases. It comes as three Skills.

**Claude on the web or desktop app** (paid plan, code execution turned on, as of October 2026)

Download each Skill:

- [google-profile-builder.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/google-profile-builder.zip)
- [listing-and-catalog-writer.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/listing-and-catalog-writer.zip)
- [review-replies.zip](https://jfk-cil.github.io/small-business-ai-helpers/downloads/review-replies.zip)

Then in Claude open **Settings**, then **Capabilities**, then **Skills**, and upload each zip. Start a new chat and say "My business doesn't show up on Google."

**Claude Code**

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install get-found-on-google@small-business-ai-helpers
```

**Cowork**

Open **Customize**, then **Plugins**, then **Add marketplace** (as of October 2026). Enter `jfk-cil/small-business-ai-helpers`, then install **get-found-on-google**.

## What's inside

| Skill | What it does | When to use it |
|---|---|---|
| google-profile-builder | Builds your Google profile kit: setup checklist, description, services, four weekly posts, review request, same name-address-phone checklist, search phrases, and website basics if you have a site. | "My business doesn't show up on Google." "Set up my Google Business Profile." |
| listing-and-catalog-writer | Rewrites menus, product and catalog text, directory listings and website pages in plain words, with character counts. | "Fix my menu." "Write my About page." "Write my WhatsApp catalog." |
| review-replies | Drafts short, calm replies to reviews, and one honest message asking every customer for a review. | "Reply to this Google review." "How do I get more reviews?" |

## Limits

- **Drafts only.** It writes words and checklists. It cannot log in to Google, claim your profile, post for you or schedule posts. You do every step in Google yourself.
- **No ranking promises.** Following the kit improves your chances. Ranking depends on Google: on how well your profile matches the search, how far you are from the person searching, and how well known you are. Ads can appear above the results, but no one can pay for a higher free place, and no one can guarantee one.
- **Genuine reviews only.** It will not write reviews, offer gifts or discounts for reviews, or help ask only happy customers.
- **Your real business name.** It will not add search words, towns or "best" to your name. Google can suspend profiles for that.
- **No unproven claims.** It leaves out "largest", "best" and "No. 1" and suggests a fact you can show instead.
- **Free and paid plans.** The phone helper should work on any Claude plan, including free, and also in ChatGPT or Gemini (tested so far in Claude only). Uploading Skills needs a paid Claude plan with code execution turned on. On a free plan you get fewer messages a day, so let it write one part at a time.
- **Rules change.** Google's menus and guidelines change. Check Google's own help pages before you rely on any line.

## Privacy

Never type these into any AI chat, this one included:

- Your Google login, password or verification code
- Customers' or guests' names and phone numbers
- Aadhaar, PAN or passport details
- Bank, UPI and card details
- Passwords and OTPs of any kind
- Health information
- Staff ID numbers and wages
- Family members' details
- Photos of people

Type your own phone number, address and website straight into Google, not into the chat. When you reply to a review, paste the review without the reviewer's name. If you paste something by mistake, stop, delete that chat, and type it again with a [blank].

## Tested

Each Skill has behavior cases with made-up businesses in [`evals/`](../../evals/) at the repo root: `evals/testbank/GPB.json` (google-profile-builder), `evals/testbank/LCW.json` (listing-and-catalog-writer) and `evals/testbank/RR.json` (review-replies). The checker is in `evals/harness/`. Results are in [`evals/RESULTS.md`](../../evals/RESULTS.md).

Free to use and adapt (CC0). It drafts; you check and publish everything yourself.
