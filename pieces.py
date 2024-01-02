# from . import Game
# import Game


class Piece:

    def __init__(self,color,image,startingRow,startingColumn) -> None:
        self.color = color
        self.img = image
        # self.starting_position = None
        self.row = startingRow
        self.column = startingColumn
        self.is_alive = True

    def setScale(self,scale):
        self.img = scale
    
    def setPosition(self,row,col):
        # self.starting_position = startingPosition
        self.row = row
        self.column = col

    def setEaten(self):
        self.is_alive = False


class Pawn(Piece):

    def allowedMoves():
        pass

class Rook(Piece):

    def allowedMoves():
        pass

class Knight(Piece):

    def allowedMoves():
        pass

class Bishop(Piece):

    def allowedMoves():
        pass

class Queen(Piece):

    def allowedMoves():
        pass

class King(Piece):

    def __init__(self, color, image, startingRow, startingColumn) -> None:
        super().__init__(color, image, startingRow, startingColumn)
        self.is_checked = False

    def setCheck(self,check_sit):
        self.is_checked = check_sit

    def allowedMoves():
        pass


    