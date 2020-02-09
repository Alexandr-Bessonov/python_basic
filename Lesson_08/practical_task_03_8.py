# practical task #3
class My_Exception:
    def __init__(self):
        self.result = []

    def check(self):

        while True:
            stop = "stop"
            try:
                user_num = int(input('Введите число для добавления в список\n '
                                     'Либо введите "stop" для выхода: '))
                self.result.append(user_num)
                print(f'Текущий список - {self.result} \n ')
            except ValueError:
                user = input("Вы ввели не число, если хотите выйти введите 'stop'")
                if user == stop:
                    return f'Вы вышли\nРезультат: {self.result}'
                else:
                    print(my_check.check())


my_check = My_Exception()
print(my_check.check())