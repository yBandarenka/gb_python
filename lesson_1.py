# задание 1

internal_var = 12
internal_var_1 = "var"

print("внутренняя переменная internal_var = ", internal_var)
print("внутернняя переменная internal_var_1 = ", internal_var_1, " типа ", type(internal_var_1))

user_var = input("введите значение переменной \nuser_var = ")

print("вы ввели значение: ", user_var)

user_var = input("введите целое положительное число: ")

if user_var.isnumeric():
    print("вы ввели значение: ", user_var)
else:
    print("вы ввели не целое/положительное число")

# задание 2

time_in_sec = input("введите время в секундах: \ntime = ")

if time_in_sec.isnumeric():
    time = int(time_in_sec)

    hours = time // (60 ** 2)
    print("hours ", hours)

    minutes = (time - hours*(60**2)) // 60
    print("minutes ", minutes)

    seconds = (time - hours*(60**2) - minutes*60)
    print("second ", seconds)

else:
    print("некорректный ввод значения для времени")

# задание 3

user_number = input("введите число: ")

if user_number.isnumeric():
    res = int(user_number) + int(user_number*2) + int(user_number*3)
    print("итоговый результат(n+nn+nnn): ", res)
else:
    print("некорректный ввод значения числа")

# задание 4

user_num = int(input("Введите число : "))
user_num_0 = user_num
num_max = 0

while user_num > 0:
    d = user_num % 10
    if num_max < d:
        num_max = d
    user_num = user_num // 10

print("итоговый результат(максимальная цифра в числе % s): " % user_num_0, num_max)

# задание 5

print("расчет рентабельности выручки")

proceeds = float(input("введите выручку фирмы: "))
costs = float(input("введите издержки фирмы: "))

if proceeds > costs:
    print("фирма работает с прибылью")
elif costs > proceeds:
    print("фирма работает с убытками")
else:
    print("фирма не имеет ни убытков ни прибыли")

# задание 6

if proceeds > costs:
    print("рентабельность  = %s" % ((proceeds - costs) / proceeds * 100), "%")
    people = int(input("введите числленность сотрудников: "))
    if people > 0:
        print("прибыль фирмы в расчёте на одного сотрудника: %s" % ((proceeds - costs) / people))
    else:
        print("ну не может на фирме работать ноль и меньше нуля сотрудников!")

# задание 7

a = float(input("введите результат первого дня (a): "))
b = float(input("введите требуемый результат (b): "))

current_distance = a
num_day = 1

while current_distance < b:
    current_distance = current_distance * 1.1
    num_day = num_day + 1
    print("%s -й день: %.2f" % (num_day, current_distance))

print("Ответ: на %s-й день спортсмен достиг результата — не менее %s км." % (num_day, b))

