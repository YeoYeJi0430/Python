class Student:
    count = 0
    __radius = 5

    
    def get_radius(self):
        return self.__radius

    
    def set_radius(self,value):
        self.__radius = value

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format( \
            self.name, \
                self.get_sum(), \
                    self.get_avg())

    def __gt__(self,value):
        return self.get_sum() > value.get_sum()


students = [
    Student("윤인",88,87,95,88),
    Student("안",88,87,95,88),
    Student("구",88,87,95,100),
    Student("나",88,87,90,88),
    Student("윤아",88,99,95,88),
    Student("윤명",88,87,95,88),
    Student("홍길",100,100,100,100),
]


# std_a = Student("윤인",88,87,95,88)
# std_b = Student("윤아",88,99,95,88)
# print(std_a < std_b)

# print("std의 클래스 인스턴스여부 :", isinstance(std, Student))

# print("생성 학생 수 ",Student.count)

std = Student("홍길동",100,100,100,100)
print(std.get_radius())