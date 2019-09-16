# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

from collections import Counter

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

def count_names(students):
    print('Задание 1')
    print('Вариант с Count()')
    name_list = []
    for name in students:
        name_list.append(name['first_name'])
    res = Counter(name_list)
    for student in res:
        print(f'{student}: {res[student]}')
    

def count_names_1(students):
    print('Вариант на циклах for')
    name_list = []
    for name in students:
        name_list.append(name['first_name'])
    for student in name_list:
        res = 0
        for i in range(0, len(name_list)):
            if student == name_list[i]:
                res += 1
        name_list.remove(student)
        print(f'{student}: {res}')
    

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students_1 = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
def frequently_name(students_1):
    print('Задание 2')
    name_list = []
    names = []
    for name in students_1:
        name_list.append(name['first_name'])
    for student in name_list:
        res = 0
        for i in range(0, len(name_list)):
            if student == name_list[i]:
                res += 1
        name_list.remove(student)
        names.append([student, res])
    temp_name = [0,0]
    for i in names:
        if i[1] > temp_name[1]:
           temp_name = [i[0], i[1]]

    print(f'Самое частое имя среди учеников: {temp_name[0]}')

def frequently_name_count(students_1):
    print('Задание 2 Count')
    name_list = []
    for name in students_1:
        name_list.append(name['first_name'])
    res = Counter(name_list)
    temp_name = [0,0]
    for student in res:
        if res[student] > temp_name[1]:
           temp_name = [student, res[student]]

    print(f'Самое частое имя среди учеников: {temp_name[0]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
def frequently_name_in_class(school_students):
    print('Задание 3')
    name_list = []
    class_number = 0
    for class_students in school_students:
        for name in class_students:
            name_list.append(name['first_name'])
            res = Counter(name_list)
        temp_name = [0,0]
        for student in res:
            if res[student] > temp_name[1]:
                temp_name = [student, res[student]]
        class_number += 1
        name_list.clear()

        print(f'Самое частое имя в классе {class_number}: {temp_name[0]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
def gender_count(school, is_male):
    print('Задание 4')
    for student_in_class in school:
        count_boys = 0
        count_girls = 0
        number_class = student_in_class['class']
        for student in student_in_class['students']:
            student_name = student['first_name']
            if is_male[student_name] == False:
                count_girls += 1
            else:
                count_boys += 1
            
        print(f'В классе {number_class} {count_girls} девочки и {count_boys} мальчика.')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
def max_gender_count(school, is_male):
    print('Задание 5')
    class_gender = []
    for student_in_class in school:
        count_boys = 0
        count_girls = 0
        number_class = student_in_class['class']
        for student in student_in_class['students']:
            student_name = student['first_name']
            if is_male[student_name] == False:
                count_girls += 1
            else:
                count_boys += 1
        class_gender.append({'class': number_class, 'boys':count_boys, 'girls':count_girls})
    max_boys = [0,0]
    max_girls = [0,0]
    for school_class in class_gender:
        if school_class['boys'] > max_boys[1]:
            max_boys = [school_class['class'],school_class['boys']]
            print(f'Больше всего мальчиков в классе {max_boys[0]}')
        elif school_class['girls'] > max_girls[1]:
            max_girls = [school_class['class'],school_class['girls']]
            print(f'Больше всего девочек в классе {max_girls[0]}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


if __name__ == '__main__':
    count_names(students)
    count_names_1(students)
    frequently_name(students_1)
    frequently_name_count(students_1)
    frequently_name_in_class(school_students)
    gender_count(school, is_male)
    max_gender_count(school, is_male)