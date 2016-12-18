#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
content_stream = urllib2.urlopen('http://www.baidu.com/')
content = content_stream.read()
print content