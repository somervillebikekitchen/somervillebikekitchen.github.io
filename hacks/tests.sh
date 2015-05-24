#!/bin/bash
error=0
# test head and tail
head_lines=$(wc -l hacks/head.html | cut -d' ' -f1)
tail_lines=$(wc -l hacks/tail.html | cut -d' ' -f1)
for f in $(find -iname '*.html' | grep -v '^./hacks'); do
  printf "testing $f..."
  (echo "$(head -n $head_lines "$f")"; echo) | diff -u hacks/head.html - >/dev/null || \
  (echo "$(tail -n $tail_lines "$f")"; echo) | diff -u hacks/tail.html - >/dev/null
  if [[ $? -ne 0 ]]; then
    error=1
    echo '[FAILED]'
  else
    echo
  fi
done
exit $error
