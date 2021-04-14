# File: Board.py
# Author: Didzis Zvaigzne
# Description: Board class for Minesweeper game
# Board Class includes Cell class

from Cell import Cell
import random

class Board():
    def __init__(self, board_size, bomb_size):
        self.board_size = board_size  # Assign board size
        self.bomb_size = bomb_size  # Assign the number of bombs
        self.free_spots = board_size * board_size - bomb_size
        self.board = self.create_the_board()  # Create the Minesweeper board
        self.pass_values_to_cells()  # Assign values to each Cell class
        self.revealed_squares = set()  # For later use {(row, col)}

    def create_the_board(self):
        # Each bomb/empty cell is determined by Cell class
        board = [[Cell() for _ in range(self.board_size)]
                 for _ in range(self.board_size)]

        # Initiate the bomb counter
        bombs_on_board = 0

        while bombs_on_board < self.bomb_size:
            location = random.randint(0, self.board_size ** 2 - 1)
            row = location // self.board_size  # For example: 80 // 10 = 8 - 8th row
            col = location % self.board_size  # For example: 80 % 10 = 0 - 0th column

            # If the board already has a bomb at that specific location, try again
            if board[row][col].value == '*':
                continue

            # Assign the bomb to a specific row/column
            board[row][col].value = '*'
            # Cell class' is_mine is set to True
            board[row][col].set_mine()
            bombs_on_board += 1
        return board

    def pass_values_to_cells(self):
        for row in range(self.board_size):
            for column in range(self.board_size):
                # If the cell contains a bomb continue
                if self.board[row][column].value == '*':
                    continue

                # Count how many bombs the cell has around it and assign a value to the number of bombs
                self.board[row][column].value = self.get_adjacent_bombs(
                    row, column)

    def get_adjacent_bombs(self, row, column):
        adjacent_bombs = 0
        # Max to not go under 0, min to not  go board_size + 1 or over
        for r in range(max(0, row - 1), min(self.board_size - 1, row + 1) + 1):
            for c in range(max(0, column - 1), min(self.board_size - 1, column + 1) + 1):
                # If r and c are the same as the location that we are checking, continue
                if r == row and c == column:
                    continue

                if self.board[r][c].value == '*':
                    adjacent_bombs += 1
        return adjacent_bombs

    def reveal_cell(self, row, column):
        self.board[row][column].set_visibility()
        self.revealed_squares.add((row, column))

        if self.board[row][column].value == '*':
            return False
        elif self.board[row][column].value > 0:
            return True
        
        # If the value is 0, the revealed square has no bombs next to it
        for r in range(max(0, row - 1), min(self.board_size - 1, row + 1) + 1):
            for c in range(max(0, column - 1), min(self.board_size - 1, column + 1) + 1):
                if (r, c) in self.revealed_squares:
                    continue 
                self.reveal_cell(r, c)
        
        return True

    def __str__(self):
        # Self string displays the current Minesweeper board situation
        display_board = " "
        splitter = "\n---"

        for i in range(0, self.board_size):
            display_board += " | " + str(i)
            splitter += "----"
        splitter += "\n"

        display_board += splitter

        for y in range(0, self.board_size):
            display_board += str(y)
            for x in range(0, self.board_size):
                if self.board[x][y].get_mine() and self.board[x][y].get_visibility():
                    display_board += " | " + str(self.board[x][y].value)
                elif self.board[x][y].get_visibility():
                    display_board += " | " + str(self.board[x][y].value)
                else:
                    display_board += " |  "
            display_board += " |  "
            display_board += splitter
        return display_board