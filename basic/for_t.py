#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':     # 第一个实例
   print 'current letter:', letter

fruits = ['banana', 'apple',  'mango']
for s in fruits:        # 第二个实例
   print 'current fruit:', s

print "Good bye!"


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'current fruit:', fruits[index]

print "Good bye!"


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d = %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, 'is a prime number\n'
'''
10 等于 2 * 5
11 是一个质数
12 等于 2 * 6
13 是一个质数
14 等于 2 * 7
15 等于 3 * 5
16 等于 2 * 8
17 是一个质数
18 等于 2 * 9
19 是一个质数
'''

for i in range(5):
    print i
    i += 2
    print i
    print 'loop over'
	
print'\n============\n'	 
 
i = 0
while i < 5:
    print i
    i += 2
    print i
    print 'loop over'
	

