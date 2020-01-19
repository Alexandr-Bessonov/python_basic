print("This is the solution to task 6 to lesson 2")
print('_' * 150)
print('Задание №6: Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. \n'
      'Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара \n'
      'и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). \n'
      'Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.')
print('_' * 150)

goods = []  # создаем пустой список "Товары"

quantity = int(input('Какое количество товары Вы хотите добавить? '))
a = 0
var = 1
while a < quantity:
    user_list = input('Введите через "/" Инфорамцию о товаре \n'
                      'Наименование товара/Цена товара/Количество/ Единицы измерения: ')

    my_list = user_list.split("/")

    my_dict = {}  # создаем пустой словарь
    my_dict.update(
        {"Название": my_list[0], "Цена": int(my_list[1]), "Количество": int(my_list[2]), "Ед": my_list[3]})  # наполняем словарь
    my_tuple = (var, my_dict)
    goods.append(my_tuple)
    var += 1
    a += 1

print(f"Каталог товаров: \n{goods}")
print('_' * 150)
print('Далее выводим аналитику по данному катологу:')

analitics = {}  # создаем словарь для аналитики

param_1 = []
var = 0
while var < quantity:
    if goods[var][1].get("Название") in param_1:
        var += 1
        continue
    else:
        param_1.append(goods[var][1].get("Название"))
        var += 1

param_2 = []
var = 0
while var < quantity:
    if goods[var][1].get("Цена") in param_2:
        var += 1
        continue
    else:
        param_2.append(goods[var][1].get("Цена"))
        var += 1

param_3 = []
var = 0
while var < quantity:
    if goods[var][1].get("Количество") in param_3:
        var += 1
        continue
    else:
        param_3.append(goods[var][1].get("Количество"))
        var += 1

param_4 = []
var = 0
while var < quantity:
    if goods[var][1].get("Ед") in param_4:
        var += 1
        continue
    else:
        param_4.append(goods[var][1].get("Ед"))
        var += 1

analitics.update({"Название": param_1, "Цена": param_2, "Количество": param_3, "Ед": param_4})

print(analitics)
