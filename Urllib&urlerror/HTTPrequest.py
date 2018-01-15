# coding:utf-8
import urllib.request
import urllib.parse

# key="礼拜"
# keycode = urllib.request.quote(key)
# url='http://www.baidu.com/s?wd=%s' % keycode
# req=urllib.request.Request(url)
# data=urllib.request.urlopen(req).read()

# file.close()
url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name": 'ceo@iqianyue.com',
    "pass": 'aA123456'}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0')
data = urllib.request.urlopen(req).read()
file = open("/media/harold/SpareDisk/pythonProject/DeepinPythonWebCrawler/3.html", 'wb')
file.write(data)
