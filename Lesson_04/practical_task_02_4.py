print("This is the solution to task 2 to lesson 4")
print('_' * 150)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [num for ind, num in enumerate(my_list) if ind != 0 and my_list[ind] > my_list[ind - 1]]

print(new_list)

print('_' * 150)
print("Второй вариант решения")
res_list = my_list[1:]
new_2_list = []

k = int(0)
while k < (len(my_list) - 1):
    if res_list[k] > my_list[k]:
        new_2_list.append(res_list[k])
        k += 1
    else:
        k += 1

print(new_2_list)
