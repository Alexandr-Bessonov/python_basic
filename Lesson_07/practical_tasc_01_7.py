class Matrix:
    def __init__(self, mx):
        self.mx = mx

    def __str__(self):
        for var in range(len(self.mx)):
            print(self.mx[var])
        return


matrix_1 = Matrix([[-1, 0, 1], [0, -1, 1], [1, 1, 1], [0, 1, 0]])
print(matrix_1.mx)

matrix_2 = Matrix([[-2, 0, 2], [0, -2, 2], [2, 2, 2]])
print(matrix_2)
