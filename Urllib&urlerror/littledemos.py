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

pat = '123435//.+?\.jpggg'
red = re.compile(pat).findall('123435//gg.jpggg')
print(red)

