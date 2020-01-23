print("This is the solution to task 4 to lesson 3")
print('_' * 150)
print('Программа принимает действительное положительное число x и целое отрицательное число y.\n'
      'Необходимо выполнить возведение числа х в степень y. Задание необходимо реализовать в виде функции my_func(x,y).\n'
      'При решении задания неоходимо обойтись без встроенной функции возведения числа в степень.')
print('_' * 150)

print('Первый вариант решения')


# Первый вариант решения
def my_fanc(x, y):
    return 1 / (x ** abs(y))


x = int(input('Введите положительное число Х: '))
y = int(input('Введите отрицательное число Y: '))
if y >= 0:
    print('Вы ввели не отрицательное число')
else:
    print(f'Результат возведения X в степень Y: {my_fanc(x, y)}')

print('Второй вариант решения')


# Второй вариант решения
def my_func_2(x, y):
    i = 1
    res = x
    if x == 0:
        return 0
    elif y == 0:
        return 1
    elif y < 0:
        while i < abs(y):
            res *= x
            i += 1
        return (1 / res)


print(my_func_2(x, y))
