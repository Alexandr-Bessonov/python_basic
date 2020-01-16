print("This is the solution to task 6")

print('Приветствую тебя, спортсмен!')
name = input('Введи твоё имя: ')
start = int(input(f'{name}, сколько ты сейчас пробегаешь киллометров в день? (нужно указать целое число) '))
finish = int(input(f'Укажи к какому результату (в км) ты стремишься: '))
result = 0
while True:
    if start < finish:
        start = start * 1.1
        result += 1
    else:
        print(f'{name}, тебе понадобиться {result} дней для достижения цели в {finish} км.')
        break

print(f'{result} - ответ одним натуральным числом - номер дня (как в задании)')
