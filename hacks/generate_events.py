#!/usr/bin/python2
import sys
from HTMLParser import HTMLParser
from string import split

EVENT_TEMPLATE = """
<li>
<h3><a href="/%(filename)s">%(title)s</a></h3> (%(datetime)s)
<p>%(description)s</p>
</li>
"""[1:-1]

class EventPageParser:
  def __init__(self):
    self.event_info = {
      'title': '',
      'datetime': '',
      'description': '',
    }
  def feed(self, text):
    text = text.split('\n')
    for line in text[1:]:
      if line.strip() == '---': break
      key,value = split(line, ':', maxsplit=1)
      key = key.strip()
      value = value.strip()
      self.event_info[key] = value

events = []

for event_page_filename in sys.argv[1:]:
  f = open(event_page_filename, 'r')
  html = f.read(1048576)
  evparser = EventPageParser()
  evparser.feed(html)
  evparser.event_info['filename'] = event_page_filename
  events.append(evparser.event_info)

print '<ul class="event-list">'
for event in sorted(events, key=lambda e: e['datetime']):
  print EVENT_TEMPLATE % event
print '</ul>'
