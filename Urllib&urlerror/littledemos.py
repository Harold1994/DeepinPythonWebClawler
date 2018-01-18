import  urllib.request
# url = "http://maps.google.com/maps/api/geocode/json?address=Beijing"
# file = urllib.request.urlopen(url)
# print(file.read())
# headers=("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) \
#                       Gecko/20100101 Firefox/56.0")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data=opener.open(url).read()
# print(data)
# for i in range(1,100):
#     try:
#         file = urllib.request.urlopen("http://yum.iqianyue.com",timeout=1)
#         data=file.read()
#         print(len(data))
#     except:
#         print("---出现一场----")
import re

# pat = '123435//.+?\.jpggg'
# red = re.compile(pat).findall('123435//gg.jpggg')
# print(red)
import http.cookiejar
url = "http://news.163.com/18/0116/21/D8A60K2T000189FH.html"
headers = { 'Connection': 'keep-alive',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
                          "like Gecko)Chrome/63.0.3239.132 Safari/537.36",
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Referer': 'http://tpc.googlesyndication.com/safeframe/1-0-14/html/container.html?n=1',
            'Accept-Language': "zh-CN,zh;q=0.9"}

cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8888'})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open('D:/DeepinPythonWebClawler/2.html','wb')
fhandle.write(data)
fhandle.close()

