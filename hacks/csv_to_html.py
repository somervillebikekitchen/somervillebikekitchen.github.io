#!/usr/bin/python2
import csv
import sys

def parse_csv(csv_file):
  f = open(csv_file)
  rows = csv.reader(f)
  first_row = True
  header_row = []
  data = []
  for row in rows:
    if first_row:
      header_row = row
      first_row = False
    else:
      data.append(row)
  return (header_row, data)

def to_html(header_row, data):
  rows = []
  # header row
  cells = []
  for cell_text in header_row:
    full_cell = '<th>%s</th>' % cell_text
    cells.append(full_cell)
  full_header_row = '<tr>%s</tr>' % ''.join(cells)
  rows.append(full_header_row)
  # data rows
  for row in data:
    cells = []
    for cell_text in row:
      full_cell = '<td>%s</td>' % cell_text
      cells.append(full_cell)
    full_data_row = '<tr>%s</tr>' % ''.join(cells)
    rows.append(full_data_row)
  # add the table tags
  full_table = '<table>%s</table>' % ''.join(rows)
  return full_table

if len(sys.argv) < 2:
  print 'missing argument'
  sys.exit(1)
if len(sys.argv) > 2:
  print 'too many arguments'
  sys.exit(1)

csv_file = sys.argv[1]
header_row, data = parse_csv(csv_file)
print to_html(header_row, data)

