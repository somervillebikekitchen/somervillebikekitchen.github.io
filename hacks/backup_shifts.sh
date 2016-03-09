#!/bin/bash
date=$(date --iso)
wget -O sbk_shifts_$date.csv http://sbk.sankey.info/calc/dewxjhhcc2.csv
wget -O sbk_terms_$date.csv http://sbk.sankey.info/calc/sbk_start_dates.csv

