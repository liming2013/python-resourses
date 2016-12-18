#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def changeme(mylist):
   u"修改传入的列表"
   mylist.append([1,2,3,4]);
   print u"函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme(mylist);
print u"函数外取值: ", mylist