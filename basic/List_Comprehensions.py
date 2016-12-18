squared = [x ** 2 for x in range(4)]
for i in squared:
	print i
print 'hello'
num = [x for x in range(4)]
for i in num:
	print i
print 'hello'
sqdEvens = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEvens:
	print i