#!/usr/bin/python
# -*- coding: UTF-8 -*-
#for version python 3
import urllib.request

filename = urllib.request.urlretrieve('https://www.baidu.com/')
print ('\n**************\n')
print ('%s',type(filename))
print ('\naaaaaaaaaaaaa\n')
print (filename[0])
print ('\n===============\n')
print (filename[1])