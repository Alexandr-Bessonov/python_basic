class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")

new_picture = Stationery('Новый рисунок')
print(new_picture.draw())
pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle('Маркер')
print(handle.draw())