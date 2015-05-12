# events page generator
EVENTS := $(wildcard events/*.html)
events.html :
	cat hacks/head.html >$@
	hacks/events_generator.py $(EVENTS) >>$@
	cat hacks/tail.html >>$@

run :
	python2 -m SimpleHTTPServer

.PHONY: events.html test_head run
