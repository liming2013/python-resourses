#!/usr/bin/python
# -*- coding: UTF-8 -*-
#for version python 3
import urllib.request
def cbk(a, b, c):  
    '''''
    a:data downloaded
	b:size of data block
    c:size of remote file
    ''' 
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print ('%.2f%%' % per)
  
url = 'https://www.baidu.com'
local = 'd://baidu.html'
urllib.request.urlretrieve(url, local, cbk)
