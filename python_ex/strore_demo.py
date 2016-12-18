#!/usr/bin/python
#encoding:utf-8

#in version 2 using 'import urllib'

#for version python 3


#import urllib.request
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

#url = 'http://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz'
#local = os.path.join('d://python_ex','python-3.5.2.tar.xz')
##urllib.request.urlretrieve(url,local,Schedule)
#urllib.request.urlretrieve(url,local,Schedule)
##in version 2 using 'urllib.urlretrieve'
#print ('tar.xz file download complete')

url2 = 'https://sourceforge.net/projects/gnuplot/files/gnuplot/5.0.4/gp504-win32-mingw.zip/download'
local = os.path.join('d://Py_exam','gp504-win32-mingw.zip.zip')
urllib.urlretrieve(url2,local,Schedule)
print ('zip file download complete')