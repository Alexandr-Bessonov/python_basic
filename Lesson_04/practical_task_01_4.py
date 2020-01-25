print("This is the solution to task 1 to lesson 4")
#print('_' * 150)
#print('Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.\n '
#      'В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.\n '
#      'Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.')
#print('_' * 150)

from sys import argv

name, production, rate, prize = argv
print(int(production) * int(rate) + int(prize))
