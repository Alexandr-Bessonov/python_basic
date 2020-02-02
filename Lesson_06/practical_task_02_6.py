class Road:

    def __init__(self, __length, __width):
        self.length = __length
        self.width = __width

    def mas(self):
        massa = (int(self.length) * int(self.width) * 25 * 5) / 1000
        return massa


road = Road(input('Введите длину (в метрах): '), input('Введите ширину (в метрах0): '))
print(f'Масса требуемого асфальтобетона: {road.mas()} тонн')
