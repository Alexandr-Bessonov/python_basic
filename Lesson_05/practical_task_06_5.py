def my_func_2(text):
    if text == 'None':
        return ''
    else:
        return text


def my_func(a):
    num = 0
    var_1 = []
    var_2 = []
    var_3 = []
    var = [var_1, var_2, var_3]
    while num < len(a):
        element = list(a[num])
        var_x = var[num]
        for el in element:
            try:
                var_x.append(int(el))
            except ValueError:
                num += 1
                break

    n = 0
    res_1 = ''
    while n < len(var_1):
        if my_func_2(var_1[n]) == var_1[n]:
            res_1 = res_1 + str(var_1[n])
            n += 1

    res_1 = int(res_1)

    n = 0
    res_2 = ''
    while n < len(var_2):
        if my_func_2(var_2[n]) == var_2[n]:
            res_2 = res_2 + str(var_2[n])
            n += 1

    res_2 = int(res_2)

    n = 0
    res_3 = ''
    while n < len(var_3):
        if my_func_2(var_3[n]) == var_3[n]:
            res_3 = res_3 + str(var_3[n])
            n += 1

    res_3 = int(res_3)


    return res_1 + res_2 + res_3


my_dict = dict()
my_list = []
with open("text_06.txt", 'r') as my_f:
    for line in my_f:
        my_list.append(line.split(" "))
        #        print(my_list)
        my_dict.update({line.split(" ")[0]: my_func(line.split(" ")[1:])})
print(my_dict)
