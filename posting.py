from wordpress_xmlrpc import Client, WordPressPost, WordPressPage
from wordpress_xmlrpc.methods.posts import NewPost

#authenticate
wp_username = "username"
wp_password = "password"
wp_url = "https://{}.wordpress.com/xmlrpc.php".format(wp_username)

print "authenticating",wp_username
wp = Client(wp_url, wp_username, wp_password)

#post and activate new post
# Checking time for post
import time
now = time.time()
for i in range(10):
	print "posting"
	post = WordPressPost()
	post.title = 'My post'
	post.content = 'This is a wonderful blog post about XML-RPC.'
	post.post_status = 'publish'
	wp.call(NewPost(post))
	
print "posting done"
print (time.time() - now)


