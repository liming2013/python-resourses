#! -*- encoding:utf-8 -*-

import urllib
import urllib2

handler = urllib2.FTPHandler()
#get the ftp list without username and password
request = urllib2.Request(url='ftp://mirrors.ustc.edu.cn/debian-cd/')
opener = urllib2.build_opener(handler)
f = opener.open(request)
print f.read()


f = urllib.urlopen(url='ftp://mirrors.ustc.edu.cn/')
print f.read()


f = urllib.urlopen(url='http://ftp.ntua.gr/pub/devel/pythonxy/')
print f.read()