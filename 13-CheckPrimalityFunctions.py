#Check if the number is prime!

def integer():
    num = int(input("Please, insert an number!\n"))
    return num

number_to_check = integer()

def check_if_prime(num):
    if num == 2:
        print(num, "is prime")
    else:
        if num > 1:
            for i in range(2,num):  
                if (num % i) == 0:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                    break
                else:
                    print(num,"is a prime number")
        else:
            print(num,"is not a prime number")

check_if_prime(number_to_check)
