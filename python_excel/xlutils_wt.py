#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt #写入数据
from xlutils.copy import copy
from xlrd import open_workbook
#----xlrd库
#打开excel文件
workbook = open_workbook('example.xls')
#获取表单
worksheet = workbook.sheet_by_index(0)
#读取数据
data = worksheet.cell_value(0,0)

#----xlwt库
#新建excel
wb = xlwt.Workbook()
#添加工作薄
sh = wb.add_sheet('demo_lm')
#写入数据
sh.write(0,0,'data')
#保存文件
wb.save('example.xls')

#----xlutils库
#打开excel文件
book = open_workbook('example.xls')
#复制一份
new_book = copy(book)

#添加工作薄
sh2 = new_book.add_sheet('demo_22')

#拿到工作薄
worksheet = new_book.get_sheet(1)
#写入数据
worksheet.write(0,0,'new data')
#保存
new_book.save('example.xls')