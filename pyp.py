""" #2-2
print("3462를 17로 나누었을 때의")
print("-몫:",3462//17)
print("-나머지:",3462%16) """


""" #2-3-1 
str_input = input("숫자 입력> ")
num_input = float(str_input)
print()
print(num_input,"inch")
print((num_input * 2.54), "cm")
#2-3-2
str_input = input("원의 반지름 입력> ")
radius = float(str_input)
print()
print("반지름: ",radius)
print("둘레: ", 2 * 3.14 * radius)
print("넓이: ", 3.14 * radius ** 2) """

""" #2-4-1
a = int(input("> 1번째 숫자: "))
b = int(input("> 2번째 숫자: "))
print()
print("{} + {} = {}".format(a, b, a + b)) """

""" #3-1-1
a = int(input("1번째: "))
b = int(input("2번째: "))
print()

if a > b:
    print("처음 입력했던 {}가 {}보다 더 크다".format(a, b))
if a < b:
    print("두 번째로 입력했던 {}가 {}보다 더 크다".format(b, a)) """

""" #3-2-1
x = int(input("입력 : "))
if 10 < x and x < 20:
    print("조건 o") """

""" #4-1-1
numbers = [1, 2, 3, 4, 100, 101, 102]

for number in numbers:
    if number >= 100:
        print(number)
#4-1-2
list_of_list = [
    [1,2,3],
    [4, 5, 6, 7],
    [8, 9],
]

for a in list_of_list:
    print(a)
    for b in a:
        print(b) """

#4-2-1
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1


print(counter)
print("----")
#4-2-2
character={
    "name":"기사",
    "level":12,
    "items":{
        "sword":"검",
        "armor":"풀"
    },
    "skill":["1","2","3"]
}

for key in character:
    if type(character[key]) is dict:
      for k in character[key]:
          print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        pass
    else:
        pass

