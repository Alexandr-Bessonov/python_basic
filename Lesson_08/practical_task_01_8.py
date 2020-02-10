# practical task #1
''' Кирилицей написал один метод, что бы проверить его работу (больше так не буду делать :)) '''


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def first(cls, date):
        my_date = []

        for el in date.split():
            if el != '-': my_date.append(el)

        return f'Дата: {int(my_date[0])}, Месяц: {int(my_date[1])}, Год: {int(my_date[2])}'

    @staticmethod
    def второй(day, month, year):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if 1 <= day <= 31:
                if 0 <= year <= 2020:
                    return True
                else:
                    return f'Неправильно указан год'
            else:
                return f'Неправильно указан день'
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 1 <= day <= 30:
                if 0 <= year <= 2020:
                    return True
                else:
                    return f'Неправильно указан год'
            else:
                return f'Неправильно указан день'
        elif month == 2:
            if 1 <= day <= 28:
                if 0 <= year <= 2020:
                    return True
                else:
                    return f'Неправильно указан год'
            else:
                return f'Неправильно указан день'
        else:
            return f'Неправильно указан месяц'

    def __str__(self):
        return f'Сейчас: {Date.first(self.date)}'


today = Date('09 - 02 - 2020')
print(today)
print(f'Через класс: {Date.first("9 - 02 - 2020")}')
print(f'Через метод: {today.first("10 - 02 - 2020")}')
print(Date.второй(10, 11, 3012))
print(today.второй(22, 13, 2019))
print(today.второй(30, 2, 2018))
print(Date.второй(9, 2, 2020))
