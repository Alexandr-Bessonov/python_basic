my_file = open("text_02.txt", "w")
my_list = ['ЧОтсчитывая время, бьют часы...\n', 'Стараюсь всё успеть, о чём мечтал:\n',
           'Построил дом, деревья есть и сын,\n', 'Но я, видать, большой оригинал...']
my_file.writelines(my_list)
my_file.close()
my_file = open("text_02.txt", "r")
content = my_file.readlines()
print(f"Число строк: {len(content)}")
my_file.close()
my_file = open("text_02.txt", "r")
str_num = 0
while str_num < int(len(content)):
    cont_str = my_file.readline().split(" ")
    print(f'Количество слов в {str_num + 1} строке: {len(cont_str)}')
    str_num += 1
#    print(f'Количество сиволов в {str_num + 1} строке: {len(content[str_num])}')
#    str_num += 1

my_file.close()
