#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
f = urllib.urlopen('http://www.baidu.com/')
firstLine = f.readline()   #读取html页面的第一行
allLine = f.readlines()
print firstLine
print '\n===============\n'
print allLine
