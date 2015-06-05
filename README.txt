###############################
#  How to create a new event  #
###############################

1. Copy an existing event page into a new html file:

   cp events/first_open_shop.html events/new_event.html

2. In the new event page, replace the title, date, description, etc.  Be sure
   not to remove or modify the id attributes.  For example, here is what the
   new html might look like:

   <h3 id="event_title">Example Event Title</h3>
   <p id="event_datetime">2015-06-24 18:00-21:00</p>
   <p id="event_description">Example short description.</p>

   <p>Longer description, in paragraph form.<p>

3. generate the events page:

   make events.html

##################################
#  How to update the tools page  #
##################################

1. Update tools.csv with the new tools information.  You can open this file in
   a CSV editor such as LibreOffice.

2. generate the tools page:

   make tools.html
