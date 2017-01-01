import re
import os.path
import urllib.request
import socket

#Python读写文件
#使用open打开文件后一定要记得调用文件对象的close()方法。比如可以用try/finally语句来确保最后能关闭文件。

n=0
file_object = open('file.txt')  #读文本文件,第二个参数默认为r
#all_the_text = file_object.read( )
for line in file_object: #如果文件是文本文件，还可以直接遍历文件对象获取每行：
    try:
        n = n+1
        #print (line,end="") #python 3.x  print 不换行
        pattern = re.compile(r'(.+?)::.+')
        match = pattern.search(line)
        if match:
            url = match.group(1)
            p,filename = os.path.split(url)
            socket.setdefaulttimeout(10) #设置超时
            data = urllib.request.urlretrieve(url,filename)
            print(url)
    except Exception as e:
        print(e,url)
        n = n-1
print(n)
file_object.close( ) #注：不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法。