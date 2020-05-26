class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def toString(self):
        return "{}\t{}\t{}".format( \
            self.name, \
                self.get_sum(), \
                    self.get_avg())

#student = Student()

students = [
    Student("윤인",88,87,95,88),
    Student("안",88,87,95,88),
    Student("구",88,87,95,100),
    Student("나",88,87,90,88),
    Student("윤아",88,99,95,88),
    Student("윤명",88,87,95,88),
]

print("이름","총점","평균",sep='\t')
for Student in students:
    print(Student.toString())
    
# print(students[1].name)
# print("실행완료")