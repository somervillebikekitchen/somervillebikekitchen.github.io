#####################################
#  How to create a new photo album  #
#####################################

1. Create a new album directory under albums/ , e.g.:

   mkdir albums/2019-01-20_my_new_album

2. Create a new index.html for that album:

   echo "---
layout: album
title: 2019-01-20_my_new_album
---" > albums/2019-01-20_my_new_album/index.html

3. Add image files to the new album directory.

4. add, commit, and push.

###############################
#  How to create a new event  #
###############################

1. Copy an existing event page into a new html file:

   cp events/first_open_shop.html events/new_event.html

2. In the new event page, replace the title, date, description, etc.

3. add, commit, and push

##################################
#  How to update the tools page  #
##################################

1. Update tools.csv with the new tools information.  You can open this
   file in a CSV editor such as LibreOffice.

2. generate the tools page:

   make tools.html

3. add, commit, and push
