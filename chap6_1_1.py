""" # try except 연습

try:
    radius = int(input("정수 입력 > "))
    print("원의 반지름 :", radius)
    print("원의 둘레 :", 2 * 33.14159265 * radius)
    print("원의 넓이 :", 3.14159265 * radius * radius)
    pass
except:
    print("정수!!")
    pass
 """

""" lists = ['11', '22', '33', '44', '안냥', '66']
outputs = []

for item in lists:
    float(item)
    outputs.append(item)

print(outputs)
오류 """

""" lists = ["11", "22", "33", "44", "안냥", "66"]
outputs = []

for item in lists:
    try:
        float(item)
        outputs.append(item)
    except:
        pass

print(outputs) """

""" try:
    radius = int(input("정수 입력 > "))

    print("원의 반지름 :", radius)
    print("원의 둘레 :", 2 * 33.14159265 * radius)
    print("원의 넓이 :", 3.14159265 * radius * radius)
    pass
except:
    print("정수!!")
    pass
else:
    print("에러발생x")
finally:
    print("프로그램종료")
 """

""" 
try:
    f = open("./data/basic.txt","r")
    f.write("TEST!!")
    pass
except Exception as e:
    print(e)
finally:
    f.close()

print("파일 클로즈?", f.closed)
#read로 열었는데 write하면
#not writable 오류. """

""" def test():
    print("test() start")
    try:
        print("test() try")
        return
        print("test() after return")
    except:
        print("test() except")
    else:
        print("test() else")
    finally:
        print("test() finally") #return있어도 finally는 무조건 실행.
    print("test() end")

print("hi")
test()
print("hi") """

lists = [52, 273, 32, 72, 100]

    inputs  = int(input("정수 입력 > "))

    print("{}번째 요소 : 값 {}".format(inputs,lists[inputs]))
    pass
except ValueError as ex:
    print("정수 입력 해라!")
    print(ex)
except IndexError as ex:
    print("인덱스 에러 발생!")
    print(ex)
except Exception as ex: # Exception 에러가 제일 위로 올라가면 다른 에러는 안되기 때문에 에러 제일 밑에 쓰기!
    print(ex)
    
