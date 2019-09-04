# ===================================//
# board class
# ===================================//

'''
creates a new board

'''

import tkinter as tk
import time
import pieces as pc
import engine
import rulesets


class board:
    def __init__(self, canvas, width, height, framerate):
        self.CANVAS = canvas
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.board = []
        self.ref = {}
        self.white, self.black = 'white', 'black'
        self.turn = self.white
        self.unit_dict = {self.white: {'pawn': '♙', 'castle': '♖', 'knight': '♘', 'bishop': '♗', 'king': '♔', 'queen': '♕'},
                          self.black: {'pawn': '♟', 'castle': '♜', 'knight': '♞', 'bishop': '♝', 'king': '♚', 'queen': '♛'}}
        self.engine = engine.chess_engine()
        self.fill = 'white'
        self.draw_board()
        self.draw_sidebar()
        self.board_setup()
        self.board_ui()

    def draw_board(self):
        base_length = (self.HEIGHT - 40) / 8
        index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for y in range(8):
            self.board.append([])
            self.fill = 'white' if self.fill == 'grey' else 'grey'
            for x in range(8):
                self.board[y].append([index[x] + str(7 - y + 1), None])
                self.ref[index[x] + str(7 - y + 1)] = (y, x)
                self.fill = 'white' if self.fill == 'grey' else 'grey'
                bottom_left = ((base_length * (y + 1)) + 20 , (base_length * x) + 20)
                top_right = ((base_length * y) + 20, (base_length * (x + 1)) + 20)
                self.CANVAS.create_rectangle(bottom_left + top_right, width=1, tag=index[x] + str(7 - y + 1), fill=self.fill)
        
    def draw_sidebar(self):
        text = 'The following moves have been played:'
        self.CANVAS.create_text((self.HEIGHT + 90, 40), tag='text', text=text, width=self.WIDTH - self.HEIGHT)

    def board_setup(self):
        for x in range(8):
            if x in (0, 7):
                self.board[0][x][1] = pc.castle(self.black, (0, x))
                self.board[7][x][1] = pc.castle(self.white, (7, x))
            if x in (1, 6):
                self.board[0][x][1] = pc.knight(self.black, (0, x))
                self.board[7][x][1] = pc.knight(self.white, (7, x))
            if x in (2, 5):
                self.board[0][x][1] = pc.bishop(self.black, (0, x))
                self.board[7][x][1] = pc.bishop(self.white, (7, x))
            if x == 3:
                self.board[0][x][1] = pc.queen(self.black, (0, x))
                self.board[7][x][1] = pc.queen(self.white, (7, x))
            if x == 4:
                self.board[0][x][1] = pc.king(self.black, (0, x))
                self.board[7][x][1] = pc.king(self.white, (7, x))
            for y in (2, 3, 4, 5):
                self.board[y][x][1] = None
            self.board[1][x][1] = pc.pawn(self.black, (1, x))
            self.board[6][x][1] = pc.pawn(self.white, (6, x))

    def test_setup(self):
        for x in range(8):
            for y in range(8):
                self.board[x][y][1] = None
        self.board[2][4][1] = pc.king(self.black, (2, 4))
        self.board[6][4][1] = pc.castle(self.white, (6, 4))
        self.board[6][1][1] = pc.bishop(self.white, (6, 1))
        self.board[3][3][1] = pc.pawn(self.white, (3, 3))

    def board_ui(self):
        self.ui = []
        base_length = (self.HEIGHT - 40) / 8
        for y in range(8):
            self.ui.append([])
            for x in range(8):
                bottom_left = ((base_length * (x + 1)) + 20 , (base_length * y) + 20)
                if self.board[y][x][1] is None:
                    self.ui[y].append([' '])
                else:
                    self.ui[y].append([self.unit_dict[self.board[y][x][1].colour][self.board[y][x][1].rank]])
                    self.CANVAS.create_text((bottom_left[0] - 35, bottom_left[1] + 35), font=20,
                        text=self.unit_dict[self.board[y][x][1].colour][self.board[y][x][1].rank], width=1)

    def update_frames(self, is_quit):
        time.sleep(self.FRAMERATE)
        if is_quit:
            self.CANVAS.quit()
        else:
            self.CANVAS.update()
