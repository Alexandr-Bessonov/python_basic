print("This is the solution to task 7 to lesson 4")
print('_' * 150)
from math import factorial
from sys import argv


def fibo_gen(my_list):
    for el in my_list:
        yield el


name, num = argv
my_list = []
i = 1
while i <= int(num):
    my_list.append(i)
    i += 1
x = 1

for el in fibo_gen(my_list):
    if x <= 15:
        print(el)
        x += 1

print(f"Факториал {num} равен: {factorial(int(num))}")
print("Возможно не правильно понял задание, решил как понял")