def print_3_times():
    print("Hello World")
    print("안냥")
    print("예디")

""" #가변매개변수와 충돌로 실행안됨.
def print_n_times(value,n=2): #default값 = 2
    for i in range(n):
        print(value,end="")

def print_n_times(value):
    for i in range(10):
        print(value, end="")
 """
def print_n_times(*values, n=2): #가변매개변수 앞으로 올때는 그 뒤에 값들을 default설정 해야함.
    for i in range(n):           #이것만 작동, 위에 def들은 작동x
        for value in values:
            print(value,end="")
        print()

def func(a,b=10,c=20):
    print(a+b+c)

"""
print_3_times()
print_n_times("Hello",4)
print_n_times(4,"안녕하세요","즐거운","파이썬","프로그래밍")
 """

print_n_times("hello",n=4) #n을 4라고 지정 해줘야 4번반복
print_n_times("안녕하세요","즐거운","파이썬","프로그래밍")
func(c=100,a=51,b=30) #가능하지만 비추