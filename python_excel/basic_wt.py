#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)  ##第二参数用于确认同一个cell单元是否可以重设值。

sheet.write(0,0,'some text')
sheet.write(0,0,'this should overwrite')   ##重新设置，需要cell_overwrite_ok=True

style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
style.font = font
sheet.write(0, 1, 'some bold Times text', style)

wbk.save('TestData2.xls')    ##该文件名必须存在