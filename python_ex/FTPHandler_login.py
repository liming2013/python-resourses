#! -*- encoding:utf-8 -*-

import urllib2

handler = urllib2.FTPHandler()
request = urllib2.Request(url='ftp://用户名:密码@ftp地址/')
opener = urllib2.build_opener(handler)
f = opener.open(request)
print f.read()