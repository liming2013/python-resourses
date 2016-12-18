# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：百度贴吧爬虫  
#   版本：0.1  
#   作者：why  
#   日期：2013-05-14  
#   语言：Python 2.7  
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。  
#   功能：下载对应页码内的所有页面并存储为html文件。  
#---------------------------------------  
   
import string, urllib2  
   
#定义百度函数  
def baidu_tieba(url,begin_page,end_page):     
    for i in range(begin_page, end_page+1):  
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名  
        print 'downloading ' + str(i) + ' page, and store as ' + sName + '......'  
        f = open(sName,'w+')  
        m = urllib2.urlopen(url + str(i)).read()  
        f.write(m)  
        f.close()  
   
   
#-------- 在这里输入参数 ------------------  
  
# 这个是酷派在百度贴吧中某一个帖子的地址 
#bdurl = 'http://tieba.baidu.com/p/4900778551?pn='  
#iPostBegin = 1  
#iPostEnd = 10  
s=u'黎明'
print s

  
bdurl=str(raw_input('intput the address\n'))
begin_page_t=int(raw_input('start page\n'))
end_page_t=int(raw_input('end page\n'))
#-------- 在这里输入参数 ------------------  
   
  
#调用  
baidu_tieba(bdurl,begin_page_t,end_page_t)

