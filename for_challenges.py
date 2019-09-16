# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
def new_string_names(names):
    for name in names:
        print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
def names_lengh(names):
    for name in names:
        print(name, len(name))



# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
def names_gender(names):
    for name in names:
        if is_male[name] == False:
            print(f'{name}, \'Пол женский\'')
        else:
            print(f'{name}, \'Пол мужской\'')
        


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
def count_group_students(groups):
    groups_count = len(groups)
    print(f'Количество групп: {groups_count}')
    for group in groups:
        students = len(group)
        print(f'Число студентов в группе: {students}')



# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

def students_in_group(groups):
    group_number = 1
    for group in groups:
        #for name in group:
            #name_student = name
        students_names = (', '.join(group))

        print(f'Группа {group_number}: {students_names}')
        group_number += 1

if __name__ == '__main__':
    new_string_names(names)
    names_lengh(names)
    names_gender(names)
    count_group_students(groups)
    students_in_group(groups)