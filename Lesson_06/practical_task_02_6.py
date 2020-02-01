class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def mas(self):
        massa = (int(self.length) * int(self.width) * 25 * 5) / 1000
        return massa


road = Road(input('Введите длину (в метрах): '), input('Введите ширину (в метрах0): '))
print(f'Масса требуемого асфальтобетона: {road.mas()} тонн')