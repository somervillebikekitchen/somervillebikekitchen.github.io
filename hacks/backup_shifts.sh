#!/bin/bash
date=$(date --iso)
wget -O sbk_shifts_$date.csv http://sbk.sankey.info/calc/dewxjhhcc2.csv
