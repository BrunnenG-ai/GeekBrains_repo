"""
print("Задание №1")
from time import sleep

class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("It's red!")
            sleep(7)
            print("it's yellow!")
            sleep(2)
            print("It's green!")
            sleep(7)
            print("it's yellow!")
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()

"""
"""
print("Задание №2")

class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def get_full_profit(self):
        return f"{self._lenght}м * {self._width}м * 25кг * 5см = {(self._lenght * self._width * 25 * 5) / 1000}т"

road_check = Road(5000, 20)
print(road_check.get_full_profit())
"""
"""
print("Задания №3")

class Worker():
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return  f"{self.name} {self.surname}"
    def get_full_proffit(self):
        return f"{sum(self._income.values())}"

manager = Position("John", "Smith", "General Manager", 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_proffit())
"""

print("Задание №4")

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print (f"Новая машина : {self.name} (цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала.")

    def stop(self):
        print(f"{self.name}: Машина остановилась. ")

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"направо" if direction == 0 else "налево"} ')

    def show_speed(self):
        return  f'{self.name}: Скорость автомобиля: {self.speed}.'

class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"

class WorkerCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"

class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar("Полицеская", "белый", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkerCar("Грузовичок", "Хаки", 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

sport_car = SportCar("Порше", "синий", 120)
sport_car.go()
sport_car.turn(1)
print(sport_car.show_speed())
sport_car.turn(0)
sport_car.stop()

town_car = TownCar("Лада", "баклажан", 150)
town_car.go()
town_car.turn(1)
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()

print(f'\n Машина {town_car.name} (цвет {town_car.color})')
print(f' Машина {police_car.name} (цвет {police_car.color}')


print("Задание №5")

class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(f"Рисую! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Рисую! {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисую! {self.title} карандашом")

class Handle(Stationery):
    def draw(self):
        print(f"Рисую! {self.title} маркером")

start = Stationery()
start.draw()
pen = Pen("Паркер")
pen.draw()
pencil = Pencil("Большевичка")
pencil.draw()
handle = Handle("ФастЛайн")
handle.draw()