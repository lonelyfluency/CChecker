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
        board_status is a dic that store the pos info of the board, the same as Board.bd_bd_pos_status
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

    def get_act_list(self,board_status):
        pass


class Xiang(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'xiang'

    def get_act_list(self,board_status):
        pass


class Shi(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'shi'

    def get_act_list(self,board_status):
        pass


class King(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'king'

    def get_act_list(self,board_status):
        pass
