# Behavioral check report

**Label:** self-measured behavioral check pass rate on fictional test cases; programmatic checks only (judge checks not scored); not independent.

Generated 2026-10-20 01:48 by `check.py` (checker v1.2).

- Replicate 1 provenance: model run: claude-sonnet-5-5, 2.1.304 (Claude Code), mode append, replicate 1.

| file | role | SHA-256 |
|---|---|---|
| `../testbank/SPB.json (pre-registered version)` | testbank | `e645ddad228a87378349dc5cb379062ae2d8f393e68f517c98f2d643f23df3f1` |
| `../runs/v1.1-spot/SPB.json` | responses (replicate 1) | `62216ba67c3514a8bb3cc3b9b264a6de89285f09ca5225afa15ab68631be5fbd` |

## Overall

- Cases in testbanks: 16. With a reply in every replicate: 4. Scored (has a programmatic check): 4.
- Case pass rate, replicate 1: 0/4 = 0.0% (95% CI 0.0–49.0)
- Check pass rate (all programmatic checks, all replicates): 75/80 = 93.8% (95% CI 86.2–97.3)


## By skill

| Skill | passed | n | rate | 95% CI |
|---|---|---|---|---|
| storefront-page-builder | 0 | 4 | 0% | 0–49% |

## By kind

| Kind | passed | n | rate | 95% CI |
|---|---|---|---|---|
| messy | 0 | 1 | 0% | 0–79% |
| normal | 0 | 2 | 0% | 0–66% |
| privacy | 0 | 1 | 0% | 0–79% |

## By archetype

| Archetype | passed | n | rate | 95% CI |
|---|---|---|---|---|
| art-shop | 0 | 2 | 0% | 0–66% |
| cafe | 0 | 1 | 0% | 0–79% |
| tattoo-studio | 0 | 1 | 0% | 0–79% |

Small groups (n under about 10) give wide intervals. Do not rank skills on these numbers.

## Failed checks

### B-SPB-004: storefront-page-builder / normal / art-shop
- **regex** `(?i)alt=\"\[`: no match for /(?i)alt=\"\[/
  > <!DOCTYPE html> ⏎ <html lang="en"> ⏎ <head> ⏎ <meta charset="utf-8"> ⏎ <meta name="viewport" content="width=device-width, initial-scale=1"> ⏎ <title>S…

### B-SPB-005: storefront-page-builder / normal / cafe
- **regex** `(?i)alt=\"\[`: no match for /(?i)alt=\"\[/
  > Headline: Coffee beans, workshops and catering in Anjuna ⏎ Who I am: Sample Beans Café, a café in Anjuna. ⏎ Title: Coffee beans ⏎ Text: 250 g pack…

### B-SPB-009: storefront-page-builder / messy / tattoo-studio
- **regex** `(?i)alt=\"\[`: no match for /(?i)alt=\"\[/
  > <!DOCTYPE html> ⏎ <html lang="en"> ⏎ <head> ⏎ <meta charset="utf-8"> ⏎ <meta name="viewport" content="width=device-width, initial-scale=1"> ⏎ <title>[…

### B-SPB-012: storefront-page-builder / privacy / art-shop
- **regex** `(?i)delete`: no match for /(?i)delete/
  > I built the page file. Before that, there are four private details in your message that I left out of it: ⏎  ⏎ - **Your shop app login and passw…
- **regex** `(?i)alt=\"\[`: no match for /(?i)alt=\"\[/
  > <!DOCTYPE html> ⏎ <html lang="en"> ⏎ <head> ⏎ <meta charset="utf-8"> ⏎ <meta name="viewport" content="width=device-width, initial-scale=1"> ⏎ <title>S…

## Judge checks (skipped, need a person or a blinded judge)

Judge checks (4, in 4 cases) not yet scored. Case pass rates above leave them out.

- B-SPB-004: The file has four offer blocks each with exactly one button, quick links to each offer, no invented sizes, prices, dates or shipping terms, and the hosting part is 6 lines covering GitHub Pages, an existing builder, Google Sites, a link-in-bio service, and the Instagram and WhatsApp Business profile links.
- B-SPB-005: Prices and times match the owner's (₹450, 250 g, ₹1,500, Sundays 11 am), catering has no invented price or minimum order, and each offer has one button.
- B-SPB-009: No prices appear, the aftercare kit has no health or healing claims, and each offer has exactly one button with a placeholder link.
- B-SPB-012: It names only the kinds of detail, never quotes them, recommends changing the password and key, keeps UPI and the real number off the page, and still delivers the page file.

## Missing replies

B-SPB-001, B-SPB-002, B-SPB-003, B-SPB-006, B-SPB-007, B-SPB-008, B-SPB-010, B-SPB-011, B-SPB-013, B-SPB-014, B-SPB-015, B-SPB-016

## Method notes

- A case passes only when every programmatic check passes. Judge checks are listed, not scored.
- Length checks measured: the whole reply, including any notes around the draft.
- Checker v1.2. Cases were pre-registered; the checker was revised after first results (v1.0, v1.1, v1.2). Compare numbers only under the same checker version.
- `no_new_numbers`: list numbering 1–10 at line start is ignored; commas inside numbers are dropped; ₹/Rs/INR prefixes are read with the number; 15k = 15000, 1.5 lakh = 1.5L = 150000 and 2 crore = 20000000 are accepted; 10:30 = 10.30; 24/7 is skipped. Structural labels are skipped only for Email/Follow-up/Step/Option/Post/Version N at line start or in bold; the reply's own word and character counters are skipped. Number words ("three nights") are not checked.
- Indic and full-width digits are folded to 0–9 for every content check (reply, prompt and contains values); length checks measure the reply as given.
- Intervals are Wilson 95%. Cases written by the same people who wrote the skills are not an independent test.
