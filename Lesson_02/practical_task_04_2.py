print("This is the solution to task 4 to lesson 2")

user_str = input('Введите строку из нескольких слов, разделяя их пробелом: ')

print(f'Введенная строка: {user_str}')
print('Результат преобразования: ')

str_work = user_str.split(" ")
var: int = 0
while (var + 1) <= len(str_work):
    if len(str_work[var]) > 10:
        str_ind = str_work[var]
        str_ind = str_ind[:10]
        str_work.insert(var, str(str_ind))
        str_work.pop(var + 1)
        var += 1
    else:
        var += 1

for ind, el in enumerate(str_work, 1):
    print(ind, el)
