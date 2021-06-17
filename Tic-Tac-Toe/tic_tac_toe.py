import random

board = {
    '1': "_", '2': "_", '3': "_",
    '4': "_", '5': "_", '6': "_",
    '7': "_", '8': "_", '9': "_"
}

players = ["X", "O"]

def display_board(board):    
    print('  ', board['1'], '  |','  ' ,board['2'], '  |', '  ',board['3'])
    print('-------+--------+--------')
    print('  ', board['4'], '  |','  ' ,board['5'], '  |', '  ',board['6'])
    print('-------+--------+--------')
    print('  ', board['7'], '  |','  ' ,board['8'], '  |', '  ',board['9'], '\n')

def clear_board():
    for key in board:
        board[key] = "_"


def play_game():
    current_player = random.choice(players)
    moves_count = 0
    for i in range(10):
        display_board(board)
        current_move = input(f"'{current_player}' to move. Please pick a position from 1 to 9: ")
        if board[current_move] == "_":
            board[current_move] = current_player
            moves_count += 1
        else:
            print("That place is occupied. Pick another position.")
            continue
        if moves_count >= 5:
            if board['1'] == board['2'] == board['3'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break
            elif board['4'] == board['5'] == board['6'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break
            elif board['7'] == board['8'] == board['9'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break
            elif board['1'] == board['4'] == board['7'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break
            elif board['2'] == board['5'] == board['8'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break
            elif board['3'] == board['6'] == board['9'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break
            elif board['1'] == board['5'] == board['9'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break            
            elif board['3'] == board['5'] == board['7'] != '_':
                display_board(board)
                print(f"Game is over! {current_player} won!")
                break

        if moves_count == 9:
            print("Game Over. It is a tie.")

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    play_again = input("Do you want to play again? (y/n")
    if play_again in ["y", "Y"]:
        clear_board()
        play_game()


play_game()