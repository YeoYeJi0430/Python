def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    retrun

students = [
    { "이름":"홍길동","korean":87},
    { "이름":"홍길순","korean":90},
    { "이름":"홍길자","korean":100},
    { "이름":"홍길국","korean":60},
    { "이름":"홍길숙","korean":0},
]

for item in students:
    print("이름{},한국어{}".format(item.get("이름"),item.get("korean")))

