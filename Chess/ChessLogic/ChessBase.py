#!/usr/bin/python3

class Game(object):
    def __init__(self, start_string=None, past_moves=None, game_info=None):
        self.start_string   = start_string
        self.past_moves     = past_moves
        self.game_info      = game_info

    @staticmethod
    def piece_factory(chp):
        dt = {'k': King, 'q': Queen, 'b': Bishop, 'n': Knight, 'r': Rook, 'p': Pawn}
        if chp.lower() in dt:
            return dt[chp.lower()]('white' if chp.islower() else 'black')
        else:
            raise ValueError("'chp' needs to be char: 'k', 'q', 'n', 'r', or 'p' (or equivalent uppercase).")

#------------------GAME-------------------------------#
class Board(object):
    default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    def __init__(self, board_string=None, board_array=None):
        if   board_array:   self.board_array = board_array
        elif board_string:  self.board_array = self.arr_from(board_string)
        else:               self.board_array = self.arr_from(self.default)

    @classmethod
    def arr_from(cls, from_string):
        new_arr = []
        for i in from_string.split("/"):
            new_arr.append([])
            for j in i:
                if j.isdigit(): new_arr[-1] += [None] * int(j)
                else:           new_arr[-1] += [Game.piece_factory(j)]
        return new_arr

    @classmethod
    def string_from(cls, board_arr):
        pass

    def __str__(self):
        return "\n".join(["".join([str(x) if x else '_' for x in y]) for y in self.board_array ][::-1])

    #def board_from_arr

#------------------ABSTRACT---------------------------#

class Piece(object):
    valid_colors = ['white', 'black']
    rep='_'

    def __init__(self, color):
        if color not in self.valid_colors:
            raise ValueError("Color must be an element within '" + self.__class__.__name__ + ".valid_colors'")
        else:
            self.color = color

    def __repr__(self):
        return self.rep if self.color == 'white' else self.rep.upper()

    def __str__(self):
        return self.__repr__()


        #self.piece_char = piece_char

#------------------PIECES-----------------------------#

class King(Piece):
    rep='k'

class Queen(Piece):
    rep='q'

class Bishop(Piece):
    rep='b'

class Knight(Piece):
    rep='n'

class Rook(Piece):
    rep='r'

class Pawn(Piece):
    rep='p'


#------------------QUICK-TESTING----------------------#
if __name__ == "__main__":
    a = Board()
    #print(a.board_array)
    print(str(a))
