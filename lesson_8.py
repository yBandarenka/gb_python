# задание 1

class Data:

    __date = ""

    def __init__(self, date):
        self.__date = date

    @property
    def data(self):
        return self.__date

    @classmethod
    def convert_date(cls, str):
        lst = str.split("-")
        print("day: ", lst[0])
        print("month: ", lst[1])
        print("year: ", lst[2])
        return [int(el) for el in lst]

    @staticmethod
    def validate_date(day, month, year):

        if (month == 2 & day > 28) or day > 31 or day == 0:
            print("Day not valid")
        elif month > 12 or month == 0:
            print("Month not valid")
        elif year == 0:
            print("Year not valid")
        else:
            print("Data is valid")


date = Data("1-2-1980")
lst = Data.convert_date(date.data)
Data.validate_date(lst[0], lst[1], lst[2])

# задание 2

class DevError(Exception):
    def __init__(self, err_txt):
        self.err_txt = err_txt


def Dev(a, b):
    return a/b


inp_a = input("Введите числитель: ")
inp_b = input("Введите делитель: ")

try:
    inp_a = int(inp_a)
    inp_b = int(inp_b)

    if inp_b == 0:
        raise DevError("Делить на ноль нельзя!")
    else:
        print(f"Результат: {Dev(inp_a, inp_b)}")

except ValueError:
    print("Вы ввели не число")
except DevError as err:
    print(err)

# задание 3

class NumError(Exception):
    def __init__(self, err_txt):
        self.err_txt = err_txt


user_list = []

print("Введите данные для списка: ")

while True:
    input_num = input()
    if input_num == "stop":
        break
    else:
        try:

            if input_num.isdigit():
                user_list.append(int(input_num))
            else:
                raise NumError("введено не число! ")
        except NumError as err:
            print(err)

print("итоговый список: ", user_list)

# задание 4-6

class CountError(Exception):
    def __init__(self, err_txt):
        self.err_txt = err_txt


class Storehouse:

    def __init__(self):
        self.__devices = dict()

    def add_position(self, type_position, count):

        try:
            if isinstance(count, int):
                if count < 0:
                    raise CountError("нельзя отрицательно внести на склад позицию!")
                elif count == 0:
                    raise CountError("и зачем 0 вносить?")

                num = self.__devices.get(type_position)
                if num is None:
                    num = 0
                num += count
            else:
                raise CountError("некорректно задано количество!")

            if isinstance(type_position, str):
                self.__devices.update({type_position: num})

                print(f"на склад прибыло: {type_position} - {count} шт")
            else:
                raise CountError("некорректно имя позиции!")

        except CountError as err:
            print(err)

    def remove_position(self, type_position, count):

        try:
            if isinstance(type_position, str):
                num = self.__devices.get(type_position)

                if num is None:
                    num = 0

            else:
                raise CountError("некорректно имя позиции!")

            if count < 0:
                raise CountError("нельзя отрицательно вынести из склада позицию!")
            elif count == 0:
                raise CountError("и зачем 0 вносить?")

            if num > 0:

                if (num - count) >= 0:
                    num -= count
                    self.__devices.update({type_position: num})
                    print(f"со склада изъяли : {type_position} - {count} шт")
                else:
                    raise CountError(f"на складе нет необходимого количества {type_position}. всего на складе: {num}")

            else:
                print("на складе отсутсвуют ", type_position)

        except CountError as err:
            print(err)

    def move_to_division(self, type_position, division, count):
        self.remove_position(type_position, count)
        print(f"изятая техника перемещена в подразделение {division}")


class OfficeDevice:
    __name = ""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Printer(OfficeDevice):

    def __init__(self, name):
        super().__init__(name)
        self.__h = None
        self.__w = None

    def set_size_paper(self, h, w):
        self.__h = h
        self.__w = w

    def print_doc(self):
        print("Печать документа...")


class Xerox(OfficeDevice):

    def __init__(self, name):
        super().__init__(name)
        self.__max_copy = None

    def set_max_copy(self, max_copy):
        self.__max_copy = max_copy

    def copy_doc(self):
        print(f"Копирование  документа. {self.__max_copy} шт")


class Scaner(OfficeDevice):

    def __init__(self, name):
        super().__init__(name)
        self.__dpi = None

    def set_dpi(self, dpi):
        self.__dpi = dpi

    def scan_doc(self):
        print(f"Сканирование документа с разрешением {self.__dpi} dpi")


printer = Printer("printer")
xerox = Xerox("xerox")
scaner = Scaner("scaner")

storehouse = Storehouse()

storehouse.add_position(printer.name, 2)
storehouse.add_position(printer.name, 0)
storehouse.add_position(printer.name, -1)
storehouse.add_position(printer.name, "test")

storehouse.add_position(xerox.name, 12)
storehouse.remove_position("test", 1)
storehouse.remove_position(xerox.name, 1)
storehouse.move_to_division(xerox.name, "бухгалтерия", 2)


# задание 7

class ComplexNum:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f"{self.a} + {self.b}i"


compl1 = ComplexNum(1, 2)
compl2 = ComplexNum(2, 3)

print("complex num 1: ", compl1)
print("complex num 2: ", compl2)

print("complex num 1 + num 2: ", compl1+compl2)
print("complex num 1 * num 2: ", compl1*compl2)
