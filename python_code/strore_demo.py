#!/usr/bin/python
#encoding:utf-8

#in version 2 using 'import urllib'

#for version python 3


import urllib.request
import os
def Schedule(a,b,c):
    '''''
    a:data downloaded
	b:size of data block
    c:size of remote file
    '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print ('%.2f%%' % per)

url = 'http://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz'
local = os.path.join('d://python_ex','python-3.5.2.tar.xz')
urllib.request.urlretrieve(url,local,Schedule)
#in version 2 using 'urllib.urlretrieve'
print ('tar.xz file download complete')

url2 = 'http://www.python.org/ftp/python/3.5.2/python-3.5.2-embed-win32.zip'
local = os.path.join('d://python_ex','python-3.5.2-embed-win32.zip')
urllib.request.urlretrieve(url2,local,Schedule)
print ('zip file download complete')