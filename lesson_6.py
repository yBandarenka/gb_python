# задание 1

from time import sleep


class TrafficLight:

    def __init__(self):
        self._colors = {"red": 1, "yellow": 1, "green": 1}
        self.current_color = "red"
        self.__is_running = False

    def running(self):
        self.__is_running = True
        count = 1
        step = 0

        while self.__is_running:

            print(self.current_color)
            sleep(self._colors.get(self.current_color))
            self.current_color = list(self._colors)[count]
            count += 1
            if count == 3:
                count = 0

            step += 1
            if step == 10:
                if input("Stop? (y/n)") == "y":
                    self.stop()
                else:
                    step = 0

    def stop(self):
        self.__is_running = False


print("Start")
traffic_l = TrafficLight()
traffic_l.running()


# задание 2

class Road:

    def __init__(self, id, length, width):
        self.__length = length
        self.__width = width
        self.__id = id

    def mass(self, mass_m2, thickness):
        return self.__length * self.__width * mass_m2 * thickness


print("create road: ")
road69 = Road(69, 10, 20)
print(road69)

print("mass road: ", road69.mass(12, 19))

# задание 3


class Worker:

    __income = dict(wage=0, bonus=0)

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus

    def get_income(self):
        return self.__income


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.get_income().get("wage") + self.get_income().get("bonus")


position = Position("Yury", "Bondarenko", "QA", 10, 14)

print("Full name: ", position.get_full_name())
print("Total income " + str(position.get_total_income()))

print("name " + position.name)
print("surname " + position.surname)
print("position " + position.position)
print("income " + str(position.get_income()))
try:
    print("income " + position.__income)
except AttributeError:
    print('Position object has no attribute __income')

# задание 4


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("car go")

    def stop(self):
        print("car stop")

    def turn(self, direction):
        print("car direction to: " + direction)

    def show_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("max speed : 60!")
        else:
            print("speed : ", self.speed)


class SportCar(Car):

    __engine = "V6"

    def get_engine(self):
        print("engine : " + self.__engine)


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("max speed : 40!")
        else:
            print("speed : ", self.speed)


class PoliceCar(Car):
    is_police = True
    color = "blue"


town_car = TownCar(10, "red", "kik", False)
sport_car = SportCar(120, "green", "sport", False)
work_car = WorkCar(15, "yellow", "woker", False)

print(town_car.name)

town_car.go()
town_car.turn("left")
town_car.turn("right")
town_car.set_speed(100)
town_car.show_speed()
town_car.set_speed(30)
town_car.show_speed()
town_car.stop()

print(sport_car.name)

sport_car.go()
sport_car.turn("left")
sport_car.turn("right")
sport_car.set_speed(100)
sport_car.show_speed()
sport_car.set_speed(30)
sport_car.show_speed()
sport_car.stop()

print(work_car.name)

work_car.go()
work_car.turn("left")
work_car.turn("right")
work_car.set_speed(50)
work_car.show_speed()
work_car.set_speed(40)
work_car.show_speed()
work_car.set_speed(10)
work_car.show_speed()
work_car.stop()

# задание 5


class Stationery:

    title ="stationery"

    def draw(self):
        print("Запуск отрисовки: " + self.title)


class Pen(Stationery):

    title = "Pen"

    def draw(self):
        print("рисуем ручкой: " + self.title)


class Pencil(Stationery):

    title = "Pencil"

    def draw(self):
        print("рисуем карандашом: " + self.title)


class Handle(Stationery):
    title = "Handle"

    def draw(self):
        print("рисуем маркером: " + self.title)


st_ob = Stationery()
pen_ob = Pen()
penc_obj = Pencil()
han_obj = Handle()

st_ob.draw()
pen_ob.draw()
penc_obj.draw()
han_obj.draw()

