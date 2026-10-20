# Example 01: an artist ties her shop, workshops and commissions together (fictional)

## Part 1: the checklist (job A)

**Owner types:**
> I'm a painter, Sample Studio, Assagao. Everything is digitized. Originals and prints are on a free shop app with my payment gateway. I run painting workshops, people message me on WhatsApp to book. Commissions come as Instagram DMs. Most people find me on Instagram, some by word of mouth. Originals are for collectors and people doing up homes, prints for gift buyers, workshops for beginners and visitors. I want people to find their own way. Make my checklist.

**Helper replies:**

**Offer map**

| Offer | Who it's for | The one action | Where it happens today | What's missing |
|---|---|---|---|---|
| Original paintings | Collectors, people doing up homes | Buy | Shop app | Sizes and shipping [blank] |
| Prints | Gift buyers | Buy | Shop app | Shop link not in Instagram bio |
| Painting workshops | Beginners, visitors | Book | WhatsApp | No ready message; dates [blank] |
| Commissions | [blank] | Ask (suggested) | Instagram DMs | No reply promise; no clear path |

**Entry point checklist** (copy into a phone note)
```
1. One page showing originals, prints, workshops and commissions.
2. Put that one link in your Instagram bio and WhatsApp profile.
3. One button each: Shop originals, Shop prints, Book a workshop, Ask.
4. Shop buttons open your shop app, not your Instagram grid.
5. Workshop button opens WhatsApp with "I would like to book" ready.
6. Commissions button opens WhatsApp, so DMs stop getting lost.
7. Add a reply promise: "I reply within [blank]."
8. Fill in sizes, shipping and workshop dates, or write "ask me".
9. Test every button on a phone, on mobile data.
10. Weekly check: count inquiries, orders and bookings.
```

Who commissions are for is [blank]: **target-customer-finder** can help with that. Next: say "write my page".

## Part 2: the page file (job C)

**Owner types:**
> Build the page file. Headline: paintings, prints and workshops from Assagao. About me: I paint the light and greens of North Goa from my home studio. People always ask: do you ship, can I pick up, do I need experience for the workshop.

**Helper replies:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>[your business name]</title>
<meta name="description" content="I paint the light and greens of North Goa from my home studio.">
<!--
  BEFORE YOU PUBLISH
  1. Replace every placeholder in [square brackets], brackets included.
  2. Links with a dashed red outline are not filled in yet.
  3. Delete any photo line you don't need.
  This page has no scripts, no tracking and no forms. You publish it yourself.
-->
<style>
:root{--bg:#fffdf8;--text:#1f1d1a;--muted:#5a554d;--card:#ffffff;--line:#e4ddd1;--btn:#1f4d3a;--btn-text:#ffffff;--mark:#c62828}
@media (prefers-color-scheme: dark){:root{--bg:#141311;--text:#f3efe8;--muted:#c9c1b5;--card:#1f1d1a;--line:#3b3731;--btn:#a8dcc0;--btn-text:#0f241a;--mark:#ff8a80}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:18px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",sans-serif}
main{max-width:640px;margin:0 auto;padding:24px 16px 48px}
h1{font-size:1.9rem;line-height:1.2;margin:8px 0}
h2{font-size:1.3rem;line-height:1.3;margin:0 0 8px}
p{margin:0 0 12px}
.intro{color:var(--muted)}
.jump{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin:16px 0 24px;padding:0}
.jump a{display:inline-flex;align-items:center;min-height:48px;padding:8px 16px;border:1px solid var(--line);border-radius:999px;color:var(--text);text-decoration:none}
.offer{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;margin:0 0 16px;scroll-margin-top:16px}
.offer img{display:block;width:100%;height:auto;border-radius:10px;margin:0 0 12px}
.btn{display:flex;align-items:center;justify-content:center;min-height:52px;padding:12px 18px;border-radius:12px;background:var(--btn);color:var(--btn-text);font-weight:600;font-size:1.05rem;text-align:center;text-decoration:none}
a:focus-visible,summary:focus-visible{outline:3px solid var(--text);outline-offset:3px}
a[href^="["],a[href*="/["]{outline:3px dashed var(--mark);outline-offset:2px}
img[src^="["]{min-height:96px;outline:3px dashed var(--mark)}
section{margin:32px 0}
ol{padding-left:24px}
li{margin:0 0 8px}
details{border-top:1px solid var(--line);padding:4px 0}
summary{display:flex;align-items:center;min-height:48px;font-weight:600;cursor:pointer}
footer{border-top:1px solid var(--line);margin-top:32px;padding-top:16px;color:var(--muted);font-size:.95rem}
footer a{display:inline-flex;align-items:center;min-height:48px;color:var(--text)}
</style>
</head>
<body>
<main>
<header>
<h1>Paintings, prints and workshops from Assagao</h1>
<p class="intro">I paint the light and greens of North Goa from my home studio.</p>
<nav aria-label="Quick links">
<ul class="jump">
<li><a href="#originals">Originals</a></li>
<li><a href="#prints">Prints</a></li>
<li><a href="#workshops">Workshops</a></li>
<li><a href="#commissions">Commissions</a></li>
<li><a href="#how">How to order</a></li>
</ul>
</nav>
</header>

<article class="offer" id="originals">
<!-- Delete this line if you have no photo. -->
<img src="[your photo file name or link]" alt="[describe this painting in a few words]">
<h2>Original paintings</h2>
<p>One-of-a-kind paintings of North Goa, for collectors and homes. Sizes: [blank].</p>
<a class="btn" href="[your shop link]">Shop originals</a>
</article>

<article class="offer" id="prints">
<!-- Delete this line if you have no photo. -->
<img src="[your photo file name or link]" alt="[describe this print in a few words]">
<h2>Prints</h2>
<p>Prints of my paintings, made for gifting. Sizes and paper: [blank].</p>
<a class="btn" href="[your shop link]">Shop prints</a>
</article>

<article class="offer" id="workshops">
<!-- Delete this line if you have no photo. -->
<img src="[your photo file name or link]" alt="[describe this workshop photo in a few words]">
<h2>Painting workshops</h2>
<p>Painting sessions for beginners and visitors. Next dates: [blank].</p>
<a class="btn" href="https://wa.me/[your number with country code, no +]?text=Hi%2C%20I%20would%20like%20to%20book%20a%20painting%20workshop">Book a workshop</a>
</article>

<article class="offer" id="commissions">
<h2>Commissions</h2>
<p>A painting made for you. Tell me what you have in mind and I will reply with the next steps.</p>
<a class="btn" href="https://wa.me/[your number with country code, no +]?text=Hi%2C%20I%20would%20like%20to%20ask%20about%20a%20commission">Ask about a commission</a>
</article>

<section id="how">
<h2>How to order or book</h2>
<ol>
<li>Tap the button for what you want.</li>
<li>Paintings and prints: pay in the shop.</li>
<li>Workshops and commissions: send the ready message on WhatsApp.</li>
<li>I confirm by message.</li>
</ol>
<p>I reply within [blank].</p>
</section>

<section id="faq">
<h2>Questions</h2>
<details><summary>Do you ship?</summary><p>[blank]</p></details>
<details><summary>Can I pick up from the studio?</summary><p>[blank]</p></details>
<details><summary>Do I need experience for the workshop?</summary><p>[blank]</p></details>
</section>

<footer>
<p>[your business name] · Assagao</p>
<p><a href="[your Instagram link]">Instagram</a> · <a href="https://wa.me/[your number with country code, no +]">WhatsApp</a></p>
</footer>
</main>
</body>
</html>
```

**Fill in before publishing:**
- [your shop link]: your shop app's page (both shop buttons; change one if originals and prints have separate pages).
- [your number with country code, no +]: your WhatsApp Business number, country code first (India is 91), no +, no spaces. It appears three times.
- [your Instagram link], [your business name], and a photo file or link with a short description for each photo (or delete the photo lines).
- Each [blank]: sizes of originals, print sizes and paper, workshop dates, your reply time, and the three FAQ answers.

**Where to put it (free):**
1. Your portfolio site's builder: add a "Start here" page; paste this file if it accepts custom HTML, or use the same words and links.
2. Google Sites: it doesn't take a whole HTML file, so rebuild the page with text blocks and buttons using these words.
3. A link-in-bio service: add one button per offer with the same labels and links.
4. GitHub Pages: its rules say it is not meant for running an online business or a site mainly for selling, so read its current terms first or pick another option.
5. Instagram: Edit profile > Links > add [your page link]. WhatsApp Business: Business tools > Business profile > Website.
6. Check each service's current terms and limits before you rely on it; menus change.

(Next: say "conversion paths" for the messages after each tap.)

## Why it looks like this
- The commission path moved from Instagram DMs to WhatsApp with a ready message, so the owner sees which offer each person came for.
- Nothing the owner didn't say is on the page: no sizes, dates, prices, shipping or pickup answers.
- The FAQ answers stay [blank]: shipping and pickup terms are the owner's to decide, and refund or returns wording is for a qualified person to check.
