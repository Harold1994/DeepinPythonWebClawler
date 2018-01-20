import re
import threading
import queue
import urllib.request
import time
import urllib.error
urlqueue = queue.Queue()
headers = ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
listurl = []

def use_proxy(proxy_addr, url):
    try:
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

class geturl(threading.Thread):
    def __init__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.key = key
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue = urlqueue
        self.key = key
    def run(self):
        page = self.pagestart
        keycode = urllib.request.quote(self.key)
        pagecode = urllib.request.quote("&")
        for page in range(self.pagestart, self.pageend + 1):
            url = 'http://weixin.sogou.com/weixin?type=2&query=' + keycode + "&page=" + str(page)
            data1 = use_proxy(self.proxy, url)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("totally get " + str(len(listurl)) + "pages")
        for i in range(len(listurl)):
            time.sleep(7)
            for j in range(len(listurl[i])):
                try:
                    url=listurl[i][j]
                    url = url.replace("amp;", '')
                    print("第"+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except urllib.error.URLError as e:
                    if hasattr(e, 'code'):
                        print(e.code)
                    if hasattr(e, 'reason'):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception: " + str(e))
                    time.sleep(1)

class getcontent(threading.Thread):
    def __init__(self,urlqueue,proxy):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy
    def run(self):
        i = 1
        html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://
            www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns ="http://www.w3.org/1999/xhtml">
            <head>
            <meta http-quiiv="Content-Type>" content="text/html; charset=utf-8" />
            <title>微信文章页面</title>
            </head>
            <body>'''
        fh = open("/media/harold/SpareDisk/pythonProject/DeepinPythonWebCrawler/2.html", 'wb')
        fh.write(html1.encode("utf-8"))
        fh.close()
        fh = open("/media/harold/SpareDisk/pythonProject/DeepinPythonWebCrawler/2.html", 'ab')
        while(True):
            try:
                url = urlqueue.get()
                data = use_proxy(self.proxy,url)
                title_pat = "<title>(.*?)</title>"
                content_pat = 'id="js_content">(.*?)<div class="rich_media_tool" id="js_sg_bar">'
                title = re.compile(title_pat).findall(data)
                content = re.compile(content_pat, re.S).findall(data)
                thistitle = "None Title"
                thiscontent = "None_Content"
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thiscontent = content[0]
                datall = "<p>标题为: " + thistitle + "</p><p>内容为：" + thiscontent + "</p><br>"
                fh.write(datall.encode('utf-8'))
                print("No." + str(i) + " check")
                i+=1
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
        fh = open("/media/harold/SpareDisk/pythonProject/DeepinPythonWebCrawler/2.html", 'ab')
        fh.write(html2.encode("utf-8"))
        fh.close()

class contrl(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
    def run(self):
        while(True):
            print("-----START----")
            time.sleep(30)
            if(self.urlqueue.empty()):
                print("-----STOP----")
                exit()

key = "AI"
proxy = "140.143.96.141:80"
proxy2 = "61.155.164.110:3128"
pagestart = 1
pagend = 3
t1 = geturl(key,pagestart,pagend,proxy,urlqueue)
t1.start()
t2 = getcontent(urlqueue,proxy)
t2.start()
t3 = contrl(urlqueue)
t3.start()









