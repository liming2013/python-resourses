import numpy as np
# Let's make 2 arrays (x, y) which we will write to a file
# x is an array containing numbers 0 to 10, with intervals of 1
x = np.arange(0.0, 10., 1.)
# y is an array containing the values in x, squared
y = x*x
print 'x = ', x
print 'y = ', y
# Now open a file to write the data to
# 'w' means open for 'writing'
file = open('testdata.txt', 'w')
# loop over each line you want to write to file
for i in range(len(x)):
    # make a string for each line you want to write
    # '\t' means 'tab'
    # '\n' means 'newline'
    # 'str()' means you are converting the quantity in brackets to a string type
    txt = str(x[i]) + '\t' + str(y[i]) + ' \n'
    # write the txt to the file
    file.write(txt)
# Close your file
file.close()