from data_student.student import input_student, view_student, view_score_student
from data_class.kelas import input_class, view_class, view_score_class

class Type:
    def __init__(self, number, name):
        self.number = number
        self.name = name

# list of all class with class name as keys and student name as value
# inside class name will be another dictionary with student name as keys and score as value
# data structure will be => {'A': {'John': 80, 'Alex': 90}, 'B: {'Jim': 75}}
list_all = {}

# implement class for constant value
cls_obj = Type(1, 'class')
std_obj = Type(2, 'student')

def select_student_or_class():
    print('Data Type')
    print(f'{cls_obj.number}. {cls_obj.name.capitalize()}')
    print(f'{std_obj.number}. {std_obj.name.capitalize()}')
    choice = int(input("Select data: "))
    if choice not in [cls_obj.number, std_obj.number]:
        print('Please select the correct data type to input!')
        return
    return choice

def menu_add():
    choice = select_student_or_class()
    if choice:
        if choice == 1:
            name = input_class()
            if name in list_all.keys():
                print('Class already exists, please input different class name.')
            else:
                list_all[name] = {}
                print(f'Class {name} added successfully.')
        elif choice == 2:
            class_name, student = input_student()
            if list_all.get(class_name) and student in list_all[class_name].keys():
                print('Student already exists in this class, please input different student.')
            else:
                if class_name in list_all.keys():
                    list_all[class_name][student] = 0
                else:
                    list_all[class_name] = {student: 0}
                print(f'Student {student} added successfully on class {class_name}')

def menu_delete():
    choice = select_student_or_class()
    if choice:
        if choice == 1:
            name = input_class()
            if name in list_all.keys():
                list_all.pop(name)
                print(f'Class {name} and all student inside class are deleted successfully.')
            else:
                print('Class not exists, please input correct name!')
        elif choice == 2:
            class_name, student = input_student()
            if list_all.get(class_name) and student in list_all[class_name].keys():
                list_all[class_name].pop(student)
                print(f'Student {student} on class {class_name} deleted successfully.')
            else:
                print('Please input correct class name or student name.')

def view_all_data():
    choice = select_student_or_class()
    if choice:
        if choice == 1:
            view_class(list_all)
        elif choice == 2:
            view_student(list_all)

def view_score():
    choice = select_student_or_class()
    if choice:
        if choice == 1:
            view_score_class(list_all)
        elif choice == 2:
            view_score_student(list_all)

def assign_score():
    class_name, student = input_student()
    if list_all.get(class_name) and student in list_all[class_name].keys():
        print(f'Assign score to {student} from class {class_name}')
        score = int(input('Enter score: '))
        if score >= 0 and score <= 100:
            old_score = list_all[class_name][student]
            new_score = score
            list_all[class_name][student] = score
            print(f'Score updated from {old_score} to {new_score}')
        else:
            print('Score value must be between 0 and 100')
    else:
        print('Please input correct class name or student name.')

while True:
    print('Menu:')
    print('1. Add (Student/Class)')
    print('2. Delete (Student/Class)')
    print('3. View All Data (Student/Class)')
    print('4. View Score (Average Class/Per Student)')
    print('5. Assign Score (To Student)')
    print('6. Exit')

    menu = int(input("Select menu : "))
    if menu == 1:
        menu_add()
    elif menu == 2:
        menu_delete()
    elif menu == 3:
        view_all_data()
    elif menu == 4:
        view_score()
    elif menu == 5:
        assign_score()
    elif menu == 6:
        print('Exit.')
        break
    else:
        print('Invalid Menu')