#!/bin/bash
echo "Content-Type: application/javascript"
echo

printf "next_shift("
./next_shift.py --json | tr -d '\n'
printf ");"

echo
