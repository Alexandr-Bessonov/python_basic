class Matrix:
    def __init__(self, mx_1, mx_2):
        self.mx_1 = mx_1
        self.mx_2 = mx_2

    def __add__(self, k=0, r=0):
        new_mx = [[0, 0, 0, 0], [0, 0, 0, 0,], [0, 0, 0, 0], [0, 0, 0, 0]]
        # self.k = k
        # self.r = r
        #
        # dic = []
        # while k < len(my_matrix[self.r]):
        #     dic.insert(self.k, 0)
        #     self.k += 1
        # while self.r < len(my_matrix):
        #     new_mx.insert(self.r, dic)
        #     self.r += 1

        for i in range(len(self.mx_1)):
            for j in range(len(self.mx_2[i])): \
            new_mx[i][j] = self.mx_1[i][j] + self.mx_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_mx]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_mx]))


my_matrix = Matrix([[11, 1, 2, 3], [10, 22, 12, 13], [20, 10, 33, 23], [19, 31, 32, 44]],
                   [[44, 43, 42, 30], [34, 33, 21, 31], [24, 23, 22, 21], [14, 13, 12, 11]])

print(my_matrix.__add__())
