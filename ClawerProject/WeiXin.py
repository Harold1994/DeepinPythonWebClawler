import re
import urllib.request
import urllib.error
import time

headers = ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
listurl = []


def use_proxy(proxy_addr, url):
    try:
        import urllib.request
        proxy = urllib.request.ProxyHandler({'https': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception: " + str(e))
        time.sleep(1)


def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote("&")
        for page in range(pagestart, pageend + 1):
            url = 'http://weixin.sogou.com/weixin?type=2&query=' + keycode+"&page="+str(page)
            data1 = use_proxy(proxy, url)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("totally get " + str(len(listurl)) + "pages")
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception: " + str(e))
        time.sleep(1)


def getcontent(listurl, proxy):
    i = 0
    html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://
    www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns ="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-quiiv="Content-Type>" content="text/html; charset=utf-8" />
    <title>微信文章页面</title>
    </head>
    <body>'''
    fh = open("D:/DeepinPythonWebClawler/1.html", 'wb')
    fh.write(html1.encode("utf-8"))
    fh.close()
    fh = open("D:/DeepinPythonWebClawler/1.html", 'ab')
    for i in range(0, len(listurl)):
        for j in range(0, len(listurl[i])):
            try:
                url = listurl[i][j]
                url = url.replace("amp;", '')
                data = use_proxy(proxy, url)
                title_pat = "<title>(.*?)</title>"
                content_pat = 'id="js_content">(.*?)<div class="rich_media_tool" id="js_sg_bar">'
                title = re.compile(title_pat).findall(data)
                content = re.compile(content_pat,re.S).findall(data)
                thistitle = "None Title"
                thiscontent = "None_Content"
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thiscontent = content[0]
                datall = "<p>标题为: " + thistitle + "</p><p>内容为：" + thiscontent + "</p><br>"
                fh.write(datall.encode('utf-8'))
                print("No." + str(j) + " check" + " in page " + str(i))
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("exception: " + str(e))
                time.sleep(1)
    fh.close()
    html2 = '''</body>
    </html>'''
    fh = open("D:/DeepinPythonWebClawler/1.html", 'ab')
    fh.write(html2.encode("utf-8"))
    fh.close()


key = "spark"
proxy = "140.143.96.141:80"
proxy2 = "61.155.164.110:3128"
pagestart = 1
pagend = 10
listurl = getlisturl(key, pagestart, pagend, proxy)
print(listurl)
getcontent(listurl, proxy)

