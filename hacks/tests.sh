#!/bin/bash
error=0
# test head and tail
head_lines=$(wc -l <hacks/head.html)
tail_lines=$(wc -l <hacks/tail.html)
for f in $(find -iname '*.html' | grep -v '^./hacks'); do
  printf "testing $f..."

  echo "$(head -n $head_lines "$f")" | cmp hacks/head.html - >/dev/null 2>&1
  if [[ $? -ne 0 ]]; then
    error=1
    echo '[FAILED] (check head)'
    continue
  fi

  echo "$(tail -n $tail_lines "$f")" | cmp hacks/tail.html - >/dev/null 2>&1
  if [[ $? -ne 0 ]]; then
    error=1
    echo '[FAILED] (check tail)'
    continue
  fi

  echo '[OK]'
done
if [[ $error -eq 1 ]]; then
  echo
  echo 'Some tests failed.'
fi
exit $error
