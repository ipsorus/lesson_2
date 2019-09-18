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
    name_list = {}
    for k in students:
        if k['first_name'] in name_list:
            name_list[k['first_name']] += 1
        else:
            name_list[k['first_name']] = 1
    return name_list

    
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.

import collections

students_1 = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
def frequently_name(students_1):
    res = count_names(students_1)
    result = collections.Counter(res)
    result = result.most_common(1)
    return result

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
    class_number = 1
    dict_students = []
    for name in school_students:
        freq_name = frequently_name(name)
        
        dict_students.append({'class': class_number, 'student': freq_name[0][0]})
        class_number += 1
    return dict_students


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
    class_list = []
    for student_in_class in school:
        number_class = student_in_class['class']
        gender_dict = {'class': number_class, 'boys': 0, 'girls': 0}
        for student in student_in_class['students']:
            student_name = student['first_name']
            if is_male[student_name] == False:
                gender_dict['girls'] += 1
            else:
                gender_dict['boys'] += 1
        class_list.append(gender_dict)
    return class_list 

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school_1 = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]}
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
def max_gender_count(school_1, is_male):
    result_list = []
    gender_result = gender_count(school_1, is_male)
    #print(gender_result)
    for g in gender_result:
        d = {'girl':g['girls'], 'boys':g['boys']}
        result = collections.Counter(d)
        result = result.most_common(1)
        result_list.append({'class': g['class'], 'gender': result[0][0]})
    return result_list
    #print(f'Больше всего мальчиков в классе {max_boys[0]}')


    #print(f'Больше всего девочек в классе {max_girls[0]}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a




if __name__ == '__main__':
    print('Задание 1')
    name_list = count_names(students)
    for k in name_list: print(f'{k}: {name_list[k]}')

    print('Задание 2')
    result = frequently_name(students_1)
    print(f'Самое частое имя среди учеников: {result[0][0]}')

    print('Задание 3')
    result = frequently_name_in_class(school_students)
    for name in result: print('Самое частое имя в классе {}: {}'.format(name['class'], name['student']))

    print('Задание 4')
    result = gender_count(school, is_male)
    for gender in result: 
        print('В классе {} {} девочки и {} мальчика.'.format(gender['class'], gender['girls'],gender['boys']))
    
    print('Задание 5')
    result = max_gender_count(school_1, is_male)
    for gender in result:
        if gender['gender'] == 'girl':
            print('Больше всего девочек в классе {}'.format(gender['class']))
        else:
            print('Больше всего мальчиков в классе {}'.format(gender['class']))