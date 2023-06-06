from School import School, ClassRoom
from Persons import Student

def main():
    school = School('Adam Jee', 'U TT RA')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('Abir Khan', eight)
    school.student_admission(abul)


    print(school)

if __name__ == '__main__':
    main()