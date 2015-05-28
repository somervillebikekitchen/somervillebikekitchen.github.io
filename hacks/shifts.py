import urllib2
import csv
import datetime

SHIFTS_CSV_URL = 'http://sbk.sankey.info/calc/dewxjhhcc2.csv'
NUM_STAFF = 8

class Shifts:
  @staticmethod
  def get_row_shifts(row):
    '''get shfits from full spreadsheet row'''
    return row[2:2+NUM_STAFF-1]
  
  @staticmethod
  def parse_header(row):
    '''parse the header row, return a list of staff members in order'''
    return Shifts.get_row_shifts(row)
  
  @staticmethod
  def parse_row(row):
    '''parse all relevant information in a full spreadsheet data row'''
    try: days_since_1900 = int(row[0])
    except: return None, None
    row_date = datetime.date(1899,12,30) + datetime.timedelta(days=days_since_1900)
    row_shifts = Shifts.get_row_shifts(row)
    return row_date, row_shifts
  
  @staticmethod
  def is_upcoming(date):
    today = datetime.date.today()
    return date >= today
  
  @staticmethod
  def is_scheduled(shifts):
    return '1' in shifts
  
  @staticmethod
  def get_scheduled_staff(shifts, all_staff):
    return [y[1] for y in zip(shifts, all_staff) if y[0] == '1']
  
  @staticmethod
  def fetch_schedule():
    f = urllib2.urlopen(SHIFTS_CSV_URL)
    rows = csv.reader(f)
    first_row = True
    all_staff = []
    data = {}
    for row in rows:
      if first_row:
        all_staff = Shifts.parse_header(row)
        first_row = False
      else:
        date, shifts = Shifts.parse_row(row)
        if not date: break
        data[date] = shifts
    return {
      'all_staff': all_staff,
      'data': data,
    }
