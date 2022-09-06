# задание 1

inner_list = [1, 2, 3, 4, 5]
print("список целых чисел")
for el in inner_list:
    print("элемент %i" % el, "тип ", type(el))

inner_list = ["asf", 's', "b", 'dewdqwd', " "]
print("список строк")
for el in inner_list:
    print("элемент %s" % el, "тип ", type(el))

inner_list = ["asf", 2, 1.1, [1, 'sad']]
print("венигрет")
for el in inner_list:
    print("элемент %s" % el, "тип ", type(el))

# задание 2

print("Введите данные для списка: \n")
inner_list = input().split(' ')

# 1 вариант решения
for i in range(inner_list.__len__()//2):
    inner_list[2*i], inner_list[2*i+1] = inner_list[2*i+1], inner_list[2*i]

print(inner_list)

# 2 вариант решения

print("Введите данные для списка: \n")
inner_list = input().split(' ')

var = 0
i = 0
while i < inner_list.__len__()//2:
    var = inner_list[2 * i]
    inner_list[2 * i] = inner_list[2 * i + 1]
    inner_list[2 * i + 1] = var
    i += 2

print(inner_list)

# задание 3

# вариант list

inner_list = ["зима", "весна", "лето", "осень"]

user_month = input("введите номер месяца: ")

if user_month.isdecimal():
    user_month = int(user_month)
    if 11 >= user_month >= 1:
        position = user_month//3
        print(inner_list[position])
    elif user_month == 12:
        print(inner_list[0])
    else:
        print("Номер месяца должен быть в диапазоне 1-12")
else:
    print("Введенные данные некорректны!")

# вариант dict

inner_list = {1: "зима", 2: "зима", 12: "зима", 3: "весна", 4: "весна",
              5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень"}
user_month = input("введите номер месяца: ")

if user_month.isdecimal():
    user_month = int(user_month)
    if 12 >= user_month >= 1:
        print(inner_list[user_month])
    else:
        print("Номер месяца должен быть в диапазоне 1-12")
else:
    print("Введенные данные некорректны!")

# задание 4

# вариант 1
inner_list = input("введите данные: ").split(' ')
index = 0
for el in inner_list:
    if el.__len__() > 10:
        el = el[0:10]
    el = el.title()
    index += 1
    print(index, ": ", el)

# вариант 2

inner_list = input("введите данные: ").split(' ')
for index, el in enumerate(inner_list,1):
    print(index, ": ", el.title() if el.__len__() < 10 else el.title()[0:10])

# задание 5

my_list = [7, 5, 3, 3, 2]
user_rate = input("введите рейтинг: ")

my_list_reverse = my_list.copy()
my_list_reverse.reverse()

if user_rate.isdecimal():
    user_rate = int(user_rate)
    if my_list_reverse.count(user_rate) > 0:
        position = my_list.__len__() - my_list_reverse.index(user_rate)
        my_list.insert(position, user_rate)
    else:

        if user_rate <= my_list[my_list.__len__()-1]:
            my_list.append(user_rate)
        else:
            for index, el in enumerate(my_list):
                if user_rate > el:
                    my_list.insert(index, user_rate)
                    break
    print(my_list)
else:
    print("Введенные данные некорректны!")

# задание 6

product_list = []
product_property_key_string = ["название", "ед"]
product_property_key_int = ["цена", "количество"]
index = 0

while True:
    add_new_product = input("ввести данные о товаре? (Да - 1, Нет - 0): ")
    if add_new_product.isdecimal():
        if int(add_new_product) == 0:
            break

        product_property = dict()
        print("введите характеристики товара")
        for key in product_property_key_string:
            product_property_value = input(key + ": ")
            product_property.update({key: product_property_value})
        for key in product_property_key_int:
            product_property_value = int(input(key + ": "))
            product_property.update({key: product_property_value})
        index += 1
        product_list.append((index, product_property))
    else:
        print("Введенные данные некорректны!")
        break

print("ввод данных завершен")
print("список товаров:")
print(product_list)

print("Аналитика по товарам: ")

analytics_list = dict()

for key in product_property_key_string:
    analytics_list.update({key: []})

for key in product_property_key_int:
    analytics_list.update({key: []})

for el in product_list:
    items = el[1]
    for key in items.keys():
        analytics_list.get(key).append(items.get(key))

print(analytics_list)

