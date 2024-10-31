#class...
#class...
class Student:

    def __init__(self, first_name, last_name, passport, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.passport = passport
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Group:
    
    def __init__ (self, name):
        self.__name__ = name
        self.__students__=[]
    
    def __str__(self):
        return f"{self.__name__} has written {" ".join(map(str, self.__students__))}"
    
    def add(self, student:Student):
        self.__students__.append(student)
    
student_1 = Student("John", "Doe", "123456", "01.01.2000")
student_2 = Student("David", "Smith", "654321", "02.02.2000")
st = [student_1]
group = Group("First")
group.add(student_1)
group.add(student_2)
print(group)