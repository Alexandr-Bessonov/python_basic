print("This is the solution to task 5 to lesson 4")
print('_' * 150)

from functools import reduce

print(reduce(lambda x, y: x * y, [i for i in range(100, 1000) if i % 2 == 0]))
