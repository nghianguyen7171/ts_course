#!/bin/bash
## Publish the built site to the gh-pages branch. Run from the project root.

set -euo pipefail

TARGET_BRANCH="gh-pages"

REPO=$(git config remote.origin.url)
SHA=$(git rev-parse --verify HEAD)

# The deployed site should always correspond to a commit that exists on main.
if [ -n "$(git status --porcelain -- src build.js build.sh)" ]; then
  echo "error: uncommitted changes to the site source. Commit them first." >&2
  exit 1
fi

# Build and stage out/ first, so a build failure never touches gh-pages.
./build.sh

# Clone gh-pages into a scratch dir, or start the branch if it does not exist.
rm -rf .deploy
git clone --quiet "$REPO" .deploy
cd .deploy
git checkout --quiet "$TARGET_BRANCH" 2>/dev/null || git checkout --quiet --orphan "$TARGET_BRANCH"
cd ..

# Clean every tracked path, keeping .git. `rm -rf .deploy/**/*` would leave
# directories standing and copy the new tree *into* them.
find .deploy -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +

cp -R out/. .deploy/
cd .deploy

# Serve the output verbatim; do not let Pages run Jekyll over it.
touch .nojekyll

git add --all .
if git diff --cached --quiet; then
  echo "No changes to deploy."
  cd .. && rm -rf .deploy
  exit 0
fi

git commit --quiet -m "Deploy to GitHub Pages: ${SHA}"
git push --quiet "$REPO" "$TARGET_BRANCH"
cd .. && rm -rf .deploy

echo ""
echo "Deployed ${SHA} to ${TARGET_BRANCH}."
echo "If this is the first gh-pages deploy, set Settings -> Pages -> Source"
echo "to 'Deploy from a branch' -> gh-pages -> / (root)."
echo ""
