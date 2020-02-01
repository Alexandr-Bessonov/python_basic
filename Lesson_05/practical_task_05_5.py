with open("text_05.txt", 'w') as f_num:
    f_num.write('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')
result = []
with open("text_05.txt", 'r') as f_num:
    for el in f_num:
        result.append(el)
end = result[0].split(" ")
num_el = 0
summa = 0
while num_el < len(end):
    if num_el < len(end):
        summa = summa + int(end[num_el])
        num_el += 1
print(f'Сумма элементов в файле: {summa}')
