print("This is the solution to task 2 to lesson 4")
# print('_' * 150)
# print('')
# print('_' * 150)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [int(i) for i in my_list if i != 0 and my_list[i] > my_list[i-1]]

print(new_list)
