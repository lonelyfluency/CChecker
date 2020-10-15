import numpy as np
import matplotlib.pyplot as plt

class Board:
    def __init__(self):
        self.bd = {}
        for i in range(10):
            for j in range(9):
                self.bd[(i,j)] = 0
    

    def draw(self):
        plt.grid()
        plt.show()


if __name__ == "__main__":
    cboard = Board()
    cboard.draw()