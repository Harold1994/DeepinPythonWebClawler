import urllib.request
import urllib.error
try:
    urllib.request.urlopen('http://blog.baidusss.net')
except urllib.error.HTTPError as e:
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)

