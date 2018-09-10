import random
import sys

user_score = 0
computer_score = 0

def computer_choice():
    computer_ch = random.choice("rps")
    return computer_ch

def user_choice():
    user_ch = input("Your choice? Options: r p s \n")
    if user_ch != "r" and user_ch != "p" and user_ch != "s":
        print("Wrong input, Try again.\n")
        user_choice()
    else:
        return user_ch
        

def compare_choice(user_choice, computer_choice):
    if user_choice == 'r' and computer_choice == 'p':
        return "computer"
    elif user_choice == "r" and computer_choice == "s":
        return "user"
    elif user_choice == "r" and computer_choice == "r":
        return "n" # n means nulL
    elif user_choice == "p" and computer_choice == "r":
        return "user"
    elif user_choice == "p" and computer_choice == "s":
        return "computer"
    elif user_choice == "p" and computer_choice == "p":
        return "n"
    elif user_choice == "s" and computer_choice == "r":
        return "computer"
    elif user_choice == "s" and computer_choice == "p":
        return "user"
    elif user_choice == "s" and computer_choice == "s":
        return "n"

def play_again():
    print("Game Over")
    choice = input(" Would you like to play again? (Y/N)")
    if choice == "y" or choice == "Y":
        play()
    elif choice == "n" or choice == "N":
        sys.exit()
    else:
        print("Wrong input, Please try again.\n")
        play_again()

def play():
    global user_score, computer_score 
    i = 0
    turn_left = 10
    print("Let's play Rock Paper Scissors! For 10 turns!\n")
    while i < 10:
        user_c = user_choice()
        computer_c = computer_choice()
        result = compare_choice(user_c, computer_c)
        if result == "user":
            user_score += 1
            turn_left -= 1
            print(f"Your choice {user_c}, the computer choice {computer_c}")
            print(f"You Won this round! Turns left: {turn_left} \n")
        elif result == "computer":
            computer_score +=1
            turn_left -= 1
            print(f"Your choice {user_c}, the computer choice {computer_c}")
            print(f"You lost this round! {turn_left}Turns left: {turn_left} \n")
        else:
            turn_left -= 1
            print(f"Your choice {user_c}, the computer choice {computer_c}")
            print(f"It was a draw in this round! Turns left: {turn_left} ")  
        i += 1
    print(f"Your score was: {user_score}, the computer score was: {computer_score} ")
    if user_score > computer_score:
        print("You are the winner!")
    else:
        print("You are a loser!")

play()





