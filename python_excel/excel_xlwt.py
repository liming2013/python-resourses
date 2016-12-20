#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
#create xls object
wb = xlwt.Workbook()
#new sheet
sh = wb.add_sheet('A Test Sheet')
#add data by position
sh.write(0, 0, 1234.56)
sh.write(1, 0, 8888)
sh.write(2, 0, 'hello')
sh.write(2, 1, 'world')
#save
wb.save('example.xls')