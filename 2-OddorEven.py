while True:
    try:
        user_number = int(input("Insert a number, num!\n"))
        check = int(input("Inser number to check if the first number is divible by it\n"))
    except ValueError:
        print("Please insert numbers, not other characters!\n")
        continue
    else:
        break

if user_number % 4 == 0:
    print(user_number, "is a multiple of 4")
elif user_number % 2 ==0:
    print(f"{user_number} is even")
else:
    print(user_number, "is odd!")
if user_number % check == 0:
    print(f"The {user_number} is divisible evenly by {check}")
else:
    print("It's not divisible!")





