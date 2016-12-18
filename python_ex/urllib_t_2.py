#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib

local = 'd://google.html'

url = 'http://www.google.com/'
urllib.urlretrieve(url, local)
#response = urllib2.urlopen(request)
#print response.read()