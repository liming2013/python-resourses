#! /usr/bin/env python 
# coding: utf-8 

import urllib
 
def DownCall(count,size,total_filesize):
    """
    count
    size
    total_filesize
    """
    per=100.0*count*size/total_filesize
    if per>100:
        per=100
    print "Already download %d KB(%.2f"  %(count*size/1024,per)+"%)"
 
url="http://www.nowamagic.net/academy/detail/1302803"
localfilepath=r"C:\Users\Administrator\Desktop\download.html"
urllib.urlretrieve(url,localfilepath,DownCall)

url="http://www.nowamagic.net/academy/category/13/"
localfilepath=r"C:\Users\Administrator\Desktop\download2.html"
urllib.urlretrieve(url,localfilepath,DownCall)
