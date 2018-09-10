import random
import string as st
import time
import sys


def main_program():
    print("PASSWORD GENERATOR PROGRAM")
    try:
        user = input("Do you want a strong or weak password?\nInsert s/w!\n")
        usernumber = int(input("How many characters do you want in your password?\n"))
        print()
        print("......Processing......")
        time.sleep(5)
        if user.lower() == 's' or user.lower() == 'strong' and usernumber > 0:
            print(f'STRONG PASSWORD GENERATED WITH DEFAULT 8 LENGHT:\n')
            print(strong_password())
            restart_program()
        elif user.lower() == 's' or user.lower() == 'strong' and usernumber >= 8:
            print(f'WEEK PASSWORD GENERATED WITH {usernumber} LENGHT:\n')
            print(weak_password(usernumber))
            restart_program()
        elif user.lower() == 'w' or user.lower() == 'weak' and usernumber > 0:
            print(f'WEEK PASSWORD GENERATED WITH DEFAULT 5 LENGHT:\n')
            print(weak_password(usernumber))
            restart_program()
        elif user.lower() == 'w' or user.lower() == 'weak' and usernumber > 5:
            print(f'WEEK PASSWORD GENERATED WITH {usernumber} LENGHT:\n')
            print(weak_password(usernumber))
            restart_program()
        else:
            print("Wrong input on first question, please insert, strong/s or weak/w!\n")
            print("Initialize the main program again.")
            time.sleep(2)
            main_program()
    except ValueError as e:
        print("Please, insert integer in the second question!\n")
        main_program()

def restart_program():
    print("Are you satisfied with the password?\nDo you want to try another one?\nInsert Yes or No.\n")
    try:
        user_answer = input()
        if user_answer.lower() == 'yes' or user_answer.lower() == 'y':
            main_program()
        if user_answer.lower() == 'no' or user_answer.lower() == 'no':
            print("Exiting the program!")
            time.sleep(2)
            sys.exit()
    except TypeError as a:
        print("You didn't insert: Yes or No!")
        print("Initizalize program, again!")
        restart_program()
    
        
def strong_password(size=8):
    total = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
    liststring = []
    for i in range(size):
        liststring.append(random.choice(total))
    string1 = ''.join(liststring)
    return string1


def weak_password(size=5):
    total2 = st.ascii_lowercase + st.ascii_uppercase + st.digits
    liststring2 = []
    for i in range(size):
        liststring2.append(random.choice(total2))
    string2 = ''.join(liststring2)
    return string2

main_program()






