# coding : utf-8
import os

export = []
for root, dirs, files in os.walk("D:\Py_exam\lovely_python_ex"):
	export.append("\n %s;%s;%s" % (root,dirs,files))
open('file_list_3', 'w').write(''.join(export))

'''
export是变量名, 初始化为一空字符串
open(路径+文件名, 读写模式)
file.write(str) # 把str写入file文件，该程序的file就是前面用open打开的文件对象
整个程序就是读取/media/cdrom0（这是linux里面光盘的路径名）目录下所有文件文件夹，然后把他们的名称先赋予变量export，然后写入mycd2.cdc文件
你这是《可爱的python》里面的例子吧，上面应该写得很清楚啊
'''