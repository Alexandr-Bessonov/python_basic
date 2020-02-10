# practical task #4-6
class StorehouseEquipment:

    def __init__(self, type, title, price, quantity):
        self.type = type
        self.title = title
        self.price = price
        self.quantity = quantity
        self.my_dict = []
        self.my_unit = {'Тип оборудования': type, 'Модель устройства': self.title, 'Цена за ед': self.price,
                        'Количество': self.quantity}


class Equipment(StorehouseEquipment):

    def reception(self):

        try:
            user_type = input(f'Введите тип оборудования(printer / scanner / copier): ')
            user_title = input(f'Введите наименование оборудования: ')
            user_price = int(input(f'Введите стоимость за ед оборудования: '))
            user_quantity = int(input(f'Введите количество '))
            user_unit = {'Тип оборудования': user_type, 'Модель устройства': user_title, 'Цена за ед': user_price,
                         'Количество': user_quantity}
            self.my_unit.update(user_unit)
            self.my_dict.append(self.my_unit)
            print(f'Текущий список: {self.my_dict}')
        except:
            return f'Ошибка ввода данных'
        exit = input(f'Для продолжение - Enter, либо "q" для выхода: ')
        if exit == 'q' or exit == 'Q':
            print(f'Весь склад -\n {self.my_dict}')
            selection = input(f'Введите тип оборудования(printer / scanner / copier) для сортировки: ')
            if selection == "print":
                pass
            elif selection == "scan":
                pass
            elif selection == "copier":
                pass
            else:
                print(f'Введен неизвестный параметр \n'
                      f'К сожалению не успел реализовать сортировку через классы устройств :(')
            return f'Выход'
        else:
            return Equipment.reception(self)

    def __str__(self):
        return f'{self.type} {self.title} цена {self.price} количество {self.quantity}'


class Printer(Equipment):
    def printer(self):
        return f'{self.type}'


class Scanner(Equipment):
    def scanner(self):
        return f'{self.type}'


class Copier(Equipment):
    def copier(self):
        return f'{self.type}'


unit = Printer(print, 'hp', 500, 15)
print(unit.reception())
