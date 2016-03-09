#!/usr/bin/python2
from shifts import Terms
import json
terms = Terms.fetch_terms()
data = {}
for member, date in terms.iteritems():
  data[member] = date.strftime('%F');
print json.dumps(data)
