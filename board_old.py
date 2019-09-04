# ===================================//
# board class
# ===================================//

import engine as ce
import pieces as pc


class board:

    def __init__(self):
        self.white = 'white'
        self.black = 'black'
        self.turn = self.white
        self.board = []
        self.ref = {}
        self.counter = 0
        index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for y in range(8):
            self.board.append([])
            for x in range(8):
                self.board[y].append([index[x] + str(7 - y + 1), None])
                self.ref[index[x] + str(7 - y + 1)] = (y, x)
        self.unit_dict = {self.black: {'pawn': '♙', 'castle': '♖', 'knight': '♘', 'bishop': '♗', 'king': '♔', 'queen': '♕'},
                          self.white: {'pawn': '♟', 'castle': '♜', 'knight': '♞', 'bishop': '♝', 'king': '♚', 'queen': '♛'}}
        self.engine = ce.chess_engine()
        self.p = input('white (w), black (b), or none (n)? ')
        if self.p == 'w':
            self.player = self.white
            self.opposition = self.black
        elif self.p == 'b':
            self.player = self.black
            self.opposition = self.white
        else:
            self.player = None
            self.opposition = None

    def board_UI(self):
        self.ui = []
        for y in range(8):
            self.ui.append([])
            for x in range(8):
                if self.board[y][x][1] is None:
                    self.ui[y].append([' '])
                else:
                    self.ui[y].append([self.unit_dict[self.board[y][x][1].colour][self.board[y][x][1].rank]])

    def setup(self):
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

    def refresh_board(self):
        for m in self.board:
            for n in m:
                if n[1]:
                    n[1].on_select(self.board)

    def turn_end(self):
        print(self.ui)
        if self.turn == self.white:
            self.turn = self.black
        else:
            self.turn = self.white

    def checkmate(self, colour):
        if colour == 'white':
            ml_ref = 0
        elif colour == 'black':
            ml_ref = 1
        copy_ui = self.ui
        for i in self.engine.move_lib[ml_ref]:
            for j in i:
                copy_ui[j[0]][j[1]] = ['@']
        #print(self.engine.move_lib[ml_ref])
        #print(copy_ui)
        print('done')
        # for i in self.board[y][x][1].possible_moves:
        #     if copy_ui[i[0]][i[1]] == [' ']:
        #         copy_ui[i[0]][i[1]] = ['@']
        return False

    def next_move(self, turn):
        self.counter += 1
        print('move', self.counter, '- ' + turn + ' to move:')
        self.refresh_board()
        self.engine.move_library(self.board)
        if self.checkmate(turn):
            return True
        if self.turn != self.player:
            ca = self.engine.random_move(self.board, self.turn)
            cmd = ca[0]
        else:
            cmd = input('select a square, or type quit: ')
        if cmd == 'quit':
            return True
        else:
            try:
                y = self.ref[cmd][0]
                x = self.ref[cmd][1]
            except KeyError:
                print("grid reference not recognised")
                return False
            if self.board[y][x][1] and self.board[y][x][1].colour == turn:
                copy_ui = self.ui
                for i in self.board[y][x][1].possible_moves:
                    if copy_ui[i[0]][i[1]] == [' ']:
                        copy_ui[i[0]][i[1]] = ['@']
                if self.turn != self.player:
                    move = ca[1]
                else:
                    print(copy_ui)
                    move = input('move ' + self.board[y][x][1].colour + ' ' + self.board[y][x][1].rank + ' ' + self.board[y][x][0] + ' to: ')
                try:
                    if self.ref[move] not in self.board[y][x][1].possible_moves:
                        print('move not allowed')
                        return False
                    else:
                        for i in range(8):
                            for j in range(8):
                                if self.board[i][j][0] == move:
                                    self.board[i][j][1] = self.board[y][x][1]
                                    self.board[y][x][1] = None
                                    self.board[i][j][1].moves += 1
                                    self.board[i][j][1].position = self.ref[move]
                                    self.board[i][j][1].inf = []
                except KeyError:
                    print("grid reference not recognised")
                    return False
            else:
                print('no piece or wrong colour piece selected')
                return False
        self.board_UI()
        self.turn_end()
        return(False)
