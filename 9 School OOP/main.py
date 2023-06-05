from School import School, ClassRoom
from Persons import Teacher, Student

def main():
    school = School('Adam Jee', 'U TT RA')
    
    # add teachers 
    chemistry_teacher = Teacher('Haradhon Nag', 'chemistry')
    school.add_teacher('chemistry', chemistry_teacher)
    physics_teacher = Teacher('ShahaJan Tapan', 'physics')
    school.add_teacher('physics', physics_teacher)
    biology_teacher = Teacher('Ajmol', 'biology')
    school.add_teacher('biology', biology_teacher)
    math_teacher = Teacher('Yahiya', 'math')
    school.add_teacher('math', math_teacher)

    # show teachers
    # print(school)

    # add classrooms
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)
    
        





if __name__ == '__main__':
    main()