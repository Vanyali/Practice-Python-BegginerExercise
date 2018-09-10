import random
import sys

def user_choice():
    user_guess = input("Escolhe um numero de 1 a 9?\n")
    return user_guess

def computerchoice():
    computer_choice = random.randint(1,9)
    return computer_choice

def play_again():
    print("Jogo acabou!\n")
    ask1 = input("Queres jogar outra vez? Escreve y/n!")
    if ask1 == 'y':
        print("Ok, vamos lá tentar outra vez:")
        play()
    elif ask1 == 'n':
        print("Até a próxima!")
        sys.exit()
    else:
        print("Escreve y ou n! Caralho fds!")
        play_again()


def play():
    computer1 = computerchoice()
    user1 = 0
    score = 0
    tries = 0
    while user1 != "exit":
        print("Escreve exit para sair! ")
        user1 = int(user_choice())
        if user1 == "exit":
            print("Até a próxima!")
            break

        if user1 < computer1:
            print(f"Too Low! Present score is {score} and {tries}")
            tries += 1
        elif user1 > computer1:
            print(f"Too High! Present score is {score} and {tries}")
            tries += 1
        else:
            print(f"You got it right! Present score is {score} and {tries}")
            score += 1
    play_again()
    
play()



        








   