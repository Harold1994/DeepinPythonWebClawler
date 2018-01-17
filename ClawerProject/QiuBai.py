# coding:utf-8
import re
import urllib.request


def getcontent(url, page):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/63.0.3239.132 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    userpat = '<h2>(.*?)</h2>'
    contentpat = '<div class="content">\n?<span>(.*?)</span>'
    userlist = re.compile(userpat,re.S).findall(data)
    contentlist = re.compile(contentpat,re.S).findall(data)
    x = 1
    for content in contentlist:
        content = content.replace('\n',"")
        content = content.replace('<br/>', "")
        name = "content" + str(x)
        exec(name+'=content')
        x += 1
    y = 1
    for user in userlist:
        name = 'content'+str(y)
        print('用户' + str(page) + str(y) + "是：" + user)
        print("内容是：")
        exec("print("+name+")")
        print("\n")
        y+=1

for i in range(1,3):
    url = 'https://www.qiushibaike.com/8hr/page/'+str(i)
    getcontent(url,i)
