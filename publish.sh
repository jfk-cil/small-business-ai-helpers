#!/usr/bin/env bash
# Publish (or update) this repo on GitHub, turn on the phone pages, and post the Skill zips.
# Run from this folder on a Mac with the GitHub CLI signed in:   bash publish.sh
# Safe to run again later: it updates the same repo.
set -euo pipefail

OWNER="jfk-cil"
NAME="small-business-ai-helpers"
REPO="$OWNER/$NAME"
SRC="$(cd "$(dirname "$0")" && pwd)"
VERSION="v$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["version"])' "$SRC/catalog/packages.json")"
TERMS="$SRC/../sbh-private-terms.txt"   # local only, never committed
WORK="$HOME/src/$NAME"   # outside iCloud, so git behaves

say() { printf '\n== %s\n' "$*"; }

say "1/7 Checking tools"
command -v gh >/dev/null || { echo "Install the GitHub CLI first: brew install gh"; exit 1; }
command -v git >/dev/null || { echo "Install git first: xcode-select --install"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "Sign in first: gh auth login"; exit 1; }
if ! gh auth status 2>&1 | grep workflow >/dev/null; then
  echo "Your GitHub login can't push workflow files yet. Run this, approve in the browser, then run publish.sh again:"
  echo "  gh auth refresh -h github.com -s workflow"
  exit 1
fi

say "2/7 Running the repo checks"
if [ -f "$TERMS" ]; then export SBH_PRIVATE_TERMS="$TERMS"; else echo "Note: $TERMS not found, so the private-name scan is skipped."; fi
python3 "$SRC/scripts/check.py"
python3 "$SRC/scripts/build.py" --check

say "3/7 Copying to $WORK"
mkdir -p "$WORK"
rsync -a --delete --exclude ".git" --exclude "__pycache__" --exclude ".DS_Store" --exclude "*.log" "$SRC/" "$WORK/"
cd "$WORK"

say "4/7 Committing"
if [ ! -d .git ]; then git init -q -b main; fi
git add -A
if git diff --cached --quiet; then echo "Nothing new to commit."; else
  git -c user.name="$OWNER" -c user.email="$OWNER@users.noreply.github.com" commit -q -m "Small business AI helpers $VERSION"; fi

say "5/7 Pushing to github.com/$REPO"
if gh repo view "$REPO" >/dev/null 2>&1; then
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$REPO.git"
  if git fetch -q origin main 2>/dev/null && ! git merge-base --is-ancestor origin/main HEAD; then
    echo "GitHub has changes this copy doesn't have. Pull them into $WORK first, then run again."; exit 1
  fi
  git push -u origin main
else
  gh repo create "$REPO" --public --source . --push \
    --description "Free AI helpers for small businesses: customer replies, bookings, follow-ups, clients, Google, posts, staff. Phone pages in 5 languages, Claude Skills, plugins. CC0."
fi
gh repo edit "$REPO" --homepage "https://$OWNER.github.io/$NAME/" \
  --add-topic small-business --add-topic claude-skills --add-topic whatsapp --add-topic india >/dev/null || true

say "6/7 Turning on the phone pages (GitHub Pages from /docs)"
if gh api "repos/$REPO/pages" >/dev/null 2>&1; then
  echo "Pages already on."
else
  if gh api -X POST "repos/$REPO/pages" -f "source[branch]=main" -f "source[path]=/docs" >/dev/null; then
    echo "Pages turned on. First build takes 1 to 3 minutes."
  else
    echo "Turn on Pages by hand: repo Settings > Pages > Branch main, folder /docs."
  fi
fi

say "7/7 Posting Skill zips as release $VERSION"
if gh release view "$VERSION" --repo "$REPO" >/dev/null 2>&1; then
  gh release upload "$VERSION" docs/downloads/*.zip --repo "$REPO" --clobber
else
  gh release create "$VERSION" docs/downloads/*.zip --repo "$REPO" --title "$VERSION" \
    --notes "Skill zips for upload in Claude (Settings > Capabilities > Skills). Phone pages: https://$OWNER.github.io/$NAME/"
fi

say "Done"
echo "Repo:        https://github.com/$REPO"
echo "Phone pages: https://$OWNER.github.io/$NAME/   (live in a few minutes)"
echo "Downloads:   https://github.com/$REPO/releases/latest"
echo "Plugins:     /plugin marketplace add $REPO"
