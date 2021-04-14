# File: minesweeper_game.py
# Author: Didzis Zvaigzne
# Description: Minesweeper game which includes two classes
#              Board class and Cell class
#              Game works just as a normal Minesweeper game,
#              except by using the command line interface

from Board import Board


def play():
    visual_line = "----------------------------------"
    board_size = 10
    bomb_size = 10
    # Create the Minesweeper game with specified board size and the amount of bombs
    minesweeper = Board(board_size, bomb_size)
    # Create the board and fill it with bombs
    minesweeper.create_the_board()

    game_not_over = True

    while minesweeper.free_spots > len(minesweeper.revealed_squares):
        print(minesweeper)
        user_row = int(input("Select row: "))
        user_column = int(input("Select column:"))
        if user_row < 0 or user_row >= minesweeper.board_size or user_column < 0 or user_column >= minesweeper.board_size:
            print("You provided wrong row or column. Try again.")
            continue

        game_not_over = minesweeper.reveal_cell(user_column, user_row)
        if game_not_over == False:
            break
    
    if game_not_over:
        print(visual_line)
        print('CONGRATULATIONS! You just beat Minesweeper!')
        print(minesweeper)
        print(visual_line)
    else:
        print(visual_line)
        print('You hit a bomb! Game over.')
        for i in minesweeper.board:
            for j in i:
                j.set_visibility()
        print(minesweeper)
        
if __name__ == '__main__':
    play()
