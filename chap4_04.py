""" temp = [1,2,3,4,5,6]

for i in reversed(temp):
    print("첫번째 반복문 {}".format(i))
print()
for i in reversed(temp):
    print("두번째 반복문 {}".format(i)) """

""" example_list = ["A","B","C"]

print(example_list)
print()

print(enumerate(example_list))
print()

print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}".format(i,value))

example_dict = {
    "키:A" : "값A",
    "키:B" : "값B",
    "키:C" : "값C",
}
print()

#딕셔너리 아이템 함수
print(example_dict.items())

for key,element in example_dict.items():
    print("dictionary[{}] = {}".format(key,element))
print() """

array=[]
#빈값 리스트 생성
#for문
for i in range(1,20,2):
    array.append(2 ** i)

#출력
print(list(array))

array2 = [2 ** i for i in range(4,20)] #잘 안쓰임
print(array2)

#조건활용리스트
array3= ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array3 if fruit != "초콜릿"] #초콜릿 x, 잘 안쓰임
print(output)