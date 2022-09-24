# задание 1

class Matrix:
    __matrix = []

    def get_list_matrix(self):
        return self.__matrix

    def __init__(self, input_matrix):
        self.__matrix = input_matrix

    def __str__(self):
        output = ""
        for str_matrix in self.__matrix:
            for col_matrix in str_matrix:
                output = output + str(col_matrix) + "  "
            output = output + "\n"
        return output

    def __add__(self, other):

        if len(list(self.__matrix)) == len(list(other.__matrix)):
            new_str = []
            j = 0
            for str_matrix in self.__matrix:
                if len(str_matrix) == len(other.get_list_matrix()[j]):
                    new_str.append([str_matrix[i] + other.get_list_matrix()[j][i] for i in range(len(str_matrix))])
                    j += 1
                else:
                    print("Ранг матриц не совпадает!")
                    break
        else:
            print("Ранг матриц не совпадает!")

        return Matrix(new_str)


matr = Matrix([[31, 32, 12, 1], [37, 43, 2, 3]])
matr1 = Matrix([[1, 2, 3, 4], [123, 78, 1, 5]])
m = matr1+matr
print(m)

# задание 2

from abc import ABC, abstractmethod


class Dress(ABC):

    __name_d = "dress"

    def __init__(self, name):
        self.__name_d = name

    def get_name(self):
        return self.__name_d

    @abstractmethod
    def rate(self):
        pass

    @abstractmethod
    def set_size(self):
        pass


class Coat(Dress):

    def __init__(self, name):
        super().__init__(name)
        self.__v = None

    @property
    def rate(self):
        return self.__v/6.5 + 0.5

    def set_size(self, v):
        self.__v = v


class Costume(Dress):

    def __init__(self, name):
        super().__init__(name)
        self.__h = None

    @property
    def rate(self):
        return 2*self.__h + 0.3

    def set_size(self, h):
        self.__h = h


coat = Coat("my coat")
coat.set_size(12.1)

print("Coat: ", coat.get_name())
print("rate: ", coat.rate)

costume = Costume("new costume")
costume.set_size(45)

print("Costume: ", costume.get_name())
print("rate: ", costume.rate)

print("all rate: ", str(coat.rate+costume.rate))

# задание 3

class Cell:

    __partition = 0

    def __init__(self, partition):
        self.__partition = partition

    def __add__(self, other):
        self.__partition += other.partitions

    def __sub__(self, other):
        sub = self.__partition - other.partitions
        if sub > 0:
            self.__partition -= other.partitions
        else:
            print("residual cannot be less than 0!")

    def __mul__(self, other):
        self.__partition *= other.partitions

    def __truediv__(self, other):
        self.__partition //= other.partitions

    def make_order(self, n):

        return ''.join(["*" if el % n != 0 else "*\n" for el in range(1, self.__partition+1)])

    @property
    def partitions(self):
        return self.__partition


cell_1 = Cell(11)
cell_2 = Cell(3)

cell_1.__add__(cell_2)
print("partition(add) " + str(cell_1.partitions))

cell_1.__sub__(cell_2)
print("partition(sub) " + str(cell_1.partitions))

cell_1.__mul__(cell_2)
print("partition(mul) " + str(cell_1.partitions))

cell_1.__truediv__(cell_2)
print("partition(truediv) " + str(cell_1.partitions))

print("partition(make_order) \n" + cell_1.make_order(4))

