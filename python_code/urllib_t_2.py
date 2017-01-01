#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib

local = 'd://baidu.html'
url = 'https://www.baidu.com'
urllib.urlretrieve(url, local)
#response = urllib2.urlopen(request)
#print response.read()