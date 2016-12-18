def Inc(x):
	x = x + 1
	return x

def Append(x):
	x.append(100)
	return x

x = 100
y = Inc(x)
print "x: ", x
print "y: ", y

x = [1, 2, 3]
y = Append(x)
print "x: ", x
print "y: ", y