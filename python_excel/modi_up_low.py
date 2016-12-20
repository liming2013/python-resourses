#!/usr/bin/python
# -*- coding: UTF-8 -*-
#读必须从原表中读取，写必须写入拷贝的表中。 下面是一个修改已存在excel的实例：修改t2.xls，并将里面小写字母变成大写字母
import xlrd
from xlutils.copy import copy

#打开excel文档并将内容读取到内存
readbook = xlrd.open_workbook('test.xls')
#将excel内容拷贝一份
copybook = copy(readbook)

for i in range(len(readbook.sheets())) :
  '''
  遍历excel文档中的每个工作表，进行下面的处理
  '''
  #获得拷贝excel中的表i
  sheet = copybook.get_sheet(i)
  #获取原excel文档中的表i
  readSheet = readbook.sheet_by_index(i)

  for row in range(readSheet.nrows) :
    '''
    对表i中的单元格数据做如下处理
    '''
    for col in range(readSheet.ncols) :
      cell = readSheet.cell(row, col).value
      print "type is :", type(cell),cell
      if type(cell) in (str, unicode) :
        '''
        判断一下读取出来的单元格数据格式，
        如果为str和unicode的字符串，就调用字符串的upper函数，
        执行大小写转换 
        '''
        #res = cell.upper()#把小些改大写
        res = cell.lower()#把大些改小写
        sheet.write(row, col, res)#将修改的内容写入拷贝的excel中
      #sheet.write(row, col, '中文'.decode('GBK'))
#将拷贝的excel保存并覆盖原来的excel文件
copybook.save('test.xls')