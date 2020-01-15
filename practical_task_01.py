print("Hello, Maria!")
print("This file contains the solution for the first practical task")
print("-------------------------------------------------------------")
print("This is a program for compiling your biography")

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
gend = input("Enter your gender (male/female): ")
mar_stat = input("Are you married? (y/n): ")

if gend == "male" and mar_stat == "y":
    gender = "женат"
elif gend == "male" and mar_stat == "n":
    gender = "холост"
elif gend == "female" and mar_stat == "y":
    gender = "замужем"
elif gend == "female" and mar_stat == "n":
    gender = "холостая"
else
    print("Введены некорректные данные по полу или семейному статусу")

print(f"Приветствую тебя! Меня зовут {name} {surname}. Я родился в {2019 - age} году. В настоящий момент я {gender}!")