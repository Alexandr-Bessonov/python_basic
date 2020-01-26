print("This is the solution to task 2 to lesson 4")
# print('_' * 150)
# print('')
# print('_' * 150)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = my_list[1:]
new_list = []

k = int(0)
while k < (len(my_list) - 1):
    if res_list[k] > my_list[k]:
        new_list.append(res_list[k])
        k += 1
    else:
        k += 1


# new_list = [r for r in res_list for m in my_list if r > m]
# ______________________________________
# k = 1
#new1_list = [el for el in my_list if my_list[el] > res_list[el-1]]

print(new_list)
#print(new1_list)
