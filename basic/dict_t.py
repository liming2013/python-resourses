#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'wd':'liming','name':'john','code':6734,'dept':'sales'}


print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值

dict_2 = {'Name': 'Zara', 'Age': 7}
print "Equivalent String : %s" % str (dict_2)
print "Variable Type : %s" %  type (dict_2)

print'================'
seq = ('name', 'age', 'sex')

#dict_3 = dict.fromkeys(seq)
#print "New Dictionary : %s" %  str(dict_3)

dict_3 = dict.fromkeys(seq, 10)
print "New Dictionary : %s" %  str(dict_3)

print "Value : %s" %  dict_3.items()

dict_3.update(dict_2)
print "Value : %s" %  dict_3

print "Value : %s" %  dict_3.values()