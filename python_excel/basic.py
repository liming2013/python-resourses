#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd                    #导入xlrd模块

#打开指定文件路径的excel文件

xlsfile = r'D:\AutoPlan\apisnew.xls' 
book = xlrd.open_workbook(xlsfile)     #获得excel的book对象

#获取sheet对象，方法有2种：
sheet_name=book.sheet_names()[0]          #获得指定索引的sheet名字
print sheet_name
sheet1=book.sheet_by_name(sheet_name)  #通过sheet名字来获取，当然如果你知道sheet名字了可以直接指定
sheet0=book.sheet_by_index(0)     #通过sheet索引获得sheet对象

#获取行数和列数：

nrows = sheet.nrows    #行总数
ncols = sheet.ncols   #列总数

#获得指定行、列的值，返回对象为一个值列表

row_data = sheet.row_values(0)   #获得第1行的数据列表
col_data = sheet.col_values(0)  #获得第一列的数据列表，然后就可以迭代里面的数据了

#通过cell的位置坐标获得指定cell的值
cell_value1 = sheet.cell_value(0,1)  ##只有cell的值内容，如：http://xxx.xxx.xxx.xxx:8850/2/photos/square/
print cell_value1
cell_value2 = sheet.cell(0,1) ##除了cell值内容外还有附加属性，如：text:u'http://xxx.xxx.xxx.xxx:8850/2/photos/square/'
print cell_value2