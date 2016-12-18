#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 10
b = 20

if (a and b):
	print 'all true'
else:
	print 'not all true'

if (a or b):
	print 'at least one of them is true'
else:
	print 'all false'

c = 0

if not (c):
	print 'c is false'
else:
	print 'c is true'
