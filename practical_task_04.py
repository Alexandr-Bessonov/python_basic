print("This is the solution to task 4")
maxi = 0
number = int(input("Введите любое число от 1 до 9999: "))

while True:
    if number <= 9:
        num = number
        maxi = num
        break
    else:
        num = number % 10
        if num == 9:
            maxi = num
            break
        elif num > maxi:
            maxi = num
        else:
            number = int(number / 10)
        if number <= 9:
            num = number
            if num > maxi:
                maxi = num
                break
            else:
                maxi = maxi


print(f"Максимальное из введенных, число {maxi}")