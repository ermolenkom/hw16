# Assignment.1
# Посмотреть видео https://www.youtube.com/watch?v=JRCJ6RtE3xU
# Создать программу, которая будет работать с внешним API для получения курса валют для выбранной динамически валюты
# Результаты отправить на почту преподавателя с помощью средств python
# Assignment.2
# Создать csv файл для списка городов в Канаде(смотри таблицы в https://en.wikipedia.org/wiki/List_of_cities_in_Canada) вида:city,lat,lon (город, широта, долгота)
# https://nominatim.org/release-docs/develop/api/Overview/ - здесь можно получить широту и долготу
# Результаты отправить на почту преподавателя с помощью средств python

# По этим заданиям необходимо сделать документацию небольшую любым удобным способом. 
#from currency import f_currency
from location import f_location
from datetime import datetime

def main():
    """Основная процедура запуска"""
    email = input("EMail to:")
    if not(email):
        email = "schumixer@list.ru"
#    f_currency(email)
    start_time = datetime.now()
    f_location(email)
    print(datetime.now() - start_time)    

if __name__ == "__main__":
    main()