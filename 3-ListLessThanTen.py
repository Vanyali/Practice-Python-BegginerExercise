lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Insert a number!\n")
user_number = int(input("Numbers, not letters! Don't make it to put try exception! :D \n"))#
new_a = []
for i in lst:
    if i < user_number:
        new_a.append(i)
print("My list in one line is", new_a)


#Simples Solution with List Comprehension
user = int(input("Insert Number!\n"))
mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [i for i in mylist if i < user]
print(a)




