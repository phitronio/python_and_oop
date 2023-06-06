import random
from School import School
class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    
    def teach(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name}'
    
    def evaluate_exam(self):
        marks = random.randint(0,100)
        return marks

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
    
    def calculate_final_grade(self):
        for grade in self.subject_grade.values():
            
            point = School.grade_to_value(grade)
            print(self.name, grade, point)



    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id == value