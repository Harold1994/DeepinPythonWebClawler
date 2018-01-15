import re

# pattern1 = "python"
# pattern2 = "python"
# string = "dhnjkeshfbPythonsdhjjkd5"
# result1 = re.search(pattern1,string,re.I)
# print(result1)

pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = '021-1234567891563'
result = re.compile(pattern).findall(string)
print(result)
