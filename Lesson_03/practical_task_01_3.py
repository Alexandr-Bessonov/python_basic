print("This is the solution to task 1 to lesson 3")
print('_' * 150)
print('Реализовать функцию, принимающую два числа (позиционные переменные и выполняющую их деление.\n'
      'Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.')
print('_' * 150)


def func():
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите первое число: '))
        c = round((a / b), 2)
    except ZeroDivisionError:
        c = "На ноль делить нельзя"
    except ValueError:
        c = "Вводить нужно цифры"
    return c

print(f"Деление двух этих чисел даст результат: {func()}")