"""
array = [273, 32, 103, "문자열", True, False, 3.141592]
array2 = [[1,2,3],[4,5,6],[7,8,9]]

print(array[1:2])
print(array[3][2])
# print(array[2][1]) int 형은 불가능
print(array2[2][1])
"""
"""
list_a = [1,2,3]
list_b = [4,5,6]

print("#리스트")
print(list_a)
print(list_b)

print(list_a+list_b)

list_c=list_a+list_b
print(list_c)

print(list_b*4)

print(len(list_c))

print(list_c[len(list_c)-1]) #리스트의 마지막값 출력 , 가장 많이 쓰임
print(list_c[-len(list_c)])  #리스트의 첫번째값 출력
print(list_c[0])             #위의 방법보다 더 편함
"""
"""
list_a = [1,2,3]

list_a.append(77)
list_a.append(99)
print(list_a)

list_a.insert(1,34)
print(list_a)

list_a.extend

del list_a[1]
print(list_a)

list_a.pop(3)
print(list_a)

del list_a[1:3]
print(list_a)
"""
"""
list_a = [1,2,3,1,4,5,6,7,8]

list_a.remove(1)
print(list_a)

list_a.clear()
print(list_a)

print("3" in "13579")

list_a = [273,32,103,57,52]
print(273 in list_a)
print(32 not in list_a)
"""
#반복문
"""
for i in range(5):
    print("출력")
"""
array = [273,32,103,57,52]

for item in array:
    print(item)