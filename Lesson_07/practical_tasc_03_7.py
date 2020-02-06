from time import sleep


class Cells:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return self.quantity * "х"

    # сложение
    def __add__(self, other):
        return (f"Сумма клеток равна: {Cells(self.quantity + other.quantity)}")

    # вычитание
    def __sub__(self, other):
        return (f"Разность клеток равна: {self.quantity - other.quantity}"
                if (self.quantity - other.quantity) > 0 else print('Отрицательно!'))

    # умножение
    def __mul__(self, other):
        return f'Произведение двух клеток равно: {int(self.quantity * other.quantity)}(х)'

    # деление
    def __truediv__(self, other):
        return f'Результат целочисленного деления равен: {Cells(round(self.quantity // other.quantity))}'

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells_1 = Cells(32)
cells_2 = Cells(7)
print(cells_1)
sleep(2)
print(Cells.__add__(cells_1, cells_2))
sleep(2)
print(Cells.__sub__(cells_1, cells_2))
sleep(2)
print(Cells.__mul__(cells_1, cells_2))
sleep(2)
print(Cells.__truediv__(cells_1, cells_2))
sleep(2)
print(cells_1.make_order(5))
sleep(2)
print(cells_2.make_order(5))
