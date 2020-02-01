f = open("Text.txt", "w")
while True:
    uzer_list = input("Введите текст: ")
    if uzer_list == '':
        break
    else:
        f.writelines(f"{uzer_list}\n")
f.close()
