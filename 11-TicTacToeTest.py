#:D

#import antigravity

import os
import time
import random


board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def welcome_print():
    print('''
        ******WELCOME TO TIC TAC TOE GAME******
            TO INSERT X USE NUMBER 1 TO 9
    Map Below, Each number equivalent of X or O positions!

                  1 |   2   | 3                             
                  4 |   5   | 6 
                  7 |   8   | 9
    ''')
    print()


def print_board():

    print("    |     |   ")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3]+" ")
    print("____|_____|____")
    print("    |     |   ")
    print(" "+board[4]+"  |  "+board[5]+"  |  "+board[6]+" ")
    print("____|_____|____")
    print("    |     |   ")
    print(" "+board[7]+"  |  "+board[8]+"  |  "+board[9]+" ")
    print("    |     |   ")



def x_winner(board, player):
    if  (board[1] == player and board[2] == player and board[3] ==player) or \
        (board[4] == player and board[5] == player and board[6] ==player) or \
        (board[7] == player and board[8] == player and board[9] ==player) or \
        (board[1] == player and board[4] == player and board[7] ==player) or \
        (board[2] == player and board[5] == player and board[8] ==player) or \
        (board[3] == player and board[6] == player and board[9] ==player) or \
        (board[1] == player and board[5] == player and board[9] ==player) or \
        (board[3] == player and board[5] == player and board[7] ==player):
        return True
    else:
        return False

def o_winner(board, player):
    if  (board[1] == player and board[2] == player and board[3] ==player) or \
        (board[4] == player and board[5] == player and board[6] ==player) or \
        (board[7] == player and board[8] == player and board[9] ==player) or \
        (board[1] == player and board[4] == player and board[7] ==player) or \
        (board[2] == player and board[5] == player and board[8] ==player) or \
        (board[3] == player and board[6] == player and board[9] ==player) or \
        (board[1] == player and board[5] == player and board[9] ==player) or \
        (board[3] == player and board[5] == player and board[7] ==player):
        return True
    else:
        return False

def board_full(board):
    if " " in board:
        return False
    else:
        return True

def show_board(board):
    os.system("cls")
    welcome_print()
    print_board()  

def user_choice_X():
    try:
        choice = int(input("Please choose an empty space for X!\n"))
        if choice in [1,2,3,4,5,6,7,8,9]:
            return choice
        else:
            print("Please insert numbers between 1-9.\n")
            user_choice_X()
    except ValueError:
        print("Please insert integers between 1-9!")
        user_choice_X()

def user_choice_O():
    try:
        choice = int(input("Please choose an empty space for O!\n"))
        if choice in [1,2,3,4,5,6,7,8,9]:
            return choice
        else:
            print("Please insert numbers between 1-9.\n")
            user_choice_O()
    except ValueError:
        print("Please insert integers between 1-9!")
        user_choice_O()

def same_spot_X(board, choice):
    if board[choice] == " ":
            board[choice] = "X" 
            return board   
    else:
        print("Sorry, that spot already used!")
        user_choice_X()
        

def same_spot_O(board, choice):
    if board[choice] == " ":
            board[choice] = "O" 
            return board    
    else:
        print("Sorry, that spot already used!")
        return board
        user_choice_O()
        

def main_program():
    print("Para a proxima e favor bloquear o ecra!!!!!!")
    show_board(board)
    while True:
        #Player X
        user = user_choice_X()
        choice = int(user)
        same_spot_X(board, choice)

        if x_winner(board, "X"):
            show_board(board)
            print("Congratulations X PLAYER X, you won!")
            break
        show_board(board)           
        if board_full(board):
            print("It's a tie!")
            break

        #Player 0
        user = user_choice_O()
        choice = int(user)
        same_spot_O(board, choice)

        if o_winner(board, "O"): 
            show_board(board)
            print("Congratulations O PLAYER O, you won!")  
            break              
        show_board(board)                
        if board_full(board):
            print("It's a tie!")
            break
        

main_program()