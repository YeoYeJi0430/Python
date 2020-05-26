""" a,b=10,20

print("swap 전", end="")
print("a",a,"b",b)

a,b=b,a

print("swap 후", end="")
print("a",a,"b",b) """

""" def call_10_times(func):
    for i  in range(10):
        func()

def print_hello():
    print("Hello World")

call_10_times(print_hello) """

""" # def power(item):
#     return item*item
#power = lambda item : item * item

# def under_3(item):
#     return item<3
under_3 = lambda item : item < 3

lists = [1, 2, 3, 4, 5]

output = map(lambda item: item  * item ,lists)

print(output)
print(list(output))

output_b = filter(lambda item:item<3, lists)
print(list(output_b)) """

#파일열고
f = open("./data/basic.txt","w")
#파일쓰고
f.write("Hello Python Programming...!!")
#파일닫기
f.close()

f1 = open("./data/basic.txt","a")
f1.write("\nAdded documents")
f1.close()

with open("./data/tset.txt","a") as f3: # a 는 계속 추가됨
    f3.write("\nWith sentence document")

content = ""
with open("./data/tset.txt","r") as f4:
    content = f4.read()

print(content)
