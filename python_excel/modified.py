#!/usr/bin/python
# -*- coding: UTF-8 -*-
#u很遗憾，并没有直接修改 xls 文件的方法。通常的做法是，读取出文件，复制一份数据，对其进行修改，再保存。在复制时，需要用到xlutils 中的方法。 
from xlrd import open_workbook
from xlutils.copy import copy
#open a file
rb = open_workbook("example.xls")
#copy
wb = copy(rb)
#select a sheet
s = wb.get_sheet(0)
#write the data
#s.write(0, 1, 'new data')
s.write(1,1,'2016-12-20')
#save
wb.save('example.xls')
