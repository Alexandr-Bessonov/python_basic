print("This is the solution to task 4 to lesson 2")

user_str = "Hello 123456789012345 world"

str_work = user_str.split(" ")
print(str_work)

for ind, el in enumerate(str_work, 1):
    print(ind, el)
