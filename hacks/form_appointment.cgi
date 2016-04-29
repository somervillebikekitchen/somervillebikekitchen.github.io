#!/usr/bin/python

import sys
import os
import subprocess
import cgi
import cgitb
cgitb.enable()
import pytz
from datetime import datetime
from form_appointment.conf.py import MSMTP_CONFIG, SBK_STAFF_ADDRESS, MAILER_ADDRESS, HUMANS_SAY

def error_and_exit(problems):
  print "Content-Type: text/plain"
  print
  print '\n'.join(problems)
  sys.exit(0)

form = cgi.FieldStorage()

# validate the form
problems = []
if 'human' not in form:
  problems.append('Not a human?')
else:
  human_answer = form['human'].value.strip(' ').lower()
  if human_answer not in HUMANS_SAY:
    problems.append('Not a human?')
if 'description' not in form:
  problems.append('Please fill in a description')
if 'name' not in form:
  problems.append('Please fill in your name')
if 'email' not in form:
  problems.append('Please fill in your email')
if 'date' not in form:
  problems.append('Please provide a date')
if len(problems) != 0:
  error_and_exit(problems)

# clean the form
form_cleaned = {
  'description': form['description'].value,
  'name': form['name'].value,
  'email': form['email'].value,
  'date': form['date'].value,
}
if 'message' in form:
  form_cleaned['message'] = form['message'].value

mail_conf = {
  'To': SBK_STAFF_ADDRESS,
  'From': MAILER_ADDRESS,
  'Subject': 'New appointment request: %(name)s' % form_cleaned,
  'Date':
    datetime.utcnow().replace(tzinfo = pytz.utc).strftime('%a, %d %b %Y %T %z'),
  'Body': '''
Somebody has requested an appointment!  See details below.

name: %(name)s
email: %(email)s
date: %(date)s

----- begin message -----
%(description)s

%(message)s
----- end message -----

---
SBK appointment system
''' % form_cleaned,
}

mail_envelope = '''Date: %(Date)s
From: %(From)s
To: %(To)s
Subject: %(Subject)s

%(Body)s
''' % mail_conf

p = subprocess.Popen(
  '/usr/bin/msmtp --file="%s" -t' % MSMTP_CONFIG,
  stdin=subprocess.PIPE,
  stdout=subprocess.PIPE,
  stderr=subprocess.PIPE,
  close_fds=True,
  shell=True)
p.stdin.write(mail_envelope)
p.stdin.close()
output = p.stdout.read()
p.stdout.close()
output += p.stderr.read()
p.stderr.close()
p.poll()
rc = p.returncode
if rc is not None and rc >> 8:
  error_and_exit('problem sending mail')

#print "Thank you for your submission!  SBK staff have been notified"
print "Location: /appointment/thanks.html"
print
