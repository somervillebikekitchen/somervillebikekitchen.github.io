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
schedule['data'] = sorted(new_data, key=lambda y: y['date'])
print schedule
