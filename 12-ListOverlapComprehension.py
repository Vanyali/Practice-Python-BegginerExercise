import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Randomly generates two order list in diferent lenght!
#random_list1 = list(range(1,random.randint(1,100)))
#random_list2 = list(range(1,random.randint(1,100)))


#print(random_list1)
#print()
#print(random_list2)

#randomly genrates two  list with random number diferent lenght
random_list3 = list(random.sample(range(500),random.randint(1,100)))
random_list4 = list(random.sample(range(500),random.randint(1,100)))

print()
print(random_list3)
print()
print(random_list4)

#Using Set built in function
no_duplicate1 = set(a)
no_duplicate2 = set(b)

new_list = [i for i in a if i in b]
print(new_list)
print()
#Using function

def Overlap(list1, list2):
    no_duplicate1 = set(list1)
    no_duplicate2 = set(list2)
    overlaplist = [i for i in no_duplicate1 if i in no_duplicate2]
    return overlaplist

print(Overlap(random_list3, random_list4))
    

absd=list(range(2,100))
print(absd[-1])
