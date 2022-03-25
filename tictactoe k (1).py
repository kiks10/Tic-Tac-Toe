#Tic-Tac-Toe game
# +-------------+
# | 1  | 8  |   |
# +-------------+
# |    | 5  |   |
# +-------------+
# | 2  |    | 9 |
# +-------------+
# Author : CS111 - 2022 Kamal eldein Tharwat Kamal Mohamed
# Version : 1.0
# Date : 2 March 2022

# Problem solving : Analysis - Design - Implementation - Testing
# Top-down Approach

# 1-Build a game board
# 2- Display game board
# 3- nActions = 0

# 4- While (nActions != 9 )
#        5- Get player 1 action
#        6- Update game board
#        7- if (player 1 is winner)
#             7.a- Print ("player1 Won")
#             7.b- End
#        8- nActions += 1
#        9- if (nActions ==9)
#            9.a- Break

#10- Get player 2 action
#11- Update game board
#12- if (player 2 is winner)
#     2.a- Print (" player 2 Won")
#     2.b- End
#13- nActions += 1
#14- Print ("Draw")
board = [101, 102, 103, 104, 105, 106, 107, 108, 109]
def display_board():
    print("-------------------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " | ")
    print("-------------------------")
    print("| ", board[3], " | ", board[4], " | ", board[5], " |")
    print("-------------------------")
    print("| ", board[6], " | ", board[7], " | ", board[8], " |")
    print("-------------------------")

# print massege
# input action
#valid_action (action is digit) and (action > 0) and (action < = 9) and board[action - 1] != [0,9]
#while (Not valid_action)
#     print(massege)
#     input(action)
#return action
def get_player_action1(player1):
    is_valid1=False
    massege1 = ("please enter number of move from 101 to 109 "+ player1 + ": ")
    while( not is_valid1):
        action1=input(massege1)
        if not action1.isdigit() :
            continue
        else:
            is_valid1 = True
            action1=int(action1)
            is_valid1=is_valid1 and int(action1) >100 and int(action1) <= 109
            is_valid1=is_valid1 and board[int(action1) -101]!=[0,9]
        return action1

def get_player_action11(player1) :
    is_valid11 = False
    massege11 = ("please enter the odd number you want to put "+ player1 +": ")
    while(not is_valid11):
        action11=input(massege11)
        if not action11.isdigit() :
            continue
        if action11 in board :
            continue
        else:
            is_valid11=int(action11)
            is_valid11=is_valid11 and int(action11)>=0 and int(action11) <= 9
            is_valid11=is_valid11 and board[int(action11) -1] != [0,9]
        return action11

def player_action2(player2) :
    is_valid2=False
    massege2 = ("please enter number of move from 101 to 109 "+ player2 + ": ")
    while( not is_valid2):
        action2=input(massege2)
        if not action2.isdigit() :
            continue
        else:
            is_valid2 = True
            action2=int(action2)
            is_valid2=is_valid2 and int(action2) >100 and int(action2) <= 109
            is_valid2=is_valid2 and board[int(action2) -101]!=[0,9]
        return action2

def player_action22(player2):
    is_valid22 = False
    massege22 = ("please enter the even number you want to put "+ player2 +": ")
    while(not is_valid22):
        action22=input(massege22)
        if not action22.isdigit() :
            continue
        if action22 in board :
            continue
        else:
            is_valid22=int(action22)
            is_valid22=is_valid22 and int(action22)>=0 and int(action22) <= 9
            is_valid22=is_valid22 and board[int(action22) -1] != [0,9]
        return action22

def update_board1(action1 , action11) :
    board[action1 - 101]=action11
    display_board()

def update_board2(action2 , action22) :
    board[action2 - 101]=action22
    display_board()

def is_winner():
    diag1 = (int(board[0]) + int(board[4]) + int(board[8])==15)
    diag2 = (int(board[2]) + int(board[4]) + int(board[6])==15)
    col1 = (int(board[0]) + int(board[3]) + int(board[6])==15)
    col2 = (int(board[1]) + int(board[4]) + int(board[7])==15)
    col3 = (int(board[2]) + int(board[5]) + int(board[8])==15)
    row1 = (int(board[0]) + int(board[1]) + int(board[2])==15)
    row2 = (int(board[3]) + int(board[4]) + int(board[5])==15)
    row3 = (int(board[6]) + int(board[7]) + int(board[8])==15)
    return diag1 or diag2 or row1 or row2 or row3 or col1 or col2 or col3

def play_game():
    display_board()
    n_actions=0
    while (n_actions !=9) :
        action1=get_player_action1("player1")
        action11 = get_player_action11("player1")
        update_board1(action1, action11)
        if (is_winner()):
            print( "player1 wins" )
            break
        n_actions+=1
        if (n_actions == 9) :
            break

        action2=player_action2("player2")
        action22=player_action22("player2")
        update_board2(action2 , action22)
        if (is_winner()) :
            print("player2 wins")
            break
        n_actions+=1
    if not ( is_winner()) :
        print("draw")
play_game(