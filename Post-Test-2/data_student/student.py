def input_student():
    class_name = str(input('Enter class name: '))
    name = str(input('Enter student name: '))
    return class_name, name

def view_student(list_all):
    print('All Student List')
    print('Student Name || Score || Class')
    print('='*10)
    for cl, student in list_all.items():
        for st, sc in student.items():
            print(f'{st} || {sc} || {cl}')

def get_class_rank(student_list, score):
    return sorted(student_list.values(), reverse=True).index(score) + 1

def view_score_student(list_all):
    view_student(list_all)
    print('='*10)
    class_name, name = input_student()
    if list_all.get(class_name) and name not in list_all[class_name].keys():
        print('Please input correct class name or student name.')
    else:
        print('Student Info')
        print(f'Name: {name}')
        print(f'Class: {class_name}')
        print(f'Score: {list_all[class_name][name]}')
        print(f'Rank: #{get_class_rank(list_all[class_name], list_all[class_name][name])} of {len(list_all[class_name])} student')

