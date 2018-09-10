
import random

a = [1,2,3,4,3,2,1,2,3,4,5,6,7,4,213,4,5,6,7,4,2]

new_a = []
for i in a:
    if i not in new_a:
        new_a.append(i)

print(new_a)

#OR

print(list(set(a)))
    