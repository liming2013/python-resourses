#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
baidu = urllib.urlopen('http://www.baidu.com')
print 'http header:\n',baidu.info()
print 'http status:',baidu.getcode()
print 'url:', baidu.geturl()
for line in baidu:
    print line,
baidu.close()