for eachNum in [0,1,2]:
	print eachNum
print
for eachNum in range(5):
	print eachNum
print

foo = 'abc-dcv'
for c in foo:
	print c,
print '\nHW'
print	#to generator a new line famaliar with'\n'
foo = 'abc-dcv'
for c in foo:
	print c+'c',

for i in range(len(foo)):
	print foo[i], '(%d)' % i
print 'HW'
for i, ch in enumerate(foo):
	print ch, '(%d)' % i
