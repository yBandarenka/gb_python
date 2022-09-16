# задание 1

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"

    f = open(f_name, 'w')

    print("Введите строки ")
    while True:
        str_input = input()
        if str_input == '':
            break
        f.write(str_input + '\n')

    f.close()

    print("содержимое файла: ")
    f = open(f_name, 'r')

    content = f.read()
    print(content)
    f.close()

except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()

# задание 2

# вариант 1

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"


    print("содержимое файла: ")
    with open(f_name) as f:
        content = f.readlines()

    len_word = [el.split(" ").__len__() for el in content]

    print(content)

    print("всего строк: ", content.__len__())
    print("всего слов: ", sum(len_word))

    f.close()

except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()

# вариант 2

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"

    print("содержимое файла: ")
    f = open(f_name, 'r')

    lines = 0
    word = 0
    for line in f:
        lines += 1
        word += line.split(" ").__len__()
        print(line)

    print("всего строк: ", lines)
    print("всего слов: ", word)
    f.close()

except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()

# задание 3

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"

    f = open(f_name, 'r')

    names = []
    names_min_20 = []
    values = []
    sum = 0
    maxS = 20000

    for line in f:
        s = line.split(" ")
        # names.append(s[0])

        try:
            s_user = float(s[1])
            values.append(s[1])
            sum += s_user

            if s_user < maxS:
                names_min_20.append(s[0])

        except ValueError:
            print("некорректные данные о зп: ", s[0])
        except IndexError:
            print("отсутсвуют данные о зп: ", s[0])

    print("имена сотрудников с зп < 20000 : ", names_min_20)
    print("средняя зп: ", sum/values.__len__())

    f.close()

except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()

# задание 4

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"

    f = open(f_name, 'r')

    name_ru = ["Один","Два","Три","Четыре"]
    list_ru = []
    index = 0
    for line in f:
        list_ru.append(" —".join([name_ru[index], line.split("—")[1]]))
        index += 1

    f.close()

    f_name = input('Введите имя файла для записи (по умолчанию out_file.txt): ')

    if f_name == '':
        f_name = "out_file.txt"

    out_f = open(f_name, "w")
    out_f.writelines(list_ru)
    out_f.close()

except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()
    out_f.close()

# задание 5

import random

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"

    f = open(f_name, 'w')

    print("сгенерированная строка чисел: ")
    str_input = [str(random.randint(0, 20)) for el in range(0, 20)]
    print(' '.join(str_input))

    f.write(' '.join(str_input))
    f.close()

    print("содержимое файла: ")
    f = open(f_name, 'r')
    content = f.read()
    print(content)
    s = content.split(" ")

    try:
        sum = 0
        for num in s:
            sum += float(num)

        print("сумма чисел: ", sum)
    except ValueError:
        print("некорректные данные")

except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()

# задание 6

import re

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"
    f = open(f_name, 'r')

    dict_less = {line.split(":")[0]: sum([int(el) for el in re.findall(r'-?\d+\.?\d*', line.split(":")[1])]) for line in f}

    print(dict_less)
except IOError:
    print("файл не найден или не может быть обработан")
finally:
    f.close()

# задание 7

import json

try:

    f_name = input('Введите имя файла (по умолчанию my_file.txt): ')

    if f_name == '':
        f_name = "my_file.txt"

    company_dict = {}
    sum_value = 0
    num = 0

    with open(f_name) as f_list:
        for line in f_list:
            line_list = line.split(" ")
            value = float(line_list[2])-float(line_list[3])
            company_dict.update({line_list[0]: value})
            if value > 0:
                sum_value += value
                num += 1
        print("Словарь фирм: ")
        print(company_dict)

        if num > 0:
            print("средняя прибыль: ", sum_value/num)
        else:
            print("доходов нет! менеджеров в магадан")

        with open("my_file.json", "w") as write_f:
            json.dump([company_dict, {"average_profit": sum_value/num if num > 0 else 0}], write_f)

except IOError:
    print("файл не найден или не может быть обработан")
