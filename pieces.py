# ===================================//
# parent piece classes
# ===================================//

import images as ig


class pieces():

    def __init__(self, colour, moves, position):
        self.rank = ''
        self.colour = colour
        self.moves = moves
        self.position = position
        self.inf = []

    def on_board(self, pos):
        if pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8:
            return True
        else:
            return False

    def mvtCardinal(self, pos, lim):
        n = []
        for i in range(4):
            n.append([])
            for j in range(lim):
                m = [((j + 1), 0), (-(j + 1), 0), (0, (j + 1)), (0, -(j + 1))]
                c = (pos[0] + m[i][0], pos[1] + m[i][1])
                if self.on_board(c):
                    n[i].append(c)
        return n

    def mvtDiagonal(self, pos, lim):
        n = []
        for i in range(4):
            n.append([])
            for j in range(lim):
                m = [((j + 1), (j + 1)), (-(j + 1), (j + 1)), (-(j + 1), -(j + 1)), ((j + 1), -(j + 1))]
                c = (pos[0] + m[i][0], pos[1] + m[i][1])
                if self.on_board(c):
                    n[i].append(c)
        return n

    def mvtKnight(self, pos):
        n = []
        m = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for i in range(len(m)):
            c = (pos[0] + m[i][0], pos[1] + m[i][1])
            if self.on_board(c):
                n.append([c])
        return n

    def mvtPawn(self, pos, moves, colour):
        n = []
        if colour == "white":
            m = [[(-1, 0)]]
            if moves == 0:
                m[0].append((-2, 0))
        else:
            m = [[(1, 0)]]
            if moves == 0:
                m[0].append((2, 0))
        for i in range(len(m)):
            n.append([])
            for j in range(len(m[i])):
                c = (pos[0] + m[i][j][0], pos[1] + m[i][j][1])
                if self.on_board(c):
                    n[i].append(c)
        return n

    def moveList(self, board):
        move_list = []
        for i in range(len(self.inf)):
            for j in range(len(self.inf[i])):
                if i != self.position[0] and j != self.position[1]:
                    if not board[self.inf[i][j][0]][self.inf[i][j][1]][1]:
                        move_list.append(self.inf[i][j])
                    else:
                        if board[self.inf[i][j][0]][self.inf[i][j][1]][1].colour != self.colour:
                            if self.rank != 'pawn':
                                move_list.append(self.inf[i][j])
                        break
        if self.rank == 'pawn':
            unit = None
            if self.colour == 'white' and self.position[0] > 0:
                unit = -1
            elif self.colour == 'black' and self.position[0] < 7:
                unit = 1
            if unit:
                if self.position[1] + 1 < 7:
                    if board[self.position[0] + unit][self.position[1] + 1][1]:
                        if board[self.position[0] + unit][self.position[1] + 1][1].colour != self.colour:
                            move_list.append((self.position[0] + unit, self.position[1] + 1))
                if self.position[1] - 1 > 0:
                    if board[self.position[0] + unit][self.position[1] - 1][1]:
                        if board[self.position[0] + unit][self.position[1] - 1][1].colour != self.colour:
                            move_list.append((self.position[0] + unit, self.position[1] - 1))
        return move_list


# ===================================//
# children of pieces class
# ===================================//


class pawn(pieces):

    def __init__(self, colour, position):
        self.rank = 'pawn'
        self.colour = colour
        self.moves = 0
        self.position = position
        self.inf = []
        self.possible_moves = []
        self.value = 1.5
        self.img = ig.pawn[self.colour]
        self.sf = 30

    def on_select(self, board):
        self.inf = self.mvtPawn(self.position, self.moves, self.colour)
        self.possible_moves = self.moveList(board)

    def en_passant(self):
        return False

    def queening(self):
        return False


class castle(pieces):

    def __init__(self, colour, position):
        self.rank = 'castle'
        self.colour = colour
        self.moves = 0
        self.position = position
        self.move_lim = 8
        self.inf = []
        self.possible_moves = []
        self.value = 5.5
        self.img = ig.castle[self.colour]
        self.sf = 35

    def on_select(self, board):
        self.inf = self.mvtCardinal(self.position, self.move_lim)
        self.possible_moves = self.moveList(board)
        print('inf = ', self.inf)
        print('position = ', self.position)
        print('move_lim = ', self.move_lim)
        print('possible_moves = ', self.possible_moves)


class knight(pieces):

    def __init__(self, colour, position):
        self.rank = 'knight'
        self.colour = colour
        self.moves = 0
        self.position = position
        self.move_lim = 1
        self.inf = []
        self.possible_moves = []
        self.value = 3.5
        self.img = ig.knight[self.colour]
        self.sf = 40

    def on_select(self, board):
        self.inf = self.mvtKnight(self.position)
        self.possible_moves = self.moveList(board)


class bishop(pieces):

    def __init__(self, colour, position):
        self.rank = 'bishop'
        self.colour = colour
        self.moves = 0
        self.position = position
        self.move_lim = 8
        self.inf = []
        self.possible_moves = []
        self.value = 3.5
        self.img = ig.bishop[self.colour]
        self.sf = 40

    def on_select(self, board):
        self.inf = self.mvtDiagonal(self.position, self.move_lim)
        self.possible_moves = self.moveList(board)


class queen(pieces):

    def __init__(self, colour, position):
        self.rank = 'queen'
        self.colour = colour
        self.moves = 0
        self.position = position
        self.move_lim = 8
        self.inf = []
        self.possible_moves = []
        self.value = 9.5
        self.img = ig.queen[self.colour]
        self.sf = 45

    def on_select(self, board):
        self.inf = self.mvtCardinal(self.position, self.move_lim)
        temp = self.mvtDiagonal(self.position, self.move_lim)
        for i in temp:
            self.inf.append(i)
        self.possible_moves = self.moveList(board)


class king(pieces):

    def __init__(self, colour, position):
        self.rank = 'king'
        self.colour = colour
        self.moves = 0
        self.position = position
        self.move_lim = 1
        self.inf = []
        self.possible_moves = []
        self.value = 1
        self.img = ig.king[self.colour]
        self.sf = 50

    def on_select(self, board):
        self.inf = self.mvtCardinal(self.position, self.move_lim)
        temp = self.mvtDiagonal(self.position, self.move_lim)
        for i in temp:
            self.inf.append(i)
        self.possible_moves = self.moveList(board)
