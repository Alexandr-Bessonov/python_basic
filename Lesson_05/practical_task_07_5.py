import json


def my_func(srez):
    return int(srez[0]) - int(srez[1])


def profit(my_dict):
    prof = my_dict.values()
    prof_list = []
    for el in prof:
        if el > 0:
            prof_list.append(el)
        else:
            continue
    return sum(prof_list) / len(prof_list)


var = []
my_dict = dict()

with open("text_07.txt", 'r', encoding='utf-8') as my_f:
    for line in my_f:
        var.append(line.split())
num = 0
while num < len(var):
    my_dict.update({var[num][0]: my_func(var[num][2:])})
    num += 1
print(my_dict)

result = []
result.append(my_dict)
result.append({"average_profit": profit(my_dict)})
print(result)

with open('text_07.json', 'w', encoding='utf-8') as my_file:
    json.dump(result, my_file)
