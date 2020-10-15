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

    def get_act_list(self,board_status):
        '''
        board_status is a dic that store the pos info of the board, the same as Board.bd_status
        '''
        pass


class Ju(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'ju'

    def get_act_list(self,board_status):
        pass


class Pao(Piece):
    def __init__(self,side,pos):
        super().__init__()
        self.side = side
        self.pos = pos
        self.name = 'pao'

    def get_act_list(self,board_status):
        pass


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