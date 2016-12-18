#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

if ( a == b ):
   print ("1 - a=b")
else:
   print ("1 - a!=b")

if ( a != b ):
   print ("2 - a!=b")
else:
   print ("2 - a=b")

if ( a <> b ):
   print ("3 - a!=b")
else:
   print ("3 - a=b")

if ( a < b ):
   print ("4 - a<b" )
else:
   print ("4-a>=b")

if ( a > b ):
   print "5 - a>b"
else:
   print "5 - a<=b"

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if ( a <= b ):
   print "6 - a<=b"
else:
   print "6 - a>b"

if ( b >= a ):
   print "7 - b>=b"
else:
   print "7 - b<b"