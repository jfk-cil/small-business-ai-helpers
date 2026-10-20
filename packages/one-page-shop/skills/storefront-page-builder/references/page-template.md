# Page template for storefront-page-builder (Mode C)

The skeleton below is the whole page. Fill it with the Mode B copy and give the owner the result in ONE copy box (```html). Do not add anything that is not in this skeleton.

## How to fill it
- Replace each `{{...}}` with the owner's copy from Mode B. `{{...}}` never appears in the output.
- Keep every `[your ...]` placeholder exactly as written, brackets included. The owner replaces them.
- Copy the offer block once per offer, in the Offer map order (up to 6). Give each block a short lowercase `id` with hyphens (`shop`, `workshops`, `commissions`). The same id goes in the quick links at the top, so `[your page link]#workshops` opens straight at that offer.
- Button links, by action:
  - Buy: `[your shop link]` or `[your payment link]`
  - Book: `[your booking form link]`, or WhatsApp if bookings happen in chat
  - Ask: WhatsApp with a prefilled message
  - Join list: `[your sign-up form link]`, or WhatsApp with "Please add me to your updates list"
- WhatsApp links: `https://wa.me/[your number with country code, no +]?text=` then the prefilled message with each space written as `%20` and each comma as `%2C`. Keep the message plain: letters, numbers, spaces, commas and periods. Letters in Hindi, Marathi or Konkani can stay as typed.
- Images: one `img` per offer, optional. Keep `src="[your photo file name or link]"` and an `alt` placeholder that says what to describe. Write "Delete this line if you have no photo." as the HTML comment above it. Photos of products, work, rooms or the owner; customers' faces only with their permission; never children's faces.
- FAQ: up to 5 `details` blocks. An answer the owner didn't give stays `[blank]`.
- Language: set `lang="en"` (English), `lang="hi"` (Hindi), `lang="mr"` (Marathi) or `lang="kok"` (Konkani).
- Never add: `<script>`, `<form>`, `<iframe>`, `<link rel="stylesheet">`, `@import`, web fonts, analytics or tracking code, counters, cookie banners, countdown timers, or any web address other than the wa.me placeholder.
- The dashed red outline in the CSS marks links that still hold a placeholder, so the owner can see on the page what is left to fill. It disappears once a real link is in.

## Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>[your business name]</title>
<meta name="description" content="{{WHO I AM LINE}}">
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
<h1>{{HEADLINE}}</h1>
<p class="intro">{{WHO I AM LINE}}</p>
<nav aria-label="Quick links">
<ul class="jump">
<li><a href="#{{OFFER ID}}">{{OFFER TITLE}}</a></li>
<!-- one li per offer -->
<li><a href="#how">How to order</a></li>
</ul>
</nav>
</header>

<!-- OFFER BLOCK: copy once per offer -->
<article class="offer" id="{{OFFER ID}}">
<!-- Delete this line if you have no photo. -->
<img src="[your photo file name or link]" alt="[describe this photo in a few words]">
<h2>{{OFFER TITLE}}</h2>
<p>{{OFFER TEXT}}</p>
<a class="btn" href="{{LINK PLACEHOLDER}}">{{BUTTON LABEL}}</a>
</article>

<section id="how">
<h2>How to order or book</h2>
<ol>
<li>{{STEP}}</li>
<!-- 3 or 4 steps -->
</ol>
<p>{{REPLY PROMISE, for example: I reply within [blank].}}</p>
</section>

<section id="faq">
<h2>Questions</h2>
<details><summary>{{QUESTION}}</summary><p>{{ANSWER or [blank]}}</p></details>
<!-- up to 5 -->
</section>

<footer>
<p>[your business name] · {{PLACE}}</p>
<p><a href="[your Instagram link]">Instagram</a> · <a href="https://wa.me/[your number with country code, no +]">WhatsApp</a></p>
</footer>
</main>
</body>
</html>
```

## Checks before giving it to the owner
1. One copy box, starting `<!DOCTYPE html>` and ending `</html>`.
2. No `{{` left anywhere.
3. No `<script`, `<form`, `<iframe`, `stylesheet`, `@import`.
4. The only web address is `https://wa.me/[your number with country code, no +]` (with or without `?text=`). No real phone number after `wa.me/`.
5. Every offer has one button, and every button's link is a placeholder.
6. Every `img` has an `alt` placeholder.
7. No price, date, size, material, shipping term, refund rule or review the owner didn't give.
