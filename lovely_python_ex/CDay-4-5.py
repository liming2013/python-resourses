#!/usr/bin/python
# coding : utf-8
import os

export = ""
for root, dirs, files in os.walk("D:\Py_exam\lovely_python_ex"):
	export+="\n %s;%s;%s" % (root,dirs,files)
open('file_list_2', 'w').write(export)
print 'hello usr/bin/python'
