# events page generator
EVENTS := $(wildcard events/*.html)
events.html :
	cat hacks/head.html >$@
	hacks/events_generator.py $(EVENTS) >>$@
	cat hacks/tail.html >>$@

run :
	@echo "navigate to http://localhost:8000/"
	python2 -m SimpleHTTPServer

test : 
	hacks/tests.sh

.PHONY: events.html test run
