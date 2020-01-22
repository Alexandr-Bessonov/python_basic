print("This is the solution to task 3 to lesson 3")
print('_' * 150)
print('Реализовать функцию my_func(), которая принимает три позиционных аргумента, '
      'и возвращает сумму наибольших двух аргументов.')
print('_' * 150)


def func(var_1, var_2, var_3):
    i = [var_1, var_2, var_3]
    el_min = min(i)
    i.remove(el_min)
    return sum(i)


num = []
num.append(int(input("Введите первое число: ")))
num.append(int(input("Введите второе число: ")))
num.append(int(input("Введите третье число: ")))
summa = func(num[0], num[1], num[2])
print(f'Сумма двух наибольших числа равна: {summa}')