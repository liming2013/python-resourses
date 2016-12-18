#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib

filename = urllib.urlretrieve('https://www.baidu.com/')
print ('\n**************\n')
print ('%s',type(filename))
print ('\naaaaaaaaaaaaa\n')
print (filename[0])
print ('\n===============\n')
print (filename[1])