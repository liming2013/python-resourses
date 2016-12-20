#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt,xlrd

xlsfile = r'D:\python_excel\example.xls'
book = xlrd.open_workbook(xlsfile)     #获得excel的book对象

#获取sheet对象，方法有2种：
sheet_name=book.sheet_names()[0]          #获得指定索引的sheet名字
print sheet_name

sheet1=book.sheet_by_name(sheet_name)  #通过sheet名字来获取，当然如果你知道sheet名字了可以直接指定
sheet0=book.sheet_by_index(0)     #通过sheet索引获得sheet对象