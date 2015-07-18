GENERATED_PAGES := events.html tools.html

default : $(GENERATED_PAGES)
	@echo "All pages generated successfully!"

run : $(GENERATED_PAGES)
	@echo "**********************************"
	@echo "navigate to http://localhost:8000/"
	@echo "**********************************"
	jekyll --server 8000

# events page generator
EVENT_PAGES := $(wildcard events/*.html)
events.html : $(EVENT_PAGES)
	@echo "---" >$@
	@echo "layout: default" >>$@
	@echo "title: Events" >>$@
	@echo "---" >>$@
	@hacks/generate_events.py $(EVENT_PAGES) >>$@
	@echo "Events page successfully created."

# tools page generator
tools.html : tools.csv
	@echo "---" >$@
	@echo "layout: default" >>$@
	@echo "title: Tools" >>$@
	@echo "---" >>$@
	@hacks/generate_tools.sh $< >>$@
	@echo "Tools page successfully created."

.PHONY: run
