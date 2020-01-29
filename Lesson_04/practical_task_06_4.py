print("This is the solution to task 6 to lesson 4")
print('_' * 150)

from math import isfinite
from sys import argv
from itertools import count, cycle


def my_func(start):
    try:
        isfinite(int(start)) == True
    except ValueError:
        return False
    return True


name, start, finish = argv
print(start, finish)

if my_func(start) == True:
    for el in count(int(start)):
        if el > int(finish):
            break
        else:
            print(el)
else:
    i = 0
    for el in cycle(start):
        if i > int(finish):
            break
        print(el)
        i += 1
