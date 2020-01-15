print("This is a two task")

sec = int(input("Введите любое количество секунд: "))

if sec < 60:
    clock = "00"
    minuts = "00"
    if sec >= 0 and sec < 10:
        seconds = "0" + str(sec)
    else:
        seconds = sec
elif sec < 0:
    print("Количество секунд должно быть положительным числом")
elif sec > 59:
    if sec >= 3600:
        clock = sec // 3600
        if clock >= 0 and clock < 10:
            clock = "0" + str(clock)
        else:
            clock = clock
        minuts = (sec % 3600) // 60
        if minuts >= 0 and minuts < 10:
            minuts = "0" + str(minuts)
        else:
            minuts = minuts
        seconds = (sec % 3600) % 60
        if seconds >= 0 and seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = seconds

print(f"Ваши {sec} могут записать в следующем виде: { clock }:{ minuts }:{ seconds }")
print("* время изложено в формате: чч:мм:сс")