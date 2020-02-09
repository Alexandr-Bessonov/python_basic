# practical task #2
class My_Exception(Exception):
    def __init__(self, txt):
        self.txt = txt


user_num = input('Введите число, на которое необходимо поделить 555: ')

try:
    user_num = int(user_num)
    if user_num == 0:
        raise My_Exception('Деление на "0" запрещено!')
except ValueError:
    print('Вы ввели не число :(')
except My_Exception as My_Exception:
    print(My_Exception)
else:
    print(f'Результат деления 555 на {user_num} = {round(555 / user_num, 2)}')
