#!/bin/bash
echo "Content-Type: application/javascript"
echo

printf "unscheduled("
./next_shift.py --json --unscheduled | tr -d '\n'
printf ");"

echo
