PI = 3.141592

# print("모듈")
# print(__name__)

def number_input():
    output = input("숫자입력 > ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

if __name__ == "__main__": #추가시 출력에 안나옴
    print("get_circumference(10)",get_circumference(10))
    print("get_circle_area(10)",get_circle_area(10))