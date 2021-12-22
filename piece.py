'''
Define different types of chess pieces.
'''

class Piece:
    def __init__(self):
        self.side = 0
        self.value = 0
        self.pos = (0,0)
        self.act_list = []


class Dummy(Piece):
    def __init__(self,pos):
        super().__init__()
        self.pos = pos
        self.name = 'void'



class Bing(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'bing'
        self.value = 1

    def get_act_list(self,board_status):
        '''
        board_status is a dic that store the pos info of the board, the same as Board.bd_pos_status
        '''
        if self.side == 0:
            if self.pos[0] < 5:
                if board_status[(self.pos[0]+1, self.pos[1])] != 1:
                    self.act_list.append((self.pos[0]+1, self.pos[1]))
            else:
                tmp_act_tar_list = []
                tmp_act_tar_choice = []
                if self.pos[0] != 9:
                    tmp_act_tar_choice.append(1)
                if self.pos[1] != 0:
                    tmp_act_tar_choice.append(2)
                if self.pos[1] != 8:
                    tmp_act_tar_choice.append(3)
                for i in tmp_act_tar_choice:
                    if i == 1:
                        tmp_act_tar_list.append((self.pos[0]+1, self.pos[1]))
                    if i == 2:
                        tmp_act_tar_list.append((self.pos[0], self.pos[1]-1))
                    if i == 3:
                        tmp_act_tar_list.append((self.pos[0], self.pos[1]+1))
                for i in tmp_act_tar_list:
                    if board_status[i] != 1:
                        self.act_list.append(i)
        else:
            if self.pos[0] > 4:
                if board_status[(self.pos[0]-1, self.pos[1])] != -1:
                    self.act_list.append((self.pos[0]-1, self.pos[1]))
            else:
                tmp_act_tar_list = []
                tmp_act_tar_choice = []
                if self.pos[0] != 0:
                    tmp_act_tar_choice.append(1)
                if self.pos[1] != 0:
                    tmp_act_tar_choice.append(2)
                if self.pos[1] != 8:
                    tmp_act_tar_choice.append(3)
                for i in tmp_act_tar_choice:
                    if i == 1:
                        tmp_act_tar_list.append((self.pos[0]-1, self.pos[1]))
                    if i == 2:
                        tmp_act_tar_list.append((self.pos[0], self.pos[1]-1))
                    if i == 3:
                        tmp_act_tar_list.append((self.pos[0], self.pos[1]+1))
                for i in tmp_act_tar_list:
                    if board_status[i] != 1:
                        self.act_list.append(i)




class Ju(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'ju'
        self.value = 9

    def get_act_list(self,board_status):
        if self.side == 0:
            up = self.pos[0]+1
            down = self.pos[0]-1
            left = self.pos[1]-1
            right = self.pos[1]+1
            if up<10:
                while board_status[(up,self.pos[1])] != 1:
                    self.act_list.append((up,self.pos[1]))
                    if board_status[(up,self.pos[1])] == -1:
                        break
                    up += 1
                    if up > 9:
                        break
            
            if down>=0:
                while board_status[(down,self.pos[1])] != 1:
                    self.act_list.append((down,self.pos[1]))
                    if board_status[(down,self.pos[1])] == -1:
                        break
                    down -= 1
                    if down < 0:
                        break
            
            if left>=0:
                while board_status[(self.pos[0],left)] != 1:
                    self.act_list.append((self.pos[0],left))
                    if board_status[(self.pos[0],left)] == -1:
                        break
                    left -= 1
                    if left < 0:
                        break

            if right<9:
                while board_status[(self.pos[0],right)] != 1:
                    self.act_list.append((self.pos[0],right))
                    if board_status[(self.pos[0],right)] == -1:
                        break
                    right += 1
                    if right > 8:
                        break
        else:
            up = self.pos[0]+1
            down = self.pos[0]-1
            left = self.pos[1]-1
            right = self.pos[1]+1
            if up<10:
                while board_status[(up,self.pos[1])] != -1:
                    self.act_list.append((up,self.pos[1]))
                    if board_status[(up,self.pos[1])] == 1:
                        break
                    up += 1
                    if up > 9:
                        break
            
            if down>=0:
                while board_status[(down,self.pos[1])] != -1:
                    self.act_list.append((down,self.pos[1]))
                    if board_status[(down,self.pos[1])] == 1:
                        break
                    down -= 1
                    if down < 0:
                        break
            
            if left>=0:
                while board_status[(self.pos[0],left)] != -1:
                    self.act_list.append((self.pos[0],left))
                    if board_status[(self.pos[0],left)] == 1:
                        break
                    left -= 1
                    if left < 0:
                        break

            if right<9:
                while board_status[(self.pos[0],right)] != -1:
                    self.act_list.append((self.pos[0],right))
                    if board_status[(self.pos[0],right)] == 1:
                        break
                    right += 1
                    if right > 8:
                        break


class Pao(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'pao'
        self.value = 5

    def get_act_list(self,board_status):
        up = self.pos[0]+1
        down = self.pos[0]-1
        left = self.pos[1]-1
        right = self.pos[1]+1
        if up<10:
            while board_status[(up,self.pos[1])] == 0:
                self.act_list.append((up,self.pos[1]))
                up += 1
                if up > 9:
                    break
        
        if down>=0:
            while board_status[(down,self.pos[1])] == 0:
                self.act_list.append((down,self.pos[1]))
                down -= 1
                if down < 0:
                    break
        
        if left>=0:
            while board_status[(self.pos[0],left)] == 0:
                self.act_list.append((self.pos[0],left))
                left -= 1
                if left < 0:
                    break

        if right<9:
            while board_status[(self.pos[0],right)] == 0:
                self.act_list.append((self.pos[0],right))
                right += 1
                if right > 8:
                    break
        
        if up < 9 and board_status[(up,self.pos[1])] != 0:
            up += 1
            while board_status[(up,self.pos[1])] == 0:
                up += 1
                if up > 9:
                    break
            if up <=9:
                if self.side == 0 and board_status[(up,self.pos[1])] == -1:
                    self.act_list.append((up,self.pos[1]))
                if self.side == 1 and board_status[(up,self.pos[1])] == 1:
                    self.act_list.append((up,self.pos[1]))
        
        if down >= 1 and board_status[(down,self.pos[1])] != 0:
            down -= 1
            while board_status[(down,self.pos[1])] == 0:
                down -= 1
                if down < 0:
                    break
            if down >= 0:
                if self.side == 0 and board_status[(down,self.pos[1])] == -1:
                    self.act_list.append((down,self.pos[1]))
                if self.side == 1 and board_status[(down,self.pos[1])] == 1:
                    self.act_list.append((down,self.pos[1]))

        if left >= 1 and board_status[(self.pos[0],left)] != 0:
            left -= 1
            while board_status[(self.pos[0],left)] == 0:
                left -= 1
                if left < 0:
                    break
            if left >= 0:
                if self.side == 0 and board_status[(self.pos[0],left)] == -1:
                    self.act_list.append((self.pos[0],left))
                if self.side == 1 and board_status[(self.pos[0],left)] == 1:
                    self.act_list.append((self.pos[0],left))

        if right < 8 and board_status[(self.pos[0],right)] != 0:
            right += 1
            while board_status[(self.pos[0],right)] == 0:
                right += 1
                if right > 8:
                    break
            if right <=8:
                if self.side == 0 and board_status[(self.pos[0],right)] == -1:
                    self.act_list.append((self.pos[0],right))
                if self.side == 1 and board_status[(self.pos[0],right)] == 1:
                    self.act_list.append((self.pos[0],right))

class Ma(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'ma'
        self.value = 5

    def get_act_list(self,board_status):
        tar_indicator_list = []
        try:
            if board_status[(self.pos[0],self.pos[1]+1)] == 0 and self.pos[1]<7:
                tar_indicator_list.append(1)
                tar_indicator_list.append(8)
        except KeyError:
            pass
        try:
            if board_status[(self.pos[0]+1,self.pos[1])] == 0 and self.pos[0]<8:
                tar_indicator_list.append(2)
                tar_indicator_list.append(3)
        except KeyError:
            pass
        try:
            if board_status[(self.pos[0],self.pos[1]-1)] == 0 and self.pos[1]>1:
                tar_indicator_list.append(4)
                tar_indicator_list.append(5)
        except KeyError:
            pass
        try:
            if board_status[(self.pos[0]-1,self.pos[1])] == 0 and self.pos[0]>1:
                tar_indicator_list.append(6)
                tar_indicator_list.append(7)
        except KeyError:
            pass

        for i in tar_indicator_list:
            if i == 1:
                tmp_pos = (self.pos[0]+1,self.pos[1]+2)
            elif i == 2:
                tmp_pos = (self.pos[0]+2,self.pos[1]+1)
            elif i == 3:
                tmp_pos = (self.pos[0]+2,self.pos[1]-1)
            elif i == 4:
                tmp_pos = (self.pos[0]+1,self.pos[1]-2)
            elif i == 5:
                tmp_pos = (self.pos[0]-1,self.pos[1]-2)
            elif i == 6:
                tmp_pos = (self.pos[0]-2,self.pos[1]-1)
            elif i == 7:
                tmp_pos = (self.pos[0]-2,self.pos[1]+1)
            else:
                tmp_pos = (self.pos[0]-1,self.pos[1]+2)
            try:
                if self.side == 0 and board_status[tmp_pos] != 1:
                    self.act_list.append(tmp_pos)
                if self.side == 1 and board_status[tmp_pos] != -1:
                    self.act_list.append(tmp_pos)
            except KeyError:
                pass


class Xiang(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'xiang'
        self.value = 3

    def get_act_list(self,board_status):
        tar_indicator_list = []
        try:
            if board_status[(self.pos[0]+1,self.pos[1]+1)] == 0 and self.pos[1]<7 and self.pos[0]<8:
                tar_indicator_list.append(1)
        except KeyError:
            pass
        try:
            if board_status[(self.pos[0]+1,self.pos[1]-1)] == 0 and self.pos[0]<8 and self.pos[1]>1:
                tar_indicator_list.append(2)
        except KeyError:
            pass
        try:
            if board_status[(self.pos[0]-1,self.pos[1]-1)] == 0 and self.pos[1]>1 and self.pos[0]>1:
                tar_indicator_list.append(3)
        except KeyError:
            pass
        try:
            if board_status[(self.pos[0]-1,self.pos[1]+1)] == 0 and self.pos[0]>1 and self.pos[1]<7:
                tar_indicator_list.append(4)
        except KeyError:
            pass

        for i in tar_indicator_list:
            if i == 1:
                tmp_pos = (self.pos[0]+2,self.pos[1]+2)
            elif i == 2:
                tmp_pos = (self.pos[0]+2,self.pos[1]-2)
            elif i == 3:
                tmp_pos = (self.pos[0]-2,self.pos[1]-2)
            else:
                tmp_pos = (self.pos[0]-2,self.pos[1]+2)
            try:
                if self.side == 0 and board_status[tmp_pos] != 1:
                    self.act_list.append(tmp_pos)
                if self.side == 1 and board_status[tmp_pos] != -1:
                    self.act_list.append(tmp_pos)
            except KeyError:
                pass


class Shi(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'shi'
        self.value = 3

    def get_act_list(self,board_status):
        if self.side == 0:
            posible_pos = [(0,3),(0,5),(1,4),(2,3),(2,5)]
            assert self.pos in posible_pos

            if self.pos == (0,3) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (0,5) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (2,3) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (2,5) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (1,4):
                for i in [(0,3),(0,5),(2,3),(2,5)]:
                    if board_status[i] != 1:
                        self.act_list.append(i)
        else:
            posible_pos = [(9,3),(9,5),(8,4),(7,3),(7,5)]
            assert self.pos in posible_pos

            if self.pos == (9,3) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (9,5) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (7,3) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (7,5) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (8,4):
                for i in [(9,3),(9,5),(7,3),(7,5)]:
                    if board_status[i] != 1:
                        self.act_list.append(i)


class King(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'king'
        self.value = 100

    def get_act_list(self,board_status,piece_status):
        tar_indicator_list = []
        if self.side == 0:
            posible_pos = [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
            assert self.pos in posible_pos

            if self.pos == (0,3) and board_status[(0,4)] != 1:
                self.act_list.append((0,4))
            if self.pos == (0,3) and board_status[(1,3)] != 1:
                self.act_list.append((1,3))
            if self.pos == (0,4) and board_status[(0,3)] != 1:
                self.act_list.append((0,3))
            if self.pos == (0,4) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (0,4) and board_status[(0,5)] != 1:
                self.act_list.append((0,5))
            if self.pos == (0,5) and board_status[(0,4)] != 1:
                self.act_list.append((0,4))
            if self.pos == (0,5) and board_status[(1,5)] != 1:
                self.act_list.append((1,5))
            
            if self.pos == (2,3) and board_status[(2,4)] != 1:
                self.act_list.append((2,4))
            if self.pos == (2,3) and board_status[(1,3)] != 1:
                self.act_list.append((1,3))
            if self.pos == (2,4) and board_status[(2,3)] != 1:
                self.act_list.append((2,3))
            if self.pos == (2,4) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (2,4) and board_status[(2,5)] != 1:
                self.act_list.append((2,5))
            if self.pos == (2,5) and board_status[(2,4)] != 1:
                self.act_list.append((2,4))
            if self.pos == (2,5) and board_status[(1,5)] != 1:
                self.act_list.append((1,5))

            if self.pos == (1,3) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))
            if self.pos == (1,3) and board_status[(2,3)] != 1:
                self.act_list.append((2,3))
            if self.pos == (1,3) and board_status[(0,3)] != 1:
                self.act_list.append((0,3))
            if self.pos == (1,4) and board_status[(1,3)] != 1:
                self.act_list.append((1,3))
            if self.pos == (1,4) and board_status[(1,5)] != 1:
                self.act_list.append((1,5))
            if self.pos == (1,4) and board_status[(0,4)] != 1:
                self.act_list.append((0,4))
            if self.pos == (1,4) and board_status[(2,4)] != 1:
                self.act_list.append((2,4))
            if self.pos == (1,5) and board_status[(0,5)] != 1:
                self.act_list.append((0,5))
            if self.pos == (1,5) and board_status[(2,5)] != 1:
                self.act_list.append((2,5))
            if self.pos == (1,5) and board_status[(1,4)] != 1:
                self.act_list.append((1,4))

            col = self.pos[1]
            for row in range(self.pos[0]+1,10):
                if board_status[(row,col)] != 0:
                    if piece_status[(row,col)].name == 'king':
                        self.act_list.append((row,col))
                    break

        else:
            posible_pos = [(9,3),(9,4),(9,5),(8,3),(8,4),(8,5),(7,3),(7,4),(7,5)]
            assert self.pos in posible_pos

            if self.pos == (9,3) and board_status[(9,4)] != -1:
                self.act_list.append((9,4))
            if self.pos == (9,3) and board_status[(8,3)] != -1:
                self.act_list.append((8,3))
            if self.pos == (9,4) and board_status[(9,3)] != -1:
                self.act_list.append((9,3))
            if self.pos == (9,4) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (9,4) and board_status[(9,5)] != -1:
                self.act_list.append((9,5))
            if self.pos == (9,5) and board_status[(9,4)] != -1:
                self.act_list.append((9,4))
            if self.pos == (9,5) and board_status[(8,5)] != -1:
                self.act_list.append((8,5))
            
            if self.pos == (7,3) and board_status[(7,4)] != -1:
                self.act_list.append((2,4))
            if self.pos == (7,3) and board_status[(8,3)] != -1:
                self.act_list.append((8,3))
            if self.pos == (7,4) and board_status[(7,3)] != -1:
                self.act_list.append((7,3))
            if self.pos == (7,4) and board_status[(7,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (7,4) and board_status[(7,5)] != -1:
                self.act_list.append((7,5))
            if self.pos == (7,5) and board_status[(7,4)] != -1:
                self.act_list.append((7,4))
            if self.pos == (7,5) and board_status[(8,5)] != -1:
                self.act_list.append((8,5))

            if self.pos == (8,3) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))
            if self.pos == (8,3) and board_status[(7,3)] != -1:
                self.act_list.append((7,3))
            if self.pos == (8,3) and board_status[(9,3)] != -1:
                self.act_list.append((9,3))
            if self.pos == (8,4) and board_status[(8,3)] != -1:
                self.act_list.append((8,3))
            if self.pos == (8,4) and board_status[(8,5)] != -1:
                self.act_list.append((8,5))
            if self.pos == (8,4) and board_status[(9,4)] != -1:
                self.act_list.append((9,4))
            if self.pos == (8,4) and board_status[(7,4)] != -1:
                self.act_list.append((7,4))
            if self.pos == (8,5) and board_status[(9,5)] != -1:
                self.act_list.append((9,5))
            if self.pos == (8,5) and board_status[(7,5)] != -1:
                self.act_list.append((7,5))
            if self.pos == (8,5) and board_status[(8,4)] != -1:
                self.act_list.append((8,4))

            col = self.pos[1]
            for row in range(self.pos[0]-1,-1,-1):
                if board_status[(row,col)] != 0:
                    if piece_status[(row,col)].name == 'king':
                        self.act_list.append((row,col))
                    break