#!/usr/bin/python
#-*- coding: utf-8 -*-
import xlrd #必须事先引入读excel的包xlrd
import urllib
import urllib2
import re
filePath=u"E:/工作/公司公告-2014.xls"#excel所在路径
baseUrl='http://snap.windin.com/ns/'#网页网址首部
tarPath="f:/pdf/2014/"#保存路径
try:
    workbook = xlrd.open_workbook(filePath)#打开Excel
    sheet = workbook.sheet_by_index(0)#第一张sheet表
    nrows = sheet.nrows #总行数
    print nrows
    #遍历对应列的每一行数据
    for rownum in range(1,2):#第一行是列名，所以从1开始即第二行读起
        #print rownum#显示当前是第几行
        code=sheet.cell(rownum,1).value#第二列的数据
        codeName=code.split(".")[0]#得到证券代码
        #print codeName
        title=sheet.cell(rownum,2).value#第三列的数据
        title=title.replace(":","_")
        title=title.replace("*","")#替换不符合文件命名的字符
        link=sheet.cell(rownum,3).value#网址链接
        #print link
        fileName=tarPath+codeName+'_'+title+'_'+str(rownum)+'.pdf'#保存的文件名
        #print fileName
        #爬虫：1、获取网页源代码，2、匹配正则表达式，找到pdf的下载链接，3、下载pdf到保存路径
        request = urllib2.Request(link)
        response = urllib2.urlopen(request)
        html=response.read()#读取网页源代码
        findLink=re.compile(r'getatt\.php\?id=\d*&att_id=\d*')#链接的正则匹配
        links=re.findall(findLink,html)
        if(len(links)==0):
			print "Failed:"+str(rownum)
        else:
            for l in links:
                #print l
                url=baseUrl+l#构造pdf的链接
                urllib.urlretrieve(url,fileName)
                #print "Succeed:"+str(rownum)
                print fileName
except Exception,e:
    print str(e)