list_student = [] # list all student

class Student:
    def __init__(self, name, grade, absent):
        self.name = name
        self.grade = grade
        self.absent = absent
        self.status, self.desc = self.check_grade()

    def check_grade(self): # assign status and description value
        con1 = self.grade >= 75
        con2 = self.absent < 4
        status = ""
        note = ""
        if con1 and con2:
            status = "Passed"
            note = "Congrats! Grade >= 75 and Absent < 4."
        else:
            status = "Failed"
            if not con1 and not con2:
                note = "Grade must be above 75 and Absent must not more than 4 times"
            elif not con1:
                note = "Grade must be above 75!"
            elif not con2:
                note = "Absent must not more than 4 times!"
        return status, note

def add_student():
    n_student = int(input('Enter total student to input: '))
    while n_student > 0:
        name = str(input('Enter student name: '))
        grade = int(input('Enter student grade: '))
        absent = int(input('Enter student absent count: '))
        list_student.append(Student(name, grade, absent))
        print('='*10) # border per student input
        n_student -= 1
    print('Input student success.')

def view_all():
    print('All Student Status')
    print('Name || Grade || Absent || Status || Description')
    print('='*10)
    for std in list_student:
        print(f'{std.name} || {std.grade} || {std.absent} || {std.status} || {std.desc}')

def view_percentage():
    print('All Student Percentage')
    print('='*10)
    passed = 0
    failed = 0
    total = 0
    for std in list_student:
        if std.status == "Passed":
            passed += 1
        else:
            failed += 1
        total += 1

    print(f'Total Student: {total}')
    print(f'Student Passed: {passed}')
    print(f'Student Failed: {failed}')
    print(f'Passed Percentage: {(passed/total)*100}%')
  
while True:
    print('Menu:')
    print('1. Add Student')
    print('2. View All Student Status')
    print('3. View Percentage Student (Passed/Failed)')
    print('4. Exit')

    menu = int(input("Select menu : "))
    if menu == 1:
        add_student()
    elif menu == 2:
        view_all()
    elif menu == 3:
        view_percentage()
    elif menu == 4:
        print('Exit.')
        break
    else:
        print('Invalid Menu')