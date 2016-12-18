f=open('file_list_2','a')
f.write('hello')
f.write('iplay')
f.close()

f1=open('file_list_2','r')
a=f1.read(100)
print "Read Line: %s" % (a)   