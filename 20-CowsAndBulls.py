import random
import sys

def compare_lists(guesslist1, testlist1):
    cow = 0
    bull = 0
    for i in range(0,4):
        if guesslist1[i] in testlist1:
            if guesslist1[i] == testlist1[i]:
                cow += 1                    
            else:
                bull += 1          
        else:
            print("Nothing inplace!\n")
    return cow, bull
    
if __name__ == "__main__":
    cow = 0
    bull = 0
    playing = True
    guesses = 0
    testlist = [1,2,3,4]
    ran_number = random.sample([1,2,3,4,5,6,7,8,9,0], 4)
    while playing:
        try: 
            guess_user = int(input("Inser 4 digit number!\n"))
            guesslist = [int(i) for i in str(guess_user)]
            startgame = compare_lists(guesslist, ran_number)
            guesses += 1
            print(f"You have {startgame[0]} cows and {startgame[1]} bulls. ")
            if startgame[0] == 4:
                playing = False
                print(f"You won this game! You guessed right with {guesses} guess!")
            else:
                print("Keep Trying!\n")
        except (IndexError, ValueError) as e:
            print("Your guess must have 4 digits at least or you inserted letters not numbers!")
            
        






        





