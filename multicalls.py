import datetime, xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

wp_username = "username"
wp_password = "password"
wp_blogid = "1"
wp_url = "https://{}.wordpress.com/xmlrpc.php".format(wp_username)

status_draft = 0
status_published = 1

# server = xmlrpclib.ServerProxy(wp_url)
server = xmlrpclib.ServerProxy(wp_url)
multicall = xmlrpclib.MultiCall(server)

import time
now = time.time()
for i in range(12):
	title = "title {}".format(i)
	content = "content {}".format(i)
	# date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2009-10-20 21:08", "%Y-%m-%d %H:%M"))
	post_type = "post"
	# categories = ["somecategory"]
	# tags = ["sometag", "othertag"]
	# data = {'title': title, 'description': content, 'post_type':post_type,'categories': categories, 'mt_keywords': tags}
	data = {'title': title, 'description': content, 'post_type':post_type}
	print data
	multicall.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)

result = multicall()
time_took = (time.time() - now)
print "time:", time_took
with open("time.txt", "a") as F:
	F.write("time: {}".format((time_took)))