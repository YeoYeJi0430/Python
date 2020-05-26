"""
a = 10
b = 20

if(a > b):
    print("a가 더 크다!")
    
    print("진짜루~") #tab 안하면 if문에 묶이지 않음.
    """

"""
#입력
number = input("수 입력")
number = int(number)

#양수조건
if(number>0):
    print("양수")

#음수조건
if(number<0):
    print("음수")

#0조건
if(number == 0):
    print("0이다")
    """

"""
import datetime

cur = datetime.datetime.now()

print(cur.year,cur.month,cur.day)
print(cur.hour,"시")
print(cur.minute,"분")
print(cur.second,"초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(cur.year,cur.month,cur.day,cur.hour,cur.minute,cur.second))

if 3<= cur.month <=5:
    print("봄이 그렇게도 좋냐 멍청이들아~")
    """

number = input("수 입력 : ")

last_ch = number[-1] #오른쪽끝마지막값
last_num = int(last_ch)

if last_num == 1 \
    or last_num == 3 \
    or last_num == 5 \
    or last_num == 7 \
    or last_num == 9 :
    print("홀수")

if last_num == 0 \
    or last_num == 2 \
    or last_num == 4 \
    or last_num == 6 \
    or last_num == 8 :
    print("짝수")

"""
if last_ch in "13579" :
    print("짝수") #in
"""
    