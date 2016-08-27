import datetime, xmlrpclib

wp_username = "username"
wp_password = "password"
wp_blogid = ""
wp_url = "https://{}.wordpress.com/xmlrpc.php".format(wp_username)

status_draft = 0
status_published = 1

server = xmlrpclib.ServerProxy(wp_url)

import time
now = time.time()
title = "Title with spaces"
content = "Body with lots of content"
date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2009-10-20 21:08", "%Y-%m-%d %H:%M"))
categories = ["somecategory"]
tags = ["sometag", "othertag"]
data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
print "time:", (time.time() - now)