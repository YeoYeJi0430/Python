""" import sys

print(sys.argv) #실행 후 PS C:\StudyPython> python chap7_1.py TEST Argument 1 입력하면 리스트로 들어감
print("---")
print(sys.getwindowsversion())
print("---")
print(sys.copyright)
print("---")
print(sys.version)
print("") """

import sys
import os
import datetime
from urllib import request

# print("OS : ", os.name)
# print("폴더 : ", os.getcwd())
# print("files : ", os.listdir())

# os.mkdir("Hello")
# os.rmdir("Hello")

# os.system("dir")
# os.system("tree")

current = datetime.datetime.now()
# print(current)
print("{}년 {}월 {}일 {}시 {}분 {}초 {}ms".format(
    current.year,
    current.month,
    current.day,
    current.hour,
    current.minute,
    current.second,
    current.microsecond
))

target = request.urlopen("https://www.google.com")
# output = target.read()

# print(output)

# status = target.getheaders()
# for item in status:
#     print(item)

print(target.status) #200 나오면 정상 그 외 비정