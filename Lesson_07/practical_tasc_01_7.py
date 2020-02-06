class Matrix:
    def __init__(self, mx_1, mx_2):
        self.mx_1 = mx_1
        self.mx_2 = mx_2

    def __add__(self):
        new_mx = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        for i in range(len(self.mx_1)):
            for j in range(len(self.mx_2[i])):
                new_mx[i][j] = self.mx_1[i][j] + self.mx_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_mx]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_mx]))


my_matrix = Matrix([[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]],
                   [[44, 43, 42, 41], [34, 33, 32, 31], [24, 23, 22, 21], [14, 13, 12, 11]])

print(my_matrix.__add__())
