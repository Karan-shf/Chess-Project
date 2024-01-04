# from . import Game
# import Game
# from .Game import check_piece_on_box


# def check_piece_on_box(row,col):
#     for piece in alive_pieces:
#         if piece.row == row and piece.column == col :
#             return piece
#     return None

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

    def __init__(self, color, image, startingRow, startingColumn) -> None:
        super().__init__(color, image, startingRow, startingColumn)
        self.has_moved = False

    def allowedMoves(self,filter=False):

        import Game
        
        allowed_locs = []

        all_locs_in_pattern = []
        crash_locs = []

        if self.color == 'White':

            crash_locs.append([self.row - 1, self.column - 1])
            crash_locs.append([self.row - 1, self.column + 1])

            if not self.has_moved :
                all_locs_in_pattern.append([self.row - 1, self.column])
                all_locs_in_pattern.append([self.row - 2, self.column])
            else:
                all_locs_in_pattern.append([self.row - 1, self.column])
                
                
            # for loc in all_locs_in_pattern:

            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = Game.check_piece_on_box(loc[0],loc[1])
            #         if des_piece is None :
            #             allowed_locs.append(loc)

            # for loc in crash_locs:
            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = Game.check_piece_on_box(loc[0],loc[1])
            #         if des_piece is not None and des_piece.color != self.color:
            #             allowed_locs.append(loc)
            #             Game.alive_pieces.remove(des_piece)
            #             Game.eaten_pieces.append(des_piece)

        else:
            
            crash_locs.append([self.row + 1, self.column - 1])
            crash_locs.append([self.row + 1, self.column + 1])

            if not self.has_moved :
                all_locs_in_pattern.append([self.row + 1, self.column])
                all_locs_in_pattern.append([self.row + 2, self.column])
            else:
                all_locs_in_pattern.append([self.row + 1, self.column])
                
                
            # for loc in all_locs_in_pattern:

            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = Game.check_piece_on_box(loc[0],loc[1])
            #         if des_piece is None :
            #             allowed_locs.append(loc)

            # for loc in crash_locs:
            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = Game.check_piece_on_box(loc[0],loc[1])
            #         if des_piece is not None and des_piece.color != self.color:
            #             allowed_locs.append(loc)





        for loc in all_locs_in_pattern:

            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = Game.check_piece_on_box(loc[0],loc[1])
                if des_piece is None :
                    allowed_locs.append(loc)

        for loc in crash_locs:
            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = Game.check_piece_on_box(loc[0],loc[1])
                if des_piece is not None and des_piece.color != self.color:
                    allowed_locs.append(loc)
                    # Game.alive_pieces.remove(des_piece)
                    # Game.eaten_pieces.append(des_piece)

        # return allowed_locs
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not Game.cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Pawn'

class Rook(Piece):

    def allowedMoves(self,filter=False):

        import Game

        allowed_locs = []

        piece_row = self.row
        piece_col = self.column
        #move up
        flag = True
        while flag:
            piece_row-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)

                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False

            else:
                flag = False

        piece_row = self.row
        piece_col = self.column
        #move down
        flag = True
        while flag:
            piece_row+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column
        #move right
        flag = True
        while flag:
            piece_col+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column
        #move left
        flag = True
        while flag:
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        # return allowed_locs
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not Game.cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Rook'

class Knight(Piece):

    def allowedMoves(self,filter=False):

        import Game

        allowed_locs = []
        all_locs_in_pattern = []

        all_locs_in_pattern.append([self.row + 1, self.column + 2])
        all_locs_in_pattern.append([self.row + 1, self.column - 2])
        all_locs_in_pattern.append([self.row - 1, self.column + 2])
        all_locs_in_pattern.append([self.row - 1, self.column - 2])
        all_locs_in_pattern.append([self.row + 2, self.column + 1])
        all_locs_in_pattern.append([self.row + 2, self.column - 1])
        all_locs_in_pattern.append([self.row - 2, self.column + 1])
        all_locs_in_pattern.append([self.row - 2, self.column - 1])
        
        for loc in all_locs_in_pattern:

            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = Game.check_piece_on_box(loc[0],loc[1])
                if des_piece is None or des_piece.color != self.color:
                    allowed_locs.append(loc)

        # return allowed_locs
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not Game.cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Knight'

class Bishop(Piece):

    def allowedMoves(self,filter=False):

        import Game

        allowed_locs = []

        piece_row = self.row
        piece_col = self.column

        #moving up and left
        flag = True
        while flag:
            piece_row-=1
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving up and right
        flag = True
        while flag:
            piece_row-=1
            piece_col+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving down and left
        flag = True
        while flag:
            piece_row+=1
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving down and right
        flag = True
        while flag:
            piece_row+=1
            piece_col+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        # return allowed_locs
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not Game.cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Bishop'

class Queen(Piece):

    def allowedMoves(self,filter=False):

        import Game

        allowed_locs = []

        piece_row = self.row
        piece_col = self.column
        #move up
        flag = True
        while flag:
            piece_row-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column
        #move down
        flag = True
        while flag:
            piece_row+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column
        #move right
        flag = True
        while flag:
            piece_col+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column
        #move left
        flag = True
        while flag:
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving up and left
        flag = True
        while flag:
            piece_row-=1
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving up and right
        flag = True
        while flag:
            piece_row-=1
            piece_col+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving down and left
        flag = True
        while flag:
            piece_row+=1
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        piece_row = self.row
        piece_col = self.column

        #moving down and right
        flag = True
        while flag:
            piece_row+=1
            piece_col+=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = Game.check_piece_on_box(piece_row,piece_col)
                # if des_piece is None or des_piece.color != self.color:
                #     allowed_locs.append([piece_row,piece_col])
                # else:
                #     flag = False
                if des_piece is None:
                    # if des_piece.color != self.color
                    allowed_locs.append([piece_row,piece_col])
                elif des_piece.color != self.color:
                    allowed_locs.append([piece_row,piece_col])
                    flag = False
                else:
                    flag = False
            else:
                flag = False

        if filter:
            # if not Game.cause_check(self,allowed_locs[0]):
            #     return allowed_locs
            # else:
            #     return []
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not Game.cause_check(self,check_loc):
                    # allowed_locs.remove(check_loc)
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs


    def __str__(self) -> str:
        return 'Queen'

class King(Piece):

    def __init__(self, color, image, startingRow, startingColumn) -> None:
        super().__init__(color, image, startingRow, startingColumn)
        self.is_checked = False

    def setCheck(self,check_sit):
        self.is_checked = check_sit

    def allowedMoves(self,filter=False):

        import Game

        allowed_locs = []
        all_locs_in_pattern = []

        all_locs_in_pattern.append([self.row - 1, self.column - 1])
        all_locs_in_pattern.append([self.row - 1, self.column - 0])
        all_locs_in_pattern.append([self.row - 1, self.column + 1])
        all_locs_in_pattern.append([self.row - 0, self.column - 1])
        all_locs_in_pattern.append([self.row - 0, self.column + 0])
        all_locs_in_pattern.append([self.row - 0, self.column + 1])
        all_locs_in_pattern.append([self.row + 1, self.column - 1])
        all_locs_in_pattern.append([self.row + 1, self.column - 0])
        all_locs_in_pattern.append([self.row + 1, self.column + 1])
        
        for loc in all_locs_in_pattern:

            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = Game.check_piece_on_box(loc[0],loc[1])
                if des_piece is None or des_piece.color != self.color:
                    allowed_locs.append(loc)

        # return allowed_locs
                    
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not Game.cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'King'


    