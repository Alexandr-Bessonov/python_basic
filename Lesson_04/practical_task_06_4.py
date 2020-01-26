print("This is the solution to task 6 to lesson 4")
print('_' * 150)

from itertools import count, cycle

for el in count(start):
    if el > finish:
        break
    else:
        print(el)