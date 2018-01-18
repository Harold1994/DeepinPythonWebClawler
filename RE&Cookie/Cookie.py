import urllib.request
import urllib.parse

url = "http://update.googleapis.com/service/update2?cup2key=7:1439191684&cup2hreq=503cf164d5bdbfa1cbedf171078b2690d941befc84cb30c9fc5e0df541111c67"
postdata = urllib.parse.urlencode({
    "loginname": "18911341910",
    "nloginpwd": "lh1994114"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("D:/DeepinPythonWebClawler/3.html", 'wb')
fhandle.write(data)
fhandle.close()

url2 = "https://www.jd.com/"
req2 = urllib.request.Request(url2,postdata)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
data2 = urllib.request.urlopen(req2).read()
fhandle = open("D:/DeepinPythonWebClawler/4.html",'wb')
fhandle.write(data)
fhandle.close()

