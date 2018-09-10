import random

list1 = list(range(1, random.randint(5,100)))
list2 = list(range(1,random.randint(5,100)))
print(list1, list2)
print()
new_list = [i for i in list1 if i in list2]
print(new_list)