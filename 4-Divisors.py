print("Insert a number we gonna create a list of range of that number and inform you what numbers from that list that are divisors of that numbers.\n")
usernumber = int(input())

a = range(1, usernumber)
mylist = list(a)
new_list = [num for num in mylist if usernumber % num == 0]
print(new_list)