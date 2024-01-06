# from . #import # #import # from .import check_piece_on_box
alive_pieces = []
turn = 'White'

def check_piece_on_box(row,col):
    for piece in alive_pieces:
        if piece.row == row and piece.column == col :
            return piece
    return None

def cause_check(pieceee,consider_destination):


    temp_piece_holder = []
    dest_piece_in_cord = check_piece_on_box(consider_destination[0],consider_destination[1])
    if dest_piece_in_cord is not None:
        # if dest_piece_in_cord.color != pieceee.color:
        # if dest_piece_in_cord is not pieceee:
        temp_piece_holder.append(dest_piece_in_cord)
        alive_pieces.remove(dest_piece_in_cord)
    
    origin_row = pieceee.row
    origin_column = pieceee.column


    # alive_pieces.remove(pieceee)
    pieceee.row = consider_destination[0]
    pieceee.column = consider_destination[1]
    # alive_pieces.append(pieceee)

    

    #check for check conidtion
    for checking_piece in alive_pieces:
        if checking_piece.color != turn:
            for loc in checking_piece.allowedMoves():
                dest_piece = check_piece_on_box(loc[0],loc[1])

                if dest_piece is not None:
                    #                                      dest_piece.color == turn
                       if dest_piece.__str__()=='King' and dest_piece.color != checking_piece.color :
                        # dest_piece.setCheck(True)
                        pieceee.row = origin_row
                        pieceee.column = origin_column
                        # print('not allowed to move!')
                        alive_pieces.extend(temp_piece_holder)
                        return True
    pieceee.row = origin_row
    pieceee.column = origin_column
    alive_pieces.extend(temp_piece_holder)
    return False

class Piece:

    def __init__(self,color,image,startingRow,startingColumn) -> None:
        self.color = color
        self.img = image
        # self.starting_position = None
        self.row = startingRow
        self.column = startingColumn
        self.is_selected = False

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
        # self.has_moved = False
        self.move_count = 0

    def allowedMoves(self,filter=False):
        
        allowed_locs = []

        all_locs_in_pattern = []
        crash_locs = []

        if self.color == 'White':

            crash_locs.append([self.row - 1, self.column - 1])
            crash_locs.append([self.row - 1, self.column + 1])

            if self.move_count==0 :
                all_locs_in_pattern.append([self.row - 1, self.column])
                all_locs_in_pattern.append([self.row - 2, self.column])
            else:
                all_locs_in_pattern.append([self.row - 1, self.column])
                
                
            # for loc in all_locs_in_pattern:

            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = check_piece_on_box(loc[0],loc[1])
            #         if des_piece is None :
            #             allowed_locs.append(loc)

            # for loc in crash_locs:
            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = check_piece_on_box(loc[0],loc[1])
            #         if des_piece is not None and des_piece.color != self.color:
            #             allowed_locs.append(loc)
            #             alive_pieces.remove(des_piece)
            #             eaten_pieces.append(des_piece)

        else:
            
            crash_locs.append([self.row + 1, self.column - 1])
            crash_locs.append([self.row + 1, self.column + 1])

            if self.move_count==0 :
                all_locs_in_pattern.append([self.row + 1, self.column])
                all_locs_in_pattern.append([self.row + 2, self.column])
            else:
                all_locs_in_pattern.append([self.row + 1, self.column])
                
                
            # for loc in all_locs_in_pattern:

            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = check_piece_on_box(loc[0],loc[1])
            #         if des_piece is None :
            #             allowed_locs.append(loc)

            # for loc in crash_locs:
            #     if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
            #         des_piece = check_piece_on_box(loc[0],loc[1])
            #         if des_piece is not None and des_piece.color != self.color:
            #             allowed_locs.append(loc)





        for loc in all_locs_in_pattern:

            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = check_piece_on_box(loc[0],loc[1])
                if des_piece is None :
                    allowed_locs.append(loc)

        for loc in crash_locs:
            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = check_piece_on_box(loc[0],loc[1])
                if des_piece is not None and des_piece.color != self.color:
                    allowed_locs.append(loc)
                    # alive_pieces.remove(des_piece)
                    # eaten_pieces.append(des_piece)

        # return allowed_locs
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Pawn'

class Rook(Piece):

    def __init__(self, color, image, startingRow, startingColumn,type='None') -> None:
        super().__init__(color, image, startingRow, startingColumn)
        self.move_count = 0
        self.type = type

    def allowedMoves(self,filter=False):

        #import 
        allowed_locs = []

        piece_row = self.row
        piece_col = self.column
        #move up
        flag = True
        while flag:
            piece_row-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = check_piece_on_box(piece_row,piece_col)

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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                if not cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Rook'

class Knight(Piece):

    def allowedMoves(self,filter=False):

        #import 
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
                des_piece = check_piece_on_box(loc[0],loc[1])
                if des_piece is None or des_piece.color != self.color:
                    allowed_locs.append(loc)

        # return allowed_locs
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Knight'

class Bishop(Piece):

    def allowedMoves(self,filter=False):

        #import 
        allowed_locs = []

        piece_row = self.row
        piece_col = self.column

        #moving up and left
        flag = True
        while flag:
            piece_row-=1
            piece_col-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                if not cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            return mod_allowed_locs
        else:
            return allowed_locs

    def __str__(self) -> str:
        return 'Bishop'

class Queen(Piece):

    def allowedMoves(self,filter=False):

        #import 
        allowed_locs = []

        piece_row = self.row
        piece_col = self.column
        #move up
        flag = True
        while flag:
            piece_row-=1
            if piece_row>=0 and piece_row<8 and piece_col>=0 and piece_col<8:
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
                des_piece = check_piece_on_box(piece_row,piece_col)
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
            # if not cause_check(self,allowed_locs[0]):
            #     return allowed_locs
            # else:
            #     return []
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not cause_check(self,check_loc):
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
        self.move_count = 0

    def setCheck(self,check_sit):
        self.is_checked = check_sit

    def allowedMoves(self,filter=False):

        #import 
        allowed_locs = []
        all_locs_in_pattern = []

        all_locs_in_pattern.append([self.row - 1, self.column - 1])
        all_locs_in_pattern.append([self.row - 1, self.column - 0])
        all_locs_in_pattern.append([self.row - 1, self.column + 1])
        all_locs_in_pattern.append([self.row - 0, self.column - 1])
        # all_locs_in_pattern.append([self.row - 0, self.column + 0])
        all_locs_in_pattern.append([self.row - 0, self.column + 1])
        all_locs_in_pattern.append([self.row + 1, self.column - 1])
        all_locs_in_pattern.append([self.row + 1, self.column - 0])
        all_locs_in_pattern.append([self.row + 1, self.column + 1])

        # if self.castling_condition('Right'):
        #     all_locs_in_pattern.append([7,6])
        # if self.castling_condition('Left'):
        #     all_locs_in_pattern.append([7,2])
        
        
        for loc in all_locs_in_pattern:

            if loc[0]>=0 and loc[0]<8 and loc[1]>=0 and loc[1]<8:
                des_piece = check_piece_on_box(loc[0],loc[1])
                if des_piece is None or des_piece.color != self.color:
                    allowed_locs.append(loc)

        # return allowed_locs
                    
        if filter:
           
            mod_allowed_locs = []
            for check_loc in allowed_locs:
                if not cause_check(self,check_loc):
                   
                    mod_allowed_locs.append(check_loc)
            
            if self.color=='White':
                if self.castling_condition('Right'):
                    mod_allowed_locs.append([7,6])
                if self.castling_condition('Left'):
                    mod_allowed_locs.append([7,2])
            else:
                if self.castling_condition('Right'):
                    mod_allowed_locs.append([0,6])
                if self.castling_condition('Left'):
                    mod_allowed_locs.append([0,2])


            return mod_allowed_locs
        else:
            return allowed_locs
        
    def castling_condition(self,mode):
        if mode == 'Right':
            if self.color == 'White':
                rook_loc = check_piece_on_box(7,5)
                king_loc = check_piece_on_box(7,6)
                if rook_loc is None and king_loc is None:
                    if not cause_check(self,[7,5]) and not cause_check(self,[7,6]):
                        for piece in alive_pieces:
                            if piece.color == self.color and piece.__str__()=='Rook' and piece.type=='Right':
                                WR_Rook:Rook = piece
                                break
                        if self.move_count==0 and WR_Rook.move_count==0 and not self.is_checked:
                            return True
                return False
            else:
                rook_loc = check_piece_on_box(0,5)
                king_loc = check_piece_on_box(0,6)
                if rook_loc is None and king_loc is None:
                    if not cause_check(self,[0,5]) and not cause_check(self,[0,6]):
                        for piece in alive_pieces:
                            if piece.color == self.color and piece.__str__()=='Rook' and piece.type=='Right':
                                BR_Rook:Rook = piece
                                break
                        if self.move_count==0 and BR_Rook.move_count==0 and not self.is_checked:
                            return True
                return False
        elif mode == 'Left':
            if self.color == 'White':
                rook_loc = check_piece_on_box(7,3)
                king_loc = check_piece_on_box(7,2)
                if rook_loc is None and king_loc is None:
                    if not cause_check(self,[7,3]) and not cause_check(self,[7,2]):
                        for piece in alive_pieces:
                            if piece.color == self.color and piece.__str__()=='Rook' and piece.type=='Left':
                                WL_Rook:Rook = piece
                                break
                        if self.move_count==0 and WL_Rook.move_count==0 and not self.is_checked:
                            return True
                return False
            else:
                rook_loc = check_piece_on_box(0,3)
                king_loc = check_piece_on_box(0,2)
                if rook_loc is None and king_loc is None:
                    if not cause_check(self,[0,3]) and not cause_check(self,[0,2]):
                        for piece in alive_pieces:
                            if piece.color == self.color and piece.__str__()=='Rook' and piece.type=='Left':
                                BL_Rook:Rook = piece
                                break
                        if self.move_count==0 and BL_Rook.move_count==0 and not self.is_checked:
                            return True
                return False


    def __str__(self) -> str:
        return 'King'


    