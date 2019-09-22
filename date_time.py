import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')

#Пример: datetime
from datetime import date, timedelta, datetime
dt_now = datetime.now()
print(dt_now)

#Мы можем "создавать" дату
dt2 = datetime(2015, 5, 16, 8, 3, 44)
print(dt2)

#Разница между датами
delta = dt_now - dt2
print('Дельта: ', delta)

dt3 = dt2 + delta
print(dt3)

#Использование timedelta
dt = date(2000, 1, 1)
print(dt)

delta = timedelta(days=1)
print(delta)

#Использование timedelta
print('День назад:', dt - delta, 'День вперед:', dt + delta)

#Вывод даты на экран
print(dt_now.strftime('%d.%m.%Y %H:%M'))

print(dt_now.strftime('%Y-%m-%d'))

print(dt_now.strftime('%A %d %B %Y'))

#Вывод даты на экран на русском языке
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')
print(dt_now.strftime('%A %d %B %Y'))

#Получение даты из строки
date_string = '12/23/2010'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)

#ЗАДАНИЕ
delta_one = timedelta(days=1)
yesterday = dt_now - delta_one
print('Вчера было:', yesterday.strftime('%d.%m.%Y'))
print('Сегодня:', dt_now.strftime('%d.%m.%Y'))

delta_month = timedelta(days=30)
month_later = dt_now - delta_month
print('Месяц назад:',month_later.strftime('%d.%m.%Y'))

time = '01/01/17 12:10:03.234567'
date_time = datetime.strptime(time, '%m/%d/%y %H:%M:%S.%f')
print(date_time)

dt_time = '2019/10/13 21:07:51'
res_dt = datetime.strptime(dt_time, '%Y/%m/%d %H:%M:%S')
print(res_dt.strftime('%A %d %B %Y'))
print(dt_time)