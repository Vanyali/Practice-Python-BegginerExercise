a = [5, 10, 15, 20, 25]
print(len(a))
def first_last(lst1):
    new_list = [lst1[0],lst1[-1]]
    return new_list

print(first_last(a))


def first_last2(lst1):
    new_list = [lst1[0],lst1[len(lst1)-1]]
    return new_list

print(first_last2(a))




