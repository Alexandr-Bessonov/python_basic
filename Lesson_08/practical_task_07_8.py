# practical task #7
class ComplexNumber:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b, self.c + other.c)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b, self.c * other.c)

    def __str__(self):
        return f'({self.a}, {self.b} ,{self.c})'


var_1 = ComplexNumber(10, 2, 30)
var_2 = ComplexNumber(4, 50, 6)
print(f'Первое комплексное число: {var_1}')
print(f'Второе комплексное число: {var_2}')
print(f'При сложении получается: {var_1 + var_2}')
print(f'При умножении получается: {var_1 * var_2}')
