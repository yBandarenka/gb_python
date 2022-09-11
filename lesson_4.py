# задание 1

from sys import argv


def error_hours():
    raise ValueError('невозможно отрицательно времени работать')


def error_hour_rate():
    raise ValueError('любой труд имеет цену')


try:
    script_name, work_hours, work_hour_rate, bonus = argv

    print(" выработка в часах: ", work_hours, "\n", "ставка в час: ", work_hour_rate, "\n", "премия: ", bonus)

    if float(work_hours) < 0:
        error_hours()

    if float(work_hour_rate) <= 0:
        error_hour_rate()

    print("заработная плата работника: ", float(work_hours) * float(work_hour_rate) + float(bonus))
except ValueError as exp:
    print(exp)

# задание 2

from random import randrange

start_list = [randrange(el + 300) for el in range(0, 20)]

print("исходный список: ")
print(start_list)

print("сортированный список: ")
print([start_list[index] for index in range(1, start_list.__len__()) if start_list[index] > start_list[index - 1]])

# задание 3

print("числа, кратные 20 или 21 в диапазоне от 20 до 240: ")

print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# задание 4

from random import randrange

start_list = [randrange(el, 20) for el in range(0, 20)]

print("исходный список: ")
print(start_list)

print("сортированный список: ")
print([start_list[index] for index in range(0, start_list.__len__()) if start_list.count(start_list[index]) == 1])

# задание 5

from functools import reduce

start_list = [el for el in range(100, 1001) if el % 2 == 0]

print("исходный список: ")
print(start_list)


def user_func(el_prev, el):
    return el_prev*el


print("результат умножения елементов: ")
print(reduce(user_func, start_list))

# задание 6

# script 1

from sys import argv
from itertools import count

try:

    script_name, user_number, user_number_end = argv

    user_number = int(user_number)
    user_number_end = int(user_number_end)

    user_number_list = []

    print("введеное начальное число: ", user_number)
    print("введеное конечное число: ", user_number_end)

    for el in count(user_number):
        if el > user_number_end:
            break
        else:
            user_number_list.append(el)

    print("список чисел: ")
    print(user_number_list)

except ValueError:
    print("некорректный ввод")

# script 2

from sys import argv
from itertools import cycle

script_name, user_list = argv

print("входное значение: ")
print(user_list)

res_list = ""
index = 0

for el in cycle(user_list):
    if index > len(user_list)-1:
        break
    else:
        res_list += el
        index += 1

print("копия входного значения: ")
print(res_list)

# # задание 7

n = input("Введите число (n): ")


def fact(a):
    x = 1
    for i in range(1, a + 1):
        x *= i
        yield x


try:
    n = int(n)

    if n == 0:
        print(1)
    elif n < 0:
        raise ValueError
    else:
        for el in fact(n):
            print(el)

except ValueError:
    print("некорректный воод числа")
