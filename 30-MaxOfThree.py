#var1, var2, var3 = input("Enter to numbers:\n").split()


def find_max():
    user_lst = [int(x) for x in input("Enter a list of integers!\n").split()]
    print(user_lst)
    max_of_user_input = user_lst[0]
    for i in range(len(user_lst)):
        if user_lst[i] > user_lst[0]:
            max_of_user_input = user_lst[i]
    return print(max_of_user_input)


find_max()
