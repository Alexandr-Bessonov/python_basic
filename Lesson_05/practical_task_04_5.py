with open("text_04.txt", 'r') as my_f:
    content = my_f.readlines()
print(content)
var = []
for el in content:
    var.append(el.split())
print(var)
rus_dict = ['Один', 'Два', 'Три', 'Четыре']
new_dict = []
num = 0
while num < len(var):
    my_dick = var[num]
    var[num].remove(my_dick[0])
    var[num].remove(my_dick[0])
    var[num].insert(0, rus_dict[num])
    num += 1
f_end = open("text_04_2.txt", 'w')
num = 0
while num < len(var):
    f_end.write(f"{var[num]}\n")
    num += 1
f_end.close()
print(var)
