my_file = open ("text_02.txt", "w")
my_list = ['Что для меня - печаль? А что - тоска?\n', 'Какие формы принимает - ложь?\n',
           'И - есть ли Истина? И - как её искать?\n', 'И - что же делать, если - не найдёшь?']
my_file.writelines(my_list)
my_file.close()