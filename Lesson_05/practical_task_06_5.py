def my_func(a):
    num = 0
    var = []
    while num < len(a)-1:
        a = list(a[num])
        try:
            for el in a:
                var.append(int(el))
                num += 1
        except ValueError:
            num += 1
    num = 0
    if number in var:
        num_end = num[0]
    return numb_end

my_dict = dict()
my_list = []
with open ("text_06.txt", 'r') as my_f:
    for line in my_f:
        my_list.append(line.split(" "))
        print(my_list)
        my_dict.update({line.split(" ")[0]: my_func(line.split(" ")[1:])})
        print(my_dict)
print(my_list)
#num = 0
#while num < len(my_list):
#    my_dict.update({"Информатика": "100"})
#    num += 1