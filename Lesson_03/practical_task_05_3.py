print("This is the solution to task 5 to lesson 3")
print('_' * 150)


def func_0(str_a):
    try:
        str_a.index("q")
    except ValueError:
        return -2
    return list(str_a.index("q"))


def func_1(a):
    list_a = []
    i = 1
    while i < len(a):
        a.pop(i)
        i += 1

    for el in a:
        el = int(el)
        list_a.append(el)
    return list_a


def func_2(b, var):
    b.pop(var)
    return sum(func_1(b))


summ = 0
while True:
    str_a = list(input("Введите строку чисел, разделенных пробелом: \n"
                       "Для выхода добавьте \"q\": "))
    if func_0(str_a) >= 0:
        print(f'Мы закончили подсчет. Итого сумма получается: {func_2(str_a, func_0(str_a))}')
        break
    else:
        summa_1 = sum(func_1(str_a))
        print(f'Промежуточная сумма: {summa_1 + summ}')
        summ = summ + summa_1
