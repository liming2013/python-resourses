#! -*- encoding:utf-8 -*-

import urllib
import urllib2

handler = urllib2.FileHandler()
request = urllib2.Request(url='file:/D:\Py_exam\python_ex\url_open.py')
opener = urllib2.build_opener(handler)
f = opener.open(request)
print f.read()



f = urllib.urlopen(url='file:/D:\Py_exam\python_ex\url_open.py')
print f.read()
