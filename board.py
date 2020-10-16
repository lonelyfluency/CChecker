import numpy as np
import matplotlib.pyplot as plt
from piece import *

class Board:
    def __init__(self):
        '''
        bd_pos_status stores whether there is a piece in pos (x,y), player 0 gets 1, player 1 gets -1, no piece gets 0.
        bd_piece_statue stores the piece type in pos (x,y). The types can be found in piece.py
        '''
        self.bd_pos_status = {}
        self.bd_piece_status = {}
        for i in range(10):
            for j in range(9):
                self.bd_pos_status[(i,j)] = 0
                self.bd_piece_status[(i,j)] = Dummy((i,j))

    def add_piece(self,piece):
        self.bd_pos_status[piece.pos] = 1 if piece.side ==0 else -1
        self.bd_piece_status[piece.pos] = piece 

    def draw(self):
        ax = plt.gca()
        ax.set_xlim(0,8)
        ax.set_ylim(0,9)
        miloc = plt.MultipleLocator(1)
        ax.xaxis.set_minor_locator(miloc)
        ax.yaxis.set_minor_locator(miloc)
        ax.grid(axis = 'x',which='major')
        ax.grid(axis = 'y',which='major')
        plt.show()


if __name__ == "__main__":
    cboard = Board()
    cboard.draw()
    ju = Ju(0,(0,0))
    bing = Bing(0,(3,0))
    pao = Pao(1,(8,0))
    cboard.add_piece(ju)
    cboard.add_piece(bing)
    cboard.add_piece(pao)
    ju.get_act_list(cboard.bd_pos_status)
    print(ju.act_list)
    bing.get_act_list(cboard.bd_pos_status)
    print(bing.act_list)
    pao.get_act_list(cboard.bd_pos_status)
    print(pao.act_list)