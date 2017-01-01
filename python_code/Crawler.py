#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
page=urllib2.urlopen("http://www.baidu.com")
print page.read()