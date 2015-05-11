#!/usr/bin/python2
import sys
from HTMLParser import HTMLParser

EVENT_TAGS = [
  'event_title',
  'event_datetime',
  'event_description',
]

EVENT_TEMPLATE = """
<li>
<h3><a href="/%(page_name)s">%(event_title)s</a></h3> (%(event_datetime)s)
<p>%(event_description)s</p>
</li>
"""[1:-1]

class EventPageParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    for attr in attrs:
      if attr[0] == 'id' and attr[1] in EVENT_TAGS:
        self.event_tag = attr[1]
        break
  def handle_endtag(self, tag):
    self.event_tag = None
  def handle_data(self, data):
    if self.event_tag:
      self.event_info[self.event_tag] = data
  def init(self):
    self.event_tag = None
    self.event_info = {}

events = []

for event_page_filename in sys.argv[1:]:
  f = open(event_page_filename, 'r')
  html = f.read(1048576)
  evparser = EventPageParser()
  evparser.init()
  evparser.feed(html)
  evparser.event_info['page_name'] = event_page_filename
  events.append(evparser.event_info)

print '<ul class="event-list">'
for event in sorted(events, key=lambda e: e['event_datetime']):
  print EVENT_TEMPLATE % event
print '</ul>'
