from datetime import date, datetime, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    my_date_today = date.today()
    my_date_yest = date.today() - timedelta(days=1)
    my_date_30_ago = date.today() - timedelta(days=30)
    print(my_date_30_ago)
    print(my_date_today)
    print(my_date_yest)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    my_date = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return my_date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
