# File: Cell.py
# Author: Didzis Zvaigzne
# Description: Cell class for Minesweeper game

class Cell():
    # Initialize each cell with invisible cell that is NOT a bomb
    def __init__(self, is_visible=False, is_mine=False):
        self.is_visible = is_visible
        self.is_mine = is_mine
        self.value = 0

    def get_mine(self):
        return self.is_mine

    def set_mine(self):
        self.is_mine = True

    def get_visibility(self):
        return self.is_visible

    def set_visibility(self):
        self.is_visible = True

    def __str__(self):
        return format(self.get_mine)