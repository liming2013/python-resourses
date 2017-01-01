#!/usr/bin/python
#encoding:utf-8

#in version 2 using 'import urllib'
import urllib
data = 'name = ~nowamagic+5'
  
data1 = urllib.quote(data)
print data1, '\n' # result: name%20%3D%20%7Enowamagic%2B5
print urllib.unquote(data1),'\n' # name = ~nowamagic+5
  
data2 = urllib.quote_plus(data)
print data2, '\n' # result: name+%3D+%7Enowamagic%2B5
print urllib.unquote_plus(data2), '\n'    # name = ~nowamagic+5
  
data3 = urllib.urlencode({ 'name': 'nowamagic-gonn', 'age': 200 })
print data3, '\n' # result: age=200&name=nowamagic-gonn
  
data4 = urllib.pathname2url(r'd:/a/b/c/23.php')
print data4, '\n' # result: ///D://a/b/c/23.php
print urllib.url2pathname(data4), '\n'    # result: D:/a/b/c/23.php