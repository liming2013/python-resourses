#!/usr/bin/python
#encoding:utf-8

#in version 2 using 'import urllib'
import urllib
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

url='https://go.microsoft.com/fwlink/?LinkID=623231'

#url = 'http://code.visualstudio.com/docs/?dv=winzip'

local = os.path.join('d://python_ex','winzip.zip')
urllib.urlretrieve(url,local,Schedule)
print ('file download complete')

#url2 = 'http://www.python.org/ftp/python/3.5.2/python-3.5.2-embed-win32.zip'
#local = os.path.join('d://python_ex','python-3.5.2-embed-win32.zip')
#urllib.urlretrieve(url2,local,Schedule)
#print ('zip file download complete')