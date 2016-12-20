#from https://zhuanlan.zhihu.com/p/22261597
import xlrd
#open a xls file
book = xlrd.open_workbook("test.xls")
print "number:", book.nsheets
print "name:", book.sheet_names()
#get first sheet
sh = book.sheet_by_index(0)
print u"list %s there are all %d lines %d columns\n" % (sh.name, sh.nrows, sh.ncols)
print "line 2 column 3:", sh.cell_value(1, 2)
#Traversal all datas
for s in book.sheets():
    for r in range(s.nrows):
        print s.row(r)
	print '\n'