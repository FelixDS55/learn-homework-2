"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as file:
        my_lst = []
        my_file = file.readlines()
        for txt in my_file:
            my_lst.append(txt.strip())
        my_read = ' '.join(my_lst)
        len_str = 0
        for str_ in my_read:
            len_str += len(str_)
        print(len_str)

        print(len(my_read.split()))
        my_read_for_file1 = my_read.replace('.', '!')
        print(my_read_for_file1)

    print(file.closed)

    with open('referat2.txt', 'w', encoding='utf-8') as file1:
        file1.write(my_read_for_file1)

    print(file1.closed)

if __name__ == "__main__":
    main()
