import urllib
import urllib2
import requests

# Test URL
url = "http://rfunction.com/code/1202/120202.R"

# 1. Using urllib module
print "Begin download with urllib"
urllib.urlretrieve(url, "code1.R")

# 2. Using urllib2 module
print "Begin download with urllib2"
f = urlllib2.urlopen(url)
with open("code2.R", "wb") as code :
    code.write(f.read())

# 3. Using requests
print "Begin download with requests"
r = requests.get(url)
with open("code3.R", "wb") as code :
    code.write(r.content)