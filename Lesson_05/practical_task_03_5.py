#f = open("text_03.txt", 'r')
#num = int(len(f.readlines()))
my_dict = dict()
my_list = []

with open('text_03.txt') as f:
    for line in f:
        var = (line.split())
        my_dict[var[0]] = var[1]
        if (float(var[1])) < 20000:
            my_list.append(var[0])

print(f"Оклад меньше 20000 рублей у: {my_list}")

var_2 = my_dict.values()
var_3 = 0
for el in var_2:
    var_3 += float(el)

print(f'Средний доход всех сотрудников: {round((var_3 / len(var_2)), 2)} рублей.')
