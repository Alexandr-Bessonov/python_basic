print("This is the solution to task 4 to lesson 4")
print('_' * 150)
from collections import Counter

source = [300, 2, 12, 44, 1, 2, 1, 4, 10, 7, 1, 78, 2, 123, 55]
print(source)
my_list = []
new_gen = [i for i in source if i not in my_list and (my_list.append(i) or True)]

counter = Counter(source)

new_gen = list(counter)

single = [x for x, n in counter.items() if n == 1]
print(single)
