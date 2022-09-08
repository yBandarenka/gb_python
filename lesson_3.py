# задание 1

# вариант 2

def inner_dev(a, b):
    return a / b


var_1 = input("Введите числитель (a): ")
var_2 = input("Введите знаменатель (b): ")

try:
    var_1 = float(var_1)
    var_2 = float(var_2)

    if float(var_2) != 0:
        print("a/b = ", inner_dev(var_1, var_2))
    else:
        print("деление на 0 невозможно")

except ValueError:
    print("некорректный воод числа")
    pass


# вариант 2

def inner_dev2():
    try:
        a = float(input("Введите числитель (a): "))
        b = float(input("Введите знаменатель (b): "))
    except ValueError:
        print("некорректный воод числа")
        return

    if b == 0:
        print("деление на 0 невозможно")
        return

    return a / b


print("a/b = ", inner_dev2())


# задание 2

def user_func(name, sname, date, city, email, phone):
    print(
        f"имя: {name}, фамилия: {sname}, год рождения: {date}, город проживания: {city}, email: {email}, телефон: {phone}")


user_data = input("введите данные пользователя (имя, фамилия, год рождения, город проживания, email, телефон): ").split(
    ", ")

user_func(name=user_data[0], sname=user_data[1], date=user_data[2], city=user_data[3], email=user_data[4],
          phone=user_data[5])


# задание 3

def my_func(a, b, c):
    sort_list = sorted([a, b, c])
    return sort_list[1], sort_list[2]


user_input = input("введите три числа: ").split(" ")

try:
    print("максимальные 2 числа: ", my_func(float(user_input[0]), float(user_input[1]), float(user_input[2])))
except ValueError:
    print("некорректный воод чисел")
    pass


# задание 4

def my_func(x, y):
    if y == 0:
        return 1

    if y < 0:
        if x != 0:
            return x ** y
        else:
            return "ComplexInfinity"
    else:
        return x ** y


def my_func2(x, y):
    if y == 0:
        return 1

    res = 1
    for i in range(abs(y)):
        res *= x

    if y < 0:
        if x != 0:
            return 1 / res
        else:
            return "ComplexInfinity"
    else:
        return res


try:
    a = float(input("введите число: "))
    b = int(input("введите степень: "))

    print("вариант ** : x^y = ", my_func(a, b))

    print("вариант for : x^y = ", my_func2(a, b))
except ValueError:
    print("некорректный воод чисел")

# задание 5

user_symbol = input("введите спецсимвол: ")
user_sum = 0
user_exit = True

while user_exit:
    user_input = input("введите числа: ").strip().split(" ")
    try:
        for el in user_input:
            if el == user_symbol:
                print("ввод чисел закончен")
                print("Итоговая сумма: ", user_sum)
                user_exit = False
                break
            user_sum += float(el)
        if user_exit:
            print("Сумма чисел: ", user_sum)
    except ValueError:
        print("некорректный воод числа")
        break


# задание 6

def int_func(s):
    return s.title()


user_input = input("введите слово: ")

print(int_func(user_input))

# задание 7

user_input = input("введите строку: ").split(" ")

res = ""
for el in user_input:
    res += int_func(el)+" "

print(res.rstrip())
