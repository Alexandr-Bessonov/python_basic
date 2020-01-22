print("This is the solution to task 2 to lesson 3")
print('_' * 150)
print('Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:\n'
      'имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры\n'
      'как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.')
print('_' * 150)

def information (name, surname, year, town, email, phone):
    return f"{surname} {name} {year} года рождения, проживает в городе {town}, почтовый ящик:{email}, номер телефона: {phone}"


name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
year = input("Введите год рождения: ")
town = input("Введите город проживания: ")
email = input("Введите адрес почтвого ящика: ")
phone = input("Введите Ваше номер телефона: ")
print(f'Справочная информация: {information(name, surname, year, town, email, phone)}')