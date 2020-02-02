import random
from time import sleep
sequence = ["left", "right", "back"]


class Car:

    def __init__(self, name, speed=40, color="white", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police
        print("Машина завелась")

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self):
        print(f"Машина повернула {random.choice(sequence)}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")
        if self.speed > 60:
            pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость автомобиля превышена")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость автомобиля превышена")


class PoliceCar(Car):
    pass


lada = TownCar("Lada", 60, "red", "False")
print(lada.show_speed())
lada.go()
sleep(2)
lada.turn()
sleep(2)
lada.turn()
sleep(2)
lada.turn()
sleep(2)
lada.stop()
# police = PoliceCar()
