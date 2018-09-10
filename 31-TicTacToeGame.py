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


def main_program():
    show_board(board)
    while True:
        #Player X
        choice = input("Please choose an empty space for X!\n ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Sorry, that spot already used!")
            time.sleep(1)      
        if x_winner(board, "X"):
            show_board(board)
            print("Congratulations X PLAYER X, you won!")
            break
        show_board(board)           
        if board_full(board):
            print("It's a tie!")
            break

        #Player 0
        choice = input("Please choose an empty space for O!\n ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Sorry, that spot already used!")
            time.sleep(1)      
        if o_winner(board, "O"): 
            show_board(board)
            print("Congratulations O PLAYER O, you won!")  
            break              
        show_board(board)                
        if board_full(board):
            print("It's a tie!")
            break
        

main_program()