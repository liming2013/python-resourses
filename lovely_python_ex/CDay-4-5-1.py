 # coding : utf-8
import os

export = ""
for files in os.walk("D:\Py_exam\lovely_python_ex"):
	export+="\n %s" % (files)
open('file_list_2_2', 'w').write(export)
