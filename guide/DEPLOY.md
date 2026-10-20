# Deploying and publishing

Every way to put these helpers in front of owners, with exact steps. Before any of them, build and check from the repo root:

```
python3 scripts/build.py          # regenerate packages, pages, downloads and artifact fragments
python3 scripts/check.py          # must end with 0 errors
python3 scripts/build.py --check  # must say generated files are current
```

## (a) GitHub Pages (the phone pages)

The phone pages and the Skill downloads are static files in `docs/`.

1. Push `main` to `github.com/jfk-cil/small-business-ai-helpers`, with the built `docs/` folder committed.
2. On GitHub, open the repo's **Settings**, then **Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Set **Branch** to `main` and the folder to `/docs`. Click **Save**.
5. Wait for the Pages deployment to finish (the repo's **Actions** tab shows it), then open https://jfk-cil.github.io/small-business-ai-helpers/ on a phone.
6. Check one package page end to end with a made-up business: answer the questions, tap **Make my helper**, **Copy helper**, and open a Download link.

`docs/.nojekyll` is generated so GitHub serves the files as they are. Every later change goes live when it is pushed to `main`; always rebuild first.

## (b) Claude pages (the artifact fragments)

`artifacts/hub.html` and `artifacts/<id>.html` are the same pages as fragments that can be published as Claude pages. A Claude page adds one thing the GitHub page can't: the **Try it here** box, which answers on the viewer's own Claude account.

Each page must be published with the `sample` capability declared, `{"sample": {}}`. That is what lets the page ask the viewer's permission to use Claude. The first time a viewer taps **Try it here**, Claude asks them to allow it; if they decline, the box hides and the rest of the page still works.

Steps, from a Claude Code session in the repo (or any Claude session that can publish pages from a file):

1. Run `python3 scripts/build.py`.
2. Publish `artifacts/hub.html`, then each of the nine package fragments (`start-here`, `customer-replies`, `booking-reminders`, `follow-ups`, `find-clients`, `get-found-on-google`, `staff-checklists`, `hire-and-onboard`, `social-posts`). For each, ask Claude for exactly this: "Publish `artifacts/<page>.html` as a Claude page with capabilities `{"sample": {}}`." The page title comes from the fragment's own `<title>`.
3. Write each page's link into `artifacts/urls.json`. Keys are `hub` and the package ids:

   ```json
   {
     "hub": "https://claude.ai/...",
     "start-here": "https://claude.ai/...",
     "customer-replies": "https://claude.ai/...",
     "booking-reminders": "https://claude.ai/...",
     "follow-ups": "https://claude.ai/...",
     "find-clients": "https://claude.ai/...",
     "get-found-on-google": "https://claude.ai/...",
     "staff-checklists": "https://claude.ai/...",
     "hire-and-onboard": "https://claude.ai/...",
     "social-posts": "https://claude.ai/..."
   }
   ```

4. Run `python3 scripts/build.py` again. **Rebuild every time you edit `urls.json`.** The links between pages come only from this file; any id missing from it falls back to its GitHub Pages address.
5. Republish every fragment **to the same link** (same file in the same session, or give Claude the page's existing link). On a republish, leave the capabilities out to keep `sample` as it is. Don't send an empty set `{}`: that removes `sample` and the Try it here box disappears.
6. Test on a phone signed in to Claude: open the hub, open a package, make a helper with a made-up business, tap **Try it here**, allow access, and read the answer.
7. Claude pages start private. Share each one by link from the page's share settings when it is ready.

Notes:

- `artifacts/urls.json` is hand-written and is the only file in `artifacts/` that is not generated. `build.py --check` ignores it.
- Download links on Claude pages always point to the GitHub Pages downloads (`.../downloads/<skill>.zip`), so path (a) must be live too.

## (c) claude.ai Skill upload (the full Skills)

Each Skill is a zip in `docs/downloads/<skill>.zip`, also linked from its package page. The zip holds one folder named exactly like the Skill (for example `message-sorter/`) with `SKILL.md` inside, plus its references, examples, owner card, safeguards, changelog and license. Test cases are left out.

Requirements: a paid Claude plan, with code execution turned on (as of October 2026).

1. Download the zip for each Skill in the package (one zip per Skill; customer-replies needs three).
2. In Claude, open **Settings**, then **Capabilities** (as of October 2026). Make sure code execution is on.
3. In the **Skills** section, choose **Upload**, pick the zip, and make sure the Skill is turned on.
4. Repeat for each zip.
5. Test: start a new chat and ask for the job in plain words ("Sort my messages: ..."). Claude picks the Skill from its description.

Do not rename the zip's inner folder or the `name:` line in `SKILL.md`; they must match. To update a Skill, upload the new zip (remove the old one first if Claude asks).

On Team and Enterprise plans, an organization owner can provision a Skill for everyone in the organization from the organization's settings, so members don't each upload it (as of October 2026).

To zip a Skill by hand (for example a changed Skill before a release), run from the repo root:

```
cd skills && zip -r ../message-sorter.zip message-sorter -x 'message-sorter/evals/*'
```

## (d) Claude Code (plugins)

The repo is a plugin marketplace (`.claude-plugin/marketplace.json`); each package is a plugin.

```
/plugin marketplace add jfk-cil/small-business-ai-helpers
/plugin install <id>@small-business-ai-helpers
```

`<id>` is a package id, for example `customer-replies` or `staff-checklists`. Install as many as needed.

- To try a local copy before pushing, add the clone by path instead: `/plugin marketplace add ./` from the repo root.
- To pick up a new release: `/plugin marketplace update small-business-ai-helpers`.
- Before every release, validate the manifests from the repo root:

  ```
  claude plugin validate .
  ```

## (e) Cowork

1. Open **Customize**, then **Plugins**.
2. Choose **Add marketplace** and enter `jfk-cil/small-business-ai-helpers`.
3. Install the packages the owner needs.

Some organizations limit which marketplaces members can add; an admin may need to allow it.

## (f) Plain-text helpers in ChatGPT or Gemini

The phone helper is plain text, so it works in any chat AI, on any plan, including free ones.

1. Open the package's phone page, answer the questions, tap **Make my helper**, then **Copy helper**.
2. Open ChatGPT or Gemini, start a new chat, paste the helper and send it.
3. Then paste a customer message or describe today's job, with no names or numbers.
4. Save the helper in WhatsApp "Message yourself" to paste again any day.

If the AI lets you save standing instructions (for example a custom GPT in ChatGPT or a Gem in Gemini), the helper can go there instead. The full Skills are written for Claude; their references are not loaded automatically anywhere else.

## (g) For a group that runs sessions

A group that runs table sessions with owners can use the GitHub Pages links as they are, or publish its own copy of the Claude pages so the links are under its control.

Publishing your own Claude pages:

1. Clone the repo and run `python3 scripts/build.py`.
2. From your group's own Claude account, follow path (b): publish the hub and the nine package fragments with `{"sample": {}}`, put the links in `artifacts/urls.json`, rebuild, and republish to the same links.
3. Share the pages by link. Try it here still runs on each viewer's own Claude account, never on the group's.
4. If your sessions should send owners to your Claude pages instead of GitHub Pages, change the links in `packages/<id>/PLAYBOOK.md` and `packages/<id>/BUILDER-NOTES.md` (they name the GitHub Pages address), and reprint any handouts that carry the old links.

Hosting your own fork on GitHub:

1. Fork the repo. In `catalog/packages.json`, change `repo` to `<your-account>/<your-repo>` and `pages_base` to your Pages address. `marketplace_name` can stay.
2. Update the hand-written links in `README.md` and the package docs.
3. Rebuild and check, then follow path (a) for your fork.
4. The install command becomes `/plugin marketplace add <your-account>/<your-repo>`.

Before each session:

- Open every page you will use on a phone with mobile data, not office wifi.
- Run each helper once with the made-up example in its `BUILDER-NOTES.md`.
- Check the Download links work.
- Have the never-type list from [PRIVACY.md](PRIVACY.md) printed for each table.
- Owners use their own phones and their own AI accounts, never the group's or a volunteer's.

## Known limits

- **No one-click install link for claude.ai Skills.** There is no official link that installs a Skill into someone's claude.ai account. Owners download the zip and upload it in Settings (path c), or use the plain-text helper (path f).
- **No prefilled claude.ai prompt link.** A claude.ai link that opens a new chat with the helper already typed in is not supported, so the page uses **Copy helper** plus **Open Claude** (which opens a blank new chat).
- **Skills on the mobile app.** Whether Skills uploaded on claude.ai are used from the Claude mobile app is not documented. Test on the owner's phone before promising it; the plain-text helper works on any phone either way.
- **Try it here** appears only on Claude pages, only for a signed-in viewer who allows it. It never appears on GitHub Pages.
