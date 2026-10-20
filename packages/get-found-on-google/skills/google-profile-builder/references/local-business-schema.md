# Website basics: titles, headings and LocalBusiness code

Use this only when the owner has a website. The owner (or their web person) makes the changes. This is a draft; check Google's own help pages ("structured data LocalBusiness") because the details change.

## 1. Page title and main heading for each main service

One page per main service works best. For each one, write:

- **Page title** (the words in the browser tab and in Google results): 60 characters or fewer. Pattern: `[Service] in [Town] | [your business name]`.
- **Main heading** (the big heading at the top of the page, also called H1): plain words a customer would say. Pattern: `[Service] for [who it's for] in [towns]`.
- **First line on the page:** one sentence saying what you do and where, using the owner's facts.

Example (fictional):

| Page | Page title | Main heading |
|---|---|---|
| Generators | Generator Hire in Verna, Goa \| Sample Equipment Hire | Generator hire for building sites and events across Goa |
| Scaffolding | Scaffolding Rental in Goa \| Sample Equipment Hire | Scaffolding rental with delivery in North and South Goa |

Only use towns and services the owner gave. Use each search phrase once in the title and once or twice on the page, naturally. Never repeat a town list over and over.

Also check:
- The same name, address and phone as on Google, in the footer of every page.
- A contact page with a Google Map of the location (if customers visit) or a list of areas served.
- The site opens fast on a phone.

## 2. LocalBusiness code (JSON-LD)

This small block tells Google the business facts in a form it reads easily. It does not guarantee anything in search. The web person pastes it inside the page's `<head>` section, or uses the site builder's "custom code" box. Change `LocalBusiness` to a closer type only if the web person checks it on schema.org (for example `HomeAndConstructionBusiness`, `ProfessionalService`).

Rules for filling it in:
- Every value comes from the owner. Anything unknown stays `[blank]`, and the web person fills it in or deletes that line before publishing.
- The phone, address and website are typed in by the owner or web person, never pasted into an AI chat. Keep them exactly as on the Google profile.
- No ratings or review counts in this code. Google does not show self-written review markup for your own business, and invented ratings break Google's rules.
- Hours use the format `Mo-Sa 09:00-19:00` (two-letter days, 24-hour clock). Leave `[blank]` if the owner didn't give hours.
- For a service-area business with no visiting address, delete the `address` block and keep `areaServed`.

Template:

```
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[your business name]",
  "description": "[one sentence from your Google description]",
  "url": "[your website]",
  "telephone": "[your phone number]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[street address]",
    "addressLocality": "[town]",
    "addressRegion": "Goa",
    "postalCode": "[PIN code]",
    "addressCountry": "IN"
  },
  "areaServed": ["[town 1]", "[town 2]", "[town 3]"],
  "openingHours": "[your hours, in the format above]",
  "image": "[link to a photo of your business]",
  "sameAs": ["[your Facebook page link]", "[your Instagram link]"]
}
</script>
```

After it is live, the web person can test the page with Google's Rich Results Test (search for it by name) and fix any errors it shows.
