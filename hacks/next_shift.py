#!/usr/bin/python2
import urllib2
import csv
import datetime

SHIFTS_CSV_URL = 'http://sbk.sankey.info/calc/dewxjhhcc2.csv'
NUM_STAFF = 8

def get_row_shifts(row):
  return row[2:2+NUM_STAFF-1]

def parse_row(row):
  try:
    days_since_1900 = int(row[0])
  except:
    return None, None
  shop_date = datetime.date(1899,12,30) + datetime.timedelta(days=days_since_1900)
  return shop_date, get_row_shifts(row)

def is_upcoming(date):
  today = datetime.date.today()
  return date >= today

def get_staff_names(shifts, all_staff):
  staff = []
  for i in range(0,NUM_STAFF-1):
    try:
      scheduled = int(shifts[i])
    except:
      scheduled = 0
    if scheduled > 0:
      staff.append(all_staff[i])
  return staff

f = urllib2.urlopen(SHIFTS_CSV_URL)
rows = csv.reader(f)
i = 0
all_staff = []
for row in rows:
  if i == 0:
    all_staff = get_row_shifts(row)
  else:
    date, shifts = parse_row(row)
    if is_upcoming(date):
      print '%d days from today (%s) the following staff members are scheduled: %s' % (
        (date - datetime.date.today()).days,
        date.strftime('%F'),
        ','.join(get_staff_names(shifts, all_staff)))
      break
  i += 1
