print("This is the solution to task 1 to lesson 2")

result_list = [26, False, None, "Hello", 74.45]
print(result_list)

length = len(result_list)  # переменная введена для случая, если список вводит пользователь

var = 0

while var < length:
    var_type = result_list[var]
    print(var_type)
    print(type(var_type))
    var += 1

print("End")
