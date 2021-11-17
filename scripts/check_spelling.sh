set -euf -o pipefail

if ! command -v spellchecker &> /dev/null; then
  echo ":: Installing Spellchecker CLI"
  npm install -g spellchecker-cli@~4.7.0
fi

export PROJECT_ROOT="$(git rev-parse --show-toplevel)"

export RANGE_DONE="a-z0-9"

if grep -aR "]()" --include "*.md" .; then
  echo "CHECK FAILED"
  echo "============"
  echo "Found the string ']()' in one or more files."
  echo "Have you forgotten to fill a link?"
  exit 1
fi

(
  cd $PROJECT_ROOT
  spellchecker \
    -d "dictionary.txt" \
    -l en-GB \
    --files '['"$RANGE_DONE"']*/**/*.[Mm][Dd]' '['"$RANGE_DONE"']*.[Mm][Dd]'
)