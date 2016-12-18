# -*- coding:utf-8 -*-
#基本的for循环语句
test_list = [2,"Jone",3,6,7,'hongten','hanyuan','good',"Tom"]
#打印列表的长度
print(len(test_list))

#遍历列表
for i in test_list:
    print(i)

test_str = "hello,i'm hongten"
print('print string: ' + test_str)
#遍历一个字符串
print('Traversal a string')
for i in test_str:
    print(i)
    
test_tuple = [("a",1),("b",2),("c",3),("d",4)]
print(test_tuple)
#遍历一个元组
print('Traversal a tuple ')
for (i,j) in test_tuple:
    print(i,j)

test_dict = {'name':'hongten','age':'20','gender':'M','sports':' football, bingpongball, swimming'}
#字典迭代器
for key  in test_dict:
    print(key + ':' + test_dict[key])
    
L1 = [1,3,5,7]
L2 = [2,4,6,8]
#使用zip将两个列表合并
print(zip(L1,L2))

for (i,j) in zip(L1,L2):
    print(i,j)
print('#######################################################')
L3 = L2[:]
L3.remove(8)
print('L1,L3 list: ')
print(L1)
print(L3)
for (i,j) in zip(L1,L3):
    print(i,j)

#可以看出来当长度不一的时候，多余的被忽略


test_keys = ['name','age','gender','weight','hight']
test_values = ['Hongten','20','M','55','170']
#使用zip来构造一个字典
print('dict\'s keys: ')
print(test_keys)
print('key\'s value:')
print(test_values)
print('after constructing ')
test_dic = dict(zip(test_keys,test_values))
for key in test_dic:
    print( key + ':' + test_dic[key])


'''

D:\Py_exam>python for_ex.py
9
2
Jone
3
6
7
hongten
hanyuan
good
Tom
print string: hello,i'm hongten
Traversal a string
h
e
l
l
o
,
i
'
m

h
o
n
g
t
e
n
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
Traversal a tuple
('a', 1)
('b', 2)
('c', 3)
('d', 4)
gender:M
age:20
name:hongten
sports: football, bingpongball, swimming
[(1, 2), (3, 4), (5, 6), (7, 8)]
(1, 2)
(3, 4)
(5, 6)
(7, 8)
#######################################################
L1,L3 list:
[1, 3, 5, 7]
[2, 4, 6]
(1, 2)
(3, 4)
(5, 6)
dict's keys:
['name', 'age', 'gender', 'weight', 'hight']
key's value:
['Hongten', '20', 'M', '55', '170']
after constructing
gender:M
age:20
name:Hongten
weight:55
hight:170

D:\Py_exam>
'''

'''
Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 


Jone



hongten
hanyuan
good
Tom
打印字符串：hello,i'm hongten
遍历一个字符串
h
e
l
l
o
,
i
'
m
 
h
o
n
g
t
e
n
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
遍历一个元组
a 1
b 2
c 3
d 4
sports:足球，乒乓球，游泳
gender:M
name:hongten
age:20
<zip object at 0x01FA1AA8>
2
4
6
8
#######################################################
L1,L3列表为：
[1, 3, 5, 7]
[2, 4, 6]
2
4
6
字典中的keys：
['name', 'age', 'gender', 'weight', 'hight']
字典中的key对应的value：
['Hongten', '20', 'M', '55', '170']
构造字典后
weight:55
hight:170
gender:M
name:Hongten
age:20
>>>

'''