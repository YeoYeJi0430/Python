"""
dict_a = {
    "name" : "어벤져스 앤드게임",
    "type" : "히어로무비",
    "cast" : ["아이언맨","스파이더맨","토르","닥터스트레인지","헐크"],
    "director" : ["안소니 루소","조 루소"],
    "release" : 2018
}

print(dict_a)
print(dict_a["name"])
print(dict_a["release"])
print(dict_a["cast"])

print(dict_a["cast"][1])

# ppt 12p 안좋은방법임.

dict_a["type"] = "로맨스"
dict_a["cameo"] = "스탠 리"

print(dict_a)

del dict_a["release"]
print(dict_a)

print("")
key = "cast"
if key in dict_a:
    print("cast",dict_a[key])
else:
    print("cast 없음")
"""
"""
명령 프롬프트


 print(True)
True
 print(false)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
 print(False)
False
 print(1==3)
False
 print(3==3)
True
 print(3>=4)
False
 print(4>=3)
True
 print("가방"=="가방")
True
 print("World"=="world")
False
 print("World" != "world")
True
 print("World"<"world")
True
 !False
  File "<stdin>", line 1
    !False
    ^
SyntaxError: invalid syntax
 not False
True
 print((1==1) and (2==2))
True
 print((1!=1) and (2==2))
False
 import this
"""

#딕셔너리 선언
dictionary = {
  "name" : "7D 건조 망고",
  "type" : "당",
  "ingredient" : ["망고","설탕","메타","치자"],
  "origin" : "Phil"
}

value = dictionary.get("price")
print("값 :",value)

if value == None:
  print("존재하지 않는 키에 접근했었습니다.")

for key in dictionary:
  #출력
  atom = dictionary.get(key)
  print("값 : ",atom)
  