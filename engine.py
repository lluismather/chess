# ===================================//
# engine class
# ===================================//
import random


class chess_engine:

    def __init__(self):
        # self.board_weights = [[3, 2, 3, 4, 4, 3, 2, 3],
        #                       [2, 2, 3, 5, 5, 3, 2, 2], [1, 2, 4, 6, 6, 4, 2, 1],
        #                       [1, 3, 5, 7, 7, 5, 3, 1], [1, 3, 5, 7, 7, 5, 3, 1],
        #                       [2, 2, 3, 4, 4, 3, 2, 2], [2, 2, 1, 1, 1, 1, 2, 2],
        #                       [3, 2, 2, 1, 1, 2, 2, 3]]
        # self.opponent_weights = [[3,2,2,1,1,2,2,3],[2,2,1,1,1,1,2,2],[2,2,3,4,4,3,2,2],[1,3,5,7,7,5,3,1],
        # [1,3,5,7,7,5,3,1],[1,2,4,6,6,4,2,1],[2,2,3,5,5,3,2,2],[3,2,3,4,4,3,2,3]]
        self.move_lib = []
        # self.opp_move_lib = []
        # self.move_lib_new = []
        # self.opp_move_lib_new = []

    def move_library(self, board):
        move_array = [[], []]
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x][1]:
                    if board[y][x][1].colour == 'white':
                        ma_ref = 0
                    elif board[y][x][1].colour == 'black':
                        ma_ref = 1
                    for i in board[y][x][1].possible_moves:
                        move_array[ma_ref].append([board[y][x][1].position, i])
        self.move_lib = move_array

    def random_move(self, board, colour):
        if colour == 'white':
            ml_ref = 0
        elif colour == 'black':
            ml_ref = 1
        if len(self.move_lib[ml_ref]) > 0:
            move_lib_temp = self.move_lib[ml_ref]
            a = move_lib_temp[random.randint(0, len(move_lib_temp) - 1)]
            return(board[a[0][0]][a[0][1]][0], board[a[1][0]][a[1][1]][0])
        else:
            print('no moves available for ' + colour + ', game over')
            quit()

    # def iterate_moves(self, board, colour):
    #     move_extent = []
    #     self.move_lib_new = self.generate_move_lib(board, colour, False)
    #     for i in self.move_lib_new:
    #         print(i)
    #         board_dummy = board
    #         board_dummy[i[1][0]][i[1][1]][1] = board_dummy[i[0][0]][i[0][1]][1]
    #         board_dummy[i[0][0]][i[0][1]][1] = None
    #         print(self.generate_score(board_dummy, board.opponent, self.board_weights))
    #         move_extent.append([i, None])
    #     print(move_extent)

    # def weighted_move(self, board, colour):
    #     self.move_lib = self.generate_move_lib(board, colour, False)
    #     self.opp_move_lib = self.generate_move_lib(board, board.player, True)
    #     move_weights = []
    #     for i in range(len(self.move_lib)):
    #         if board[self.move_lib[i][1][0]][self.move_lib[i][1][1]][1] and board[self.move_lib[i][1][0]][self.move_lib[i][1][1]][1].colour != colour:
    #             w = board[self.move_lib[i][1][0]][self.move_lib[i][1][1]][1].value*self.board_weights[self.move_lib[i][1][0]][self.move_lib[i][1][1]]
    #         else:
    #             w = self.board_weights[self.move_lib[i][1][0]][self.move_lib[i][1][1]]
    #         if self.infl_check(self.move_lib[i],self.opp_move_lib) and not self.infl_check(self.move_lib[i],self.move_lib):
    #             w = w / 2
    #         move_weights.append(w)
    #     lw_len = len([i for i in range(0,len(move_weights)) if move_weights[i]==max(move_weights)])
    #     if lw_len > 1:
    #         a = self.move_lib[[i for i in range(0,len(move_weights)) if move_weights[i]==max(move_weights)][random.randint(0,lw_len-1)]]
    #     else:
    #         a = self.move_lib[move_weights.index(max(move_weights))]
    #     move = board[a[0][0]][a[0][1]][0], board[a[1][0]][a[1][1]][0]
    #     print(move[0], 'to', move[1])
    #     scores = [self.generate_score(board, board.opponent, self.board_weights), self.generate_score(board, board.player, self.opponent_weights)]
    #     print('scores: ', scores)
    #     return(move)

    # def generate_move_lib(self, board, colour, add_pawns):
    #     ml = []
    #     for y in range(len(board)):
    #         for x in range(len(board[y])):
    #             if board[y][x][1] and board[y][x][1].colour == colour:
    #                 for i in board[y][x][1].possible_moves:
    #                     ml.append([board[y][x][1].position, i])
    #     if add_pawns:
    #         for y in range(len(board)):
    #             for x in range(len(board[y])):
    #                 if board[y][x][1] and board[y][x][1].colour == colour and board[y][x][1].rank == 'pawn':
    #                     if colour == board.player:
    #                         ml.append([(board[y][x][1].position),(board[y][x][1].position[0]-1,board[y][x][1].position[1]-1)])
    #                         ml.append([(board[y][x][1].position),(board[y][x][1].position[0]-1,board[y][x][1].position[1]+1)])
    #                         try:
    #                             ml.remove([(board[y][x][1].position),(board[y][x][1].position[0]-1,board[y][x][1].position[1])])
    #                         except ValueError:
    #                             pass
    #                     else:
    #                         ml.append([(board[y][x][1].position),(board[y][x][1].position[0]+1,board[y][x][1].position[1]-1)])
    #                         ml.append([(board[y][x][1].position),(board[y][x][1].position[0]+1,board[y][x][1].position[1]+1)])
    #                         try:
    #                             ml.remove([(board[y][x][1].position),(board[y][x][1].position[0]+1,board[y][x][1].position[1])])
    #                         except ValueError:
    #                             pass
    #     return(ml)

    # def generate_score(self, board, colour, weights):
    #     score = 0
    #     for y in range(len(board)):
    #         for x in range(len(board[y])):
    #             if board[y][x][1] and board[y][x][1].colour == colour:
    #                 score += (board[y][x][1].value * weights[y][x])
    #     return(score)

    # def infl_check(self, xy, move_list):
    #     for move in move_list:
    #         if xy != move:
    #             if xy[1] == move[1]:
    #                 return(True)
    #     return(False)
