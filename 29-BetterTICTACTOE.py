from itertools import cycle

WIN_CONDITIONS = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
]

def welcome_print():
    print('''
        ******WELCOME TO TIC TAC TOE GAME******
            TO INSERT X USE NUMBER 1 TO 9
    Map Below, Each number equivalent of X or O positions!
                  1  |   2   |  3                             
                  4  |   5   |  6 
                  7  |   8   |  9
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


def winner(board, player):
    for positions in WIN_CONDITIONS:
        cell_values = [board[cell] for cell in positions]
        if all(cell == player for cell in cell_values):
            return True
    return False


def board_full(board):
    if " " in board:
        return False
    else:
        return True

def show_board(board):
    print("\n" * 100)
    welcome_print()
    print_board()  

def get_choice(player):
    choice = int(input("Please choose an empty space for {}!\n".format(player)))
    if choice in [1,2,3,4,5,6,7,8,9]:
        return choice
    else:
        print("Please insert numbers between 1-9.\n")
        raise ValueError("Number must be between 1-9")


def clear_spot(board, choice):
    if board[choice] == " ":
        return True
    else:
        return False


def player_choice(board, player):
    valid_choice = False
    while not valid_choice:
        try:
            choice = get_choice(player)
            if clear_spot(board, choice):
                valid_choice = True
        except ValueError:
            pass

    board[choice] = player

def main_program(board):
    show_board(board)

    for player in cycle("XO"):
        player_choice(board, player)

        if winner(board, player):
            show_board(board)
            print("Congratulations {0} PLAYER {0}, you won!".format(player))
            break
        show_board(board)           
        if board_full(board):
            print("It's a tie!")
            break

            
if __name__ == "__main__":
    board = [""] + [" "] * 9
    main_program(board)