from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

#authenticate
wp_username = "username"
wp_password = "password"
wp_url = "https://{}.wordpress.com/xmlrpc.php".format(wp_username)

print "authenticating",wp_username
wp = Client(wp_url, wp_username, wp_password)

#post and activate new post
print "posting"
post = WordPressPost()
post.title = 'My post'
post.content = 'This is a wonderful blog post about XML-RPC.'
post.post_status = 'publish'
post.terms_names = {
  'post_tag': ['test', 'firstpost'],
  'category': ['Introductions', 'Tests']
}
wp.call(NewPost(post))