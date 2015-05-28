#!/usr/bin/python2
from shifts import Shifts
schedule = Shifts.fetch_schedule()
new_data = []
for date, shifts in schedule['data'].items():
  if Shifts.is_upcoming(date):
    new_data.append({
      'date': date.strftime('%F'),
      'shifts': shifts,
      'is_scheduled': Shifts.is_scheduled(shifts),
    }) 
schedule['data'] = new_data
print schedule
