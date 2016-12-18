#! -*- encoding:utf-8 -*-

import urllib
import urllib2

opener = urllib2.OpenerDirector()
handler = urllib2.HTTPHandler()
opener.add_handler(handler)
content_stream = opener.open('http://www.baidu.com/')
print content_stream.read()



#another method using add proxy
f = urllib.urlopen(url='http://www.baidu.com/', proxies={'has_key' : 'http://216.66.205.76:8080/'})

print f.read()
