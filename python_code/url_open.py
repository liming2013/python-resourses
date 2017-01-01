#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
f = urllib.urlopen('http://global.bing.com/')
firstLine = f.readline()   #读取html页面的第一行
print firstLine
