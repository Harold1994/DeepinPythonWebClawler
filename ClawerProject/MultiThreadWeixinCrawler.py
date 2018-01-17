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
            for j in range(len(listurl[i][j])):
                try:
                    url=listurl[i][j]
                    url = url.replace("amp;", '')
                    print("第"+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.taskdone()
                except urllib.error.URLError as e:
                    if hasattr(e, 'code'):
                        print(e.code)
                    if hasattr(e, 'reason'):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception: " + str(e))
                    time.sleep(1)





