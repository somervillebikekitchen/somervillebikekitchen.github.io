#!/usr/bin/python2
import urllib2
import csv
import datetime
import sys

SHIFTS_CSV_URL = 'http://sbk.sankey.info/calc/dewxjhhcc2.csv'
NUM_STAFF = 8
NUM_UNSCHEDULED = 2

if '--help' in sys.argv:
  print 'usage: %s [--help] [--json] [--unscheduled]' % sys.argv[0]
  sys.exit(0)

def get_row_shifts(row):
  column_first_person = 3
  return row[column_first_person:column_first_person+NUM_STAFF-1]

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
  for i in range(0,len(shifts)-1):
    try:
      scheduled = int(shifts[i])
    except:
      scheduled = 0
    if scheduled > 0:
      staff.append(all_staff[i])
  return staff

def is_scheduled(shifts):
  return '1' in shifts

def get_next_shift():
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
        return '%d days from today (%s) the following staff members are scheduled: %s' % (
          (date - datetime.date.today()).days,
          date.strftime('%F'),
          ','.join(get_staff_names(shifts, all_staff)))
    i += 1

def get_unscheduled():
  f = urllib2.urlopen(SHIFTS_CSV_URL)
  rows = csv.reader(f)
  all_staff = []
  unscheduled = []
  r = 0
  n = 0
  for row in rows:
    if r == 0:
      all_staff = get_row_shifts(row)
    else:
      date, shifts = parse_row(row)
      if is_upcoming(date) and not is_scheduled(shifts):
        unscheduled.append('%s (%s) %d days from now!' % (
          date.strftime('%F'),
          date.strftime('%A'),
          (date - datetime.date.today()).days))
        n += 1
        if n >= NUM_UNSCHEDULED: break
    r += 1
  return unscheduled

if '--unscheduled' in sys.argv:
  if '--json' in sys.argv:
    print "{\"message\":[\"%s\"]}" % '","'.join(get_unscheduled())
  else:
    print '\n'.join(get_unscheduled())
else:
  if '--json' in sys.argv:
    print "{\"message\":\"%s\"}" % get_next_shift()
  else:
    print get_next_shift()

