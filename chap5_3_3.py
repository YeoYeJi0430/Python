""" def test():
    print("함수가 호출 되었습니다.")
    yield "test"

#함수 호출
print("A 지점 통과")
test()

print("B 지점 통과")
test()

print(test()) """

#yield
#https://dojang.io/mod/page/view.php?id=2412 참고
#return 과 다름
def test():
    print("A 지점 통과")
    yield 1                 #yield1 수행후 쉬었다가 불리면 다음꺼(yield2) 실행
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test()

print("D 지점 통과")
a = next(output)
print(a)

print("E 지점 통과")
b = next(output)
print(b)

# print("F 지점 통과")
# c = next(output)
# print(c)