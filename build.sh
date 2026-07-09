#!/bin/bash
set -euo pipefail

# Build the site into the repo root, then stage a publishable copy in out/.
#
# The repo root is NOT the published tree. out/ is. That distinction is the
# whole point: it lets us keep instructor material in the repository without
# serving it. Anything not copied below is simply not published.

rm -f index.html topics.html topic*.html
rm -rf assets/css out

npm run build

mkdir -p out

# Generated pages and stylesheet.
cp index.html topics.html out/
cp topic*.html out/
mkdir -p out/assets
cp -r assets/css out/assets/css

# Student-facing pages that are not generated. These are hand-written and still
# use the original style.css, so it ships alongside them.
cp acf_problem_set_no_solutions.html midterm_presentation_guide.html style.css out/
mkdir -p out/Final
# grading_form.html is a blank rubric, linked from the final guide. It was never
# committed, so that link 404'd on the live site.
cp "Final/final_presentation_guide.html" "Final/grading_form.html" out/Final/
# The rest of Final/ — Final_submission/, grading_AI66*.xlsx, Exam_day/ — holds
# student work and marks. It is gitignored and never published.

# Slides and images.
cp -r slides img out/

# Topic images only. README.md and starter.ipynb are read on GitHub, and the
# topic pages already embed the README content.
mkdir -p out/Topic
for d in Topic/*/; do
  name=$(basename "$d")
  mkdir -p "out/Topic/$name"
  find "$d" -maxdepth 1 -type f \( -iname '*.jpeg' -o -iname '*.jpg' -o -iname '*.png' \) \
    -exec cp {} "out/Topic/$name/" \;
done

# From idea/, publish ONLY the three pages the site links plus the figures they
# embed. Deliberately excluded:
#   idea/week10_exercise/solution_key.html
#   idea/week13_exercise/solution_key.html   -> answer keys, linked from nowhere
#   idea/**/*.py, *.ipynb, *.csv             -> generator scripts and raw data
mkdir -p out/idea/figures out/idea/eeg_emg_exercise out/idea/week6_7_exercise
cp idea/acf_problem_set.html out/idea/
cp idea/figures/*.png out/idea/figures/
cp idea/eeg_emg_exercise/eeg_emg_practice_exercises.html out/idea/eeg_emg_exercise/
cp idea/week6_7_exercise/health_practice_exercises.html out/idea/week6_7_exercise/

# Guard: nothing named solution_key may reach the published tree.
if find out -name 'solution_key*' | grep -q .; then
  echo "error: a solution_key file reached out/. Refusing to publish." >&2
  exit 1
fi

echo ""
echo "Staged in out/: $(find out -type f | wc -l | tr -d ' ') files"
echo ""
