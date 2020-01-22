print("This is the solution to task 2 to lesson 2")

result_list = []  # создаем пустой список
quantity = int(input('Введите количество элементов в списке: '))
var = 0  # временная переменная для создания списка
var_2 = 0  # временная переменая для индексации элементов списка

while var < quantity:
    user_input = input('Введите число: ')
    result_list.append(user_input)
    var += 1

if quantity % 2 == 0:
    while var_2 < quantity:
        result_list.insert(var_2, result_list[var_2 + 1])
        result_list.pop(var_2 + 2)
        var_2 += 2
else:
    while var_2 < (quantity - 1):
        result_list.insert(var_2, result_list[var_2 + 1])
        result_list.pop(var_2 + 2)
        var_2 += 2

print(result_list)

print('_' * 150)
print("Второй вариант решения")

i = []  # создаем пустой список
quantity = int(input('Введите количество элементов в списке: '))
var = 0
while var < quantity:
    user_input = input('Введите число: ')
    i.append(user_input)
    var += 1

i[:-1:2], i[1:-1:2] = i[1:-1:2], i[:-1:2]
print(i)
