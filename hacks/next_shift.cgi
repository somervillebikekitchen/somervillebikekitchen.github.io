#!/bin/bash
echo "Content-Type: text/plain"
echo

printf "next_shift("
./next_shift.py --json | tr -d '\n'
printf ")"

echo
