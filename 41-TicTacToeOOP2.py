from random import *
from time import *


class Play:
    def __init__(self):#Menu - maybe shouldn't be an initialiser
    #self in brackets but not used, i know, it's icky... but it works
        print("Noughts and Crosses")
        print("1 - Play Single Player, against the Computer")
        print("2 - Play Multiplayer with a friend on the same computer")
        print("3 - Play with... oh wait, this isn't right. press 3 to not play at all?")
        Play.Choice = input("Please Enter your Choice: ")
        while Play.Choice not in ['1','2','3']:
            Play.Choice = input("Please type 1,2 or 3 as your Choice: ")
        if Play.Choice == '1':
            Play.GameType = "S"
        elif Play.Choice == '2':
            Play.GameType = "M"
        else:
            print("\nComputer v Computer it is...\n") 
            Play.GameType = "Computer v Computer" # not actally reffered to directly, so can be anything
        Board()
        Play.Type = choice(['X','O'])#more effective than randint
        Play.Round()

        #waiting for game to end...

        if Play.GameWon == True:#if you win...
            print(Play.WinningType, "Wins!")
        else:#if you draw... (will not get to this stage is GameWon is False, as will stay in the loop
            print("Draw!")
        PlayAgain = input("Do you want to play again? Y/es or N/o: ")
        if PlayAgain in ["Yes", "yes", "y", "Y"]:
            print()
            Play()

    def Round():
        Play.GameWon = False
        while not Play.GameWon:#loops until someone wins
            if Play.GameType in ["S","M"]:
                Play.Move()
                Play.CheckWin()
                Play.ChangeType()
            if Play.GameType != "M" and Play.GameWon == False:# If Single Player and the Game has not been Won...
                print(Play.Type+"'s Go...")#Computers Go!
                sleep(1)
                Computer.GetComputersChoice()
                Play.CheckWin()
                Play.ChangeType()

    def Move():
        Play.VerifyPosition()#asks for your square,verifies, then moves
        Board.PrintBoard()#shows the board

    def ChangeType():
        if Play.Type == 'X':
            Play.Type = 'O'
        else:
            Play.Type = 'X'

    def VerifyPosition():
        Valid = False
        print(Play.Type+"'s Go...")#O's Go... / X's Go...
        while not Valid:
            Position = input("Please type where you wish to place: ")
            while Position.isdigit() == False or int(Position) > 9 or int(Position) <= 0:#Ensures the player does not type an incorrect location to place in
                Position = input("Please type a valid integer between 1 and 9: ")
            Play.Position = int(Position)
            if Board.Places[Play.Position-1] == 'X' or Board.Places[Play.Position-1] == 'O':#9 on the keypad would refer to index 8, as starts from 0 but keypad starts at 1
                Valid = False
                print("That is an invalid square, please try again ")
            else:
                Valid = True
        Board.Places[Play.Position-1] = Play.Type#lists start at 0, inputs start at 1, hence -1
        #the board is layed out identical to a Computer's Key-Pad, hence starting at 1 and not 0, requiring -1 to the positional index

    def CheckWin():
        if ((Board.Places[0]== Play.Type) and (Board.Places[1] == Play.Type) and (Board.Places[2] == Play.Type)) or (
            (Board.Places[3]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[5] == Play.Type)) or (
            (Board.Places[6]== Play.Type) and (Board.Places[7] == Play.Type) and (Board.Places[8] == Play.Type)) or (
            #Row Check^^^^^^^
            (Board.Places[0]== Play.Type) and (Board.Places[3] == Play.Type) and (Board.Places[6] == Play.Type)) or (
            (Board.Places[1]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[7] == Play.Type)) or (
            (Board.Places[2]== Play.Type) and (Board.Places[5] == Play.Type) and (Board.Places[8] == Play.Type)) or (
            #Column Check^^^^
            (Board.Places[0]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[8] == Play.Type)) or (
            (Board.Places[2]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[6] == Play.Type)):
            #Diagonal Check^^
            Play.WinningType = Play.Type
            Play.GameWon = True
        if Play.GameWon != True:#if no one wins (potentially on the last go...)
            DrawCheck = 0
            for i in range(0,9):#checks the number of spaces left in the board out of 9 squares, 0-8
                if Board.Places[i] == ' ':
                    DrawCheck = DrawCheck + 1
            if DrawCheck == 0:#if there are no squares...
                Play.GameWon = 'Draw'

class Computer:
    def GetComputersChoice():
        Computer.FindEmptySpaces()
        Computer.ComputerMove()
        Board.PrintBoard() # Prints the Board

    def FindEmptySpaces():
        Computer.EmptySpaces = []
        for i in range(0,9):#goes through all spaces on the board...
            if Board.Places[i] == ' ': #Finds empty spaces...
                Computer.EmptySpaces.append(i) # Adds them to a list for future reference

    def ComputerMove():
        Computer.Change = False
        OriginalType = Play.Type # prevents placing down the opponent's piece when checking for a BLOCK
        for j in range(0,2):#Checks each space twice, FIRST to see if there is a winning move, THEN to check if they can block the opponent
            for i in range(0,len(Computer.EmptySpaces)):#check the space to see FIRST if two friendly pieces are in line for a win, THEN check if you can block an opponent, IF NEITHER, radomise
                if not Computer.Change: # If no change has happened (prevents re-checking after a space has been found)
                    Computer.CheckComputerWin((Computer.EmptySpaces[i])) # checks to see whether the computer can cause a three-in-a-row... or prevent one
                if Computer.Change:    # If there is a change...
                    Board.Places[Computer.EmptySpaces[i]] = OriginalType # Fills in the space
                    Play.Type = OriginalType
                    return
            Play.ChangeType() #switches the type, to see if any draws are available AFTER checking for wins
        Play.Type = OriginalType
        Board.Places[choice(Computer.EmptySpaces)] = OriginalType # If no places were found to have a effect, randomize the location...

    def CheckComputerWin(SpaceToCheck):
        if (SpaceToCheck in [6,3,0] and Board.Places[SpaceToCheck + 1] == Play.Type and Board.Places[SpaceToCheck + 2] == Play.Type) or (#Left Side Checks     |
            SpaceToCheck in [7,4,1] and Board.Places[SpaceToCheck + 1] == Play.Type and Board.Places[SpaceToCheck - 1] == Play.Type) or (#Central Column check | Horizontal Checks
            SpaceToCheck in [8,5,2] and Board.Places[SpaceToCheck - 1] == Play.Type and Board.Places[SpaceToCheck - 2] == Play.Type) or (#Right Side Check     |
            SpaceToCheck in [6,7,8] and Board.Places[SpaceToCheck - 3] == Play.Type and Board.Places[SpaceToCheck - 6] == Play.Type) or (#Top Row Check     |
            SpaceToCheck in [5,4,3] and Board.Places[SpaceToCheck - 3] == Play.Type and Board.Places[SpaceToCheck + 3] == Play.Type) or (#Middle Row Check  | Vertical Checks
            SpaceToCheck in [2,1,0] and Board.Places[SpaceToCheck + 3] == Play.Type and Board.Places[SpaceToCheck + 6] == Play.Type) or (#Bottom Row Check  |
            SpaceToCheck == 0 and Board.Places[SpaceToCheck + 4] == Play.Type and Board.Places[SpaceToCheck + 8] == Play.Type) or ( #Bottom Left  |
            SpaceToCheck == 2 and Board.Places[SpaceToCheck + 2] == Play.Type and Board.Places[SpaceToCheck + 4] == Play.Type) or ( #Bottom Right | Diagonal
            SpaceToCheck == 6 and Board.Places[SpaceToCheck - 2] == Play.Type and Board.Places[SpaceToCheck - 4] == Play.Type) or ( #Top Left     | Checks
            SpaceToCheck == 8 and Board.Places[SpaceToCheck - 4] == Play.Type and Board.Places[SpaceToCheck - 8] == Play.Type) or ( #Top Right    |
            SpaceToCheck == 4 and ((Board.Places[SpaceToCheck + 2] == Play.Type and Board.Places[SpaceToCheck - 2] == Play.Type) or ( # Centre Piece, | Top-Left to Bottom-Right  | Diagonal
                Board.Places[SpaceToCheck + 4] == Play.Type and Board.Places[SpaceToCheck - 4] == Play.Type))):                     # Centre Piece, | Top-Right to Bottom-Left  | Checks
            Computer.Change = True
class Board:
    def __init__(self):
        if Play.GameType in ["S", "M"]:
            Board.Places = ['1','2','3',#for the initial board - to show the player which key relates to which position
                            '4','5','6',
                            '7','8','9']#flipped as Key-Pads are flipped
            print("This is  how the Board is layed Out (Key-Pad use recommended)")
            Board.PrintBoard()
        Board.Places = [' ',' ',' ',
                        ' ',' ',' ',
                        ' ',' ',' ']
        if Play.GameType not in ["S","M"]:
            Board.PrintBoard()
            sleep(1)

    def PrintBoard(): #Prints the Board, mirrors a laptop's keypad
        print('',Board.Places[6],'|',Board.Places[7],'|',Board.Places[8],'')
        print('---|---|---')
        print('',Board.Places[3],'|',Board.Places[4],'|',Board.Places[5],'')
        print('---|---|---')
        print('',Board.Places[0],'|',Board.Places[1],'|',Board.Places[2],'')
        print()#empty line at the bottom to make room for further prompts


Play()