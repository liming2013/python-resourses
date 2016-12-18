#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
tuple_t = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = ('john')
tinytuple_t = ('john',70.2)
c = 'liming'
d = 'l'

if ( tinytuple_t in tuple_t ):
	print "tinytuple_t in the tuple tuple_t"
else:
	print "tinytuple_t not in the tuple tuple_t"

if ( tinytuple in tuple_t ):
	print "tinytuple in the tuple tuple_t"
else:
	print "tinytuple not in the tuple tuple_t"

if ( d in c ):
   print "d in the string c"
else:
   print "d not in the string c"

if ( a in list ):
   print "a in the list"
else:
   print "a not in the list"

if ( b not in list ):
   print "b not in the list"
else:
   print "b in the list"

# change the value of a
a = 2
if ( a in list ):
   print "a in the list"
else:
   print "a not in the list"