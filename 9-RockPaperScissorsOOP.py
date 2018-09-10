import random
import sys

class Player:
    def __init__(self):
        self.score = 0
        self.draw = 0

    def update_score(self):
        self.score += 1

    def update_draw(self):
        self.draw += 1
        
class ComputerPlayer(Player):
    
    def choose(self):
        computer_choice = random.choice("rps")
        return computer_choice

class UserPlayer(Player):

    def choose(self):
        user_ch = input(" Your choice? ")
        while user_ch != "r" and user_ch != "p" and user_ch != "s":
            print("Wrong input, Please again!\n")
            user_ch = input(" Your choice? ")
        return user_ch

class Game: 

    def play_again(self):
        print("Game Over")
        choice = input(" Would you like to play again? (Y/N) ")
        if choice == "y" or choice == "Y":
            self.play()
        elif choice == "n" or choice == "N":
            sys.exit()
        else:
            print("Wrong input, Please try again.\n")
            self.play_again()

    def compare_choices(self, computer_choice, user_choice):
        results = {('r','p'):'computer',
          ('r','s'):'user',
          ('r','r'):None,
          ('p','r'):'user',
          ('p','s'):'computer',
          ('p','p'):None,
          ('s','r'):'computer',
          ('s','p'):'user',
          ('s','s'):None}       
        for key, value in results.items():
            if (computer_choice == key[1]) and (user_choice == key[0]):
                result = value
        return result

    def play(self):
        user = UserPlayer()
        computer = ComputerPlayer()      
        for _ in range(1,6):
            user_ch = user.choose()
            computer_ch = computer.choose()
            result = self.compare_choices(user_ch, computer_ch)

            if result == "user":
                user.update_score()
                print(f"Your choice was {user_ch}, the computer's choice was {computer_ch}!")
                print("You won!")
            elif result == "computer":
                computer.update_score()
                print(f"Your choice was {user_ch}, the computer's choice was {computer_ch}!")
                print("You lost, computer wins!")
            else:
                computer.update_draw()
                print(f"Your choice was {user_ch}, the computer's choice was {computer_ch}!")
                print("It was a draw!")               
            
        print(f"Your score was: {user.score}! The Computer's score was: {computer.score}!Draws: {computer.draw}!")
        if user.score > computer.score:
            print("You are the WINNER, CONGRATULATIONS! \n\n")
        else:
            print("The Computer is the WINNER. \n\n")
        self.play_again()

if __name__ == "__main__":
    game = Game()
    game.play()
                

    




    







