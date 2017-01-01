#coding=gbk
import httplib
conn = httplib.HTTPConnection("www.baidu.com")
conn.request('get', '/')
print  conn.getresponse().read()
conn.close()