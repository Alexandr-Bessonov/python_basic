import random
from time import sleep
sequence = ["left", "right", "back"]


class Car:

    def __init__(self, name, speed=40, color="white", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police
        print(f"{name} завелась")

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        print(f"{self.name} повернула {random.choice(sequence)}")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed}")
        if self.speed > 60:
            print(f"Скорость {self.name} превышена")


class SportCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed}")
        if self.speed > 60:
            print(f"Скорость {self.name} превышена")
        print(f"{self.name} гоняет по треку")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.name} превышена")


class PoliceCar(Car):
    def go(self):
        print(f"{self.name} выехала в погоню")
    def chase(self):
        if lada.speed > 60:
            self.polise.go()
        print(f"Скорость движения полиции: {police.speed}")
    def stop(self):
        print(f"{self.name} заблокировала нарушителя")


lada = TownCar("Lada", 65, "red", "False")
sleep(2)
lada.go()
sleep(2)
print(lada.show_speed())
sleep(2)
police = PoliceCar("Porshe", 70, "police", True)
sleep(2)
police.go()
sleep(2)
print(police.show_speed())
sleep(2)
lada.turn()
sleep(2)
police.turn()
sleep(2)
lada.turn()
police.turn()
sleep(2)
lada.turn()
sleep(2)
police.turn()
sleep(2)
lada.stop()
sleep(2)
police.stop()

