# _*_ coding:utf-8 _*_
import os
for root,dirs,files in os.walk("D:\\Py_exam"):
	open("file_list","a").write("%s %s %s" % (root,dirs,files))