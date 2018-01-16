import urllib.request
import urllib.parse

url = "https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check"
postdata = urllib.parse.urlencode({
    "username": "18911341910",
    "password": "lh1994114"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("D:/DeepinPythonWebClawler/3.html", 'wb')
fhandle.write(data)
fhandle.close()

# url2 = "https://www.csdn.net/"
# req2 = urllib.request.Request(url2,postdata)
# req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
#                 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
# data2 = urllib.request.urlopen(req2).read()
# fhandle = open("D:/DeepinPythonWebClawler/4.html",'wb')
# fhandle.write(data)
# fhandle.close()

