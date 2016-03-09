#!/usr/bin/python2
from shifts import Terms
import json
import datetime
terms = Terms.fetch_terms()
data = {}
for member, join_date in terms.iteritems():
  data[member] = {}
  data[member]['start_date'] = join_date.strftime('%F')
  data[member]['current_term'] = Terms.current_term_start(join_date).strftime('%F')
print json.dumps(data)
