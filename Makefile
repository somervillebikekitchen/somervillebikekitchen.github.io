GENERATED_PAGES := events.html tools.html

default : $(GENERATED_PAGES)
	@echo "All pages generated successfully!"

run : $(GENERATED_PAGES)
	@echo "**********************************"
	@echo "navigate to http://localhost:8000/"
	@echo "**********************************"
	jekyll serve --port 8000 || jekyll --server 8000

# tools page generator
tools.html : tools.csv
	@echo "---" >$@
	@echo "layout: default" >>$@
	@echo "title: Tools" >>$@
	@echo "---" >>$@
	@hacks/generate_tools.sh $< >>$@
	@echo "Tools page successfully created."

.PHONY: run
