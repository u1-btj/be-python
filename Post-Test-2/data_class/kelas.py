def input_class():
    name = str(input('Enter class name: '))
    return name

def view_class(list_all):
    print('All Class List')
    print('Class Name || Total Student || Average Score')
    print('='*10)
    for cl, st in list_all.items():
        print(f'Class {cl} || {len(st)} || {get_average_score(st)}')

# decorator for error handling
def error_handling(func):
    def check_empty_val(*items):
        if len(*items) == 0:
            return 0
        return func(*items)
    return check_empty_val

@error_handling
def get_average_score(student_list):
    total_score = 0
    for st, sc in student_list.items():
        total_score += sc
    return total_score / len(student_list)

@error_handling
def get_best_student(student_list):
    max_score = max(student_list.values())
    best_student = ""
    for st, sc in student_list.items():
        if sc == max_score:
            best_student = st
    return f'{best_student} ({max_score})'

@error_handling
def get_worst_student(student_list):
    min_score = min(student_list.values())
    worst_student = ""
    for st, sc in student_list.items():
        if sc == min_score:
            worst_student = st
    return f'{worst_student} ({min_score})'

def view_score_class(list_all):
    view_class(list_all)
    print('='*10)
    name = input_class()
    if name not in list_all.keys():
        print('Class not exists, please input correct name!')
    else:
        print(f'Class {name}')
        print(f'Total Student: {len(list_all[name])}')
        print(f'Average Score: {get_average_score(list_all[name])}')
        print(f'Best Student: {get_best_student(list_all[name])}')
        print(f'Worst Student: {get_best_student(list_all[name])}')

