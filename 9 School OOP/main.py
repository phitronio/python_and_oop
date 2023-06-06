from School import School, ClassRoom, Subject
from Persons import Student, Teacher

def main():
    school = School('Adam Jee', 'U TT RA')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    abul = Student('Abul Khan', eight)
    school.student_admission(abul)
    babul = Student('Babul Khan', eight)
    school.student_admission(babul)
    cabul = Student('Cabul Khan', eight)
    school.student_admission(cabul)

    # subjects
    physics_teacher = Teacher('Shahjahan Tapon Rana')
    physics = Subject('physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Haradon Nag')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher = Teacher('Azmal Sir')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()


    print(school)

if __name__ == '__main__':
    main()