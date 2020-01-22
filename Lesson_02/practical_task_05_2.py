print("This is the solution to task 5 to lesson 2")
print('_' * 150)
print('Задание: Реализовать структуру «Рейтинг», представляющую собой '
      'не возрастающий набор натуральных чисел. \nУ пользователя необходимо '
      'запрашивать новый элемент рейтинга.\nЕсли в рейтинге существуют элементы '
      'с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.')

print('_' * 150)

my_list = [7, 5, 3, 3, 2]

print(my_list)

while True:
    user_number = input('Введите новый элекмент рейтинга \n(для выхода наберите "exit"): ')
    if user_number == "exit":
        print('Спасибо за уделенное время!')
        print(f"Окончательный ретинг выглядит следующим образом: {my_list}")
        break
    else:
        user_number = int(user_number)
        if user_number <= 0:
            print("Нужно вводить только положительные числа")
            continue
        elif len(my_list) == 0:
            my_list.inser(0, user_number)
        elif user_number in my_list:
            my_list.insert((my_list.index(user_number) + my_list.count(user_number)), user_number)
        else:
            var = 1
            while True:
                if (user_number + var) in my_list:
                    my_list.insert((my_list.index(user_number + var) + my_list.count(user_number + var)), user_number)
                    break
                elif (user_number - var) in my_list:
                    my_list.insert(my_list.index(user_number - var), user_number)
                    break
                else:
                    var += 1
        print(my_list)
