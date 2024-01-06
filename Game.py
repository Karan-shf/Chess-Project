import pieces
import pygame
import sys
import time

class Stack:

    def __init__(self,max) -> None:
        self.top = -1
        self.max = max
        self.properties = []
        for i in range(max):
            self.properties.append(None)

    def push(self,value):
        
        if self.isFull():
            raise Exception('Stack is Full')
        else:
            self.top += 1
            self.properties[self.top] = value
            
    def pop(self):

        if self.isEmpty():
            raise Exception('Stack is Empty')
        else:
            index = self.top
            self.top -=1
            return self.properties[index]

    def isFull(self):

        if self.max-1 == self.top:
            return True
        else:
            return False
        
    def isEmpty(self):

        if self.top==-1:
            return True
        else:
            return False
        
    def printProperties(self):
        
        for i in range(self.top,-1,-1):
            print(self.properties[i])

    def clear(self):
        self.properties.clear()
        for i in range(self.max):
            self.properties.append(None)
        self.top = -1

    def count(self):
        return self.top + 1

class Queue:

    def __init__(self,max) -> None:

        self.rear = -1
        self.front = -1
        self.max = max
        self.properties = []
        for i in range(max):
            self.properties.append(None)

    def add(self,value):

        if self.isFull():
            raise Exception('Queue is Full')
        else:
            self.rear +=1
            self.properties[self.rear]=value

    def dequeue(self):

        if self.isEmpty():
            raise Exception('Queue is Empty')
        else:
            self.front+=1
            return self.properties[self.front]

    def isFull(self):

        if self.max-1 == self.rear:
            return True
        else:
            return False
        
    def isEmpty(self):

        if self.front==self.rear:
            return True
        else:
            return False
        
    def printProperties(self):

        for i in range(self.front+1,self.rear+1):
            print(self.properties[i])

class Move:

    def __init__(self,color,piece,origin_loc,destination,eaten_piece,pawn_promotion=False,castling=False,en_passant=False) -> None:
        self.color = color
        self.piece = piece
        self.origin_loc = origin_loc
        self.destination = destination
        self.eaten_piece = eaten_piece
        self.pawn_promotion = pawn_promotion
        self.castling = castling
        self.en_passant = en_passant

def initialize_pieces():

    WL_rook = pieces.Rook('White',pygame.image.load('imgs/White_Rook.png'),7,0,'Left')
    WL_rook.setScale(pygame.transform.scale(WL_rook.img,(50,50)))
    # WL_rook.setStartingPosition(WL_rook.img.get_rect())
    # WL_rook.starting_position.topleft = (250,500)
    pieces.alive_pieces.append(WL_rook)

    WR_rook = pieces.Rook('White',pygame.image.load('imgs/White_Rook.png'),7,7,'Right')
    WR_rook.setScale(pygame.transform.scale(WR_rook.img,(50,50)))
    # WR_rook.setStartingPosition(WR_rook.img.get_rect())
    # WR_rook.starting_position.topleft = (700,500)
    pieces.alive_pieces.append(WR_rook)

    WL_knight = pieces.Knight('White',pygame.image.load('imgs/White_Knight.png'),7,1)
    WL_knight.setScale(pygame.transform.scale(WL_knight.img,(50,50)))
    # WL_knight.setStartingPosition(WL_knight.img.get_rect())
    # WL_knight.starting_position.topleft = (320,500)
    pieces.alive_pieces.append(WL_knight)

    WR_knight = pieces.Knight('White',pygame.image.load('imgs/White_Knight.png'),7,6)
    WR_knight.setScale(pygame.transform.scale(WR_knight.img,(50,50)))
    # WR_knight.setStartingPosition(WR_knight.img.get_rect())
    # WR_knight.starting_position.topleft = (630,500)
    pieces.alive_pieces.append(WR_knight)
   
    WL_bishop = pieces.Bishop('White',pygame.image.load('imgs/White_Bishop.png'),7,2)
    WL_bishop.setScale(pygame.transform.scale(WL_bishop.img,(50,50)))
    # WL_bishop.setStartingPosition(WL_bishop.img.get_rect())
    # WL_bishop.starting_position.topleft = (380,500)
    pieces.alive_pieces.append(WL_bishop)

    WR_bishop = pieces.Bishop('White',pygame.image.load('imgs/White_Bishop.png'),7,5)
    WR_bishop.setScale(pygame.transform.scale(WR_bishop.img,(50,50)))
    # WR_bishop.setStartingPosition(WR_bishop.img.get_rect())
    # WR_bishop.starting_position.topleft = (570,500)
    pieces.alive_pieces.append(WR_bishop)

#fmerklgelkrngeklnrgklenlgkenrgneklrg
    W_Queen = pieces.Queen('White',pygame.image.load('imgs/White_Queen.png'),7,3)
    W_Queen.setScale(pygame.transform.scale(W_Queen.img,(50,50)))
    # W_Queen.setStartingPosition(W_Queen.img.get_rect())
    # W_Queen.starting_position.topleft = (440,500)
    pieces.alive_pieces.append(W_Queen)

#ngkgnelkrngelknglekngeklnrg
    W_King = pieces.King('White',pygame.image.load('imgs/White_King.png'),7,4)
    W_King.setScale(pygame.transform.scale(W_King.img,(50,50)))
    # W_King.setStartingPosition(W_King.img.get_rect())
    # W_King.starting_position.topleft = (510,500)
    pieces.alive_pieces.append(W_King)

    W_Pawn1 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,0)
    W_Pawn1.setScale(pygame.transform.scale(W_Pawn1.img,(50,50)))
    # W_Pawn1.setStartingPosition(W_Pawn1.img.get_rect())
    # W_Pawn1.starting_position.topleft = (250,430)
    pieces.alive_pieces.append(W_Pawn1)

    W_Pawn2 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,1)
    W_Pawn2.setScale(pygame.transform.scale(W_Pawn2.img,(50,50)))
    # W_Pawn2.setStartingPosition(W_Pawn2.img.get_rect())
    # W_Pawn2.starting_position.topleft = (320,430)
    pieces.alive_pieces.append(W_Pawn2)

    W_Pawn3 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,2)
    W_Pawn3.setScale(pygame.transform.scale(W_Pawn3.img,(50,50)))
    # W_Pawn3.setStartingPosition(W_Pawn3.img.get_rect())
    # W_Pawn3.starting_position.topleft = (380,430)
    pieces.alive_pieces.append(W_Pawn3)

    W_Pawn4 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,3)
    W_Pawn4.setScale(pygame.transform.scale(W_Pawn4.img,(50,50)))
    # W_Pawn4.setStartingPosition(W_Pawn4.img.get_rect())
    # W_Pawn4.starting_position.topleft = (440,430)
    pieces.alive_pieces.append(W_Pawn4)

    W_Pawn5 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,4)
    W_Pawn5.setScale(pygame.transform.scale(W_Pawn5.img,(50,50)))
    # W_Pawn5.setStartingPosition(W_Pawn5.img.get_rect())
    # W_Pawn5.starting_position.topleft = (510,430)
    pieces.alive_pieces.append(W_Pawn5)

    W_Pawn6 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,5)
    W_Pawn6.setScale(pygame.transform.scale(W_Pawn6.img,(50,50)))
    # W_Pawn6.setStartingPosition(W_Pawn6.img.get_rect())
    # W_Pawn6.starting_position.topleft = (570,430)
    pieces.alive_pieces.append(W_Pawn6)

    W_Pawn7 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,6)
    W_Pawn7.setScale(pygame.transform.scale(W_Pawn7.img,(50,50)))
    # W_Pawn7.setStartingPosition(W_Pawn7.img.get_rect())
    # W_Pawn7.starting_position.topleft = (630,430)
    pieces.alive_pieces.append(W_Pawn7)

    W_Pawn8 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,7)
    W_Pawn8.setScale(pygame.transform.scale(W_Pawn8.img,(50,50)))
    # W_Pawn8.setStartingPosition(W_Pawn8.img.get_rect())
    # W_Pawn8.starting_position.topleft = (700,430)
    pieces.alive_pieces.append(W_Pawn8)




    BL_rook = pieces.Rook('Black',pygame.image.load('imgs/Black_Rook.png'),0,0,'Left')
    BL_rook.setScale(pygame.transform.scale(BL_rook.img,(50,50)))
    pieces.alive_pieces.append(BL_rook)

    BR_rook = pieces.Rook('Black',pygame.image.load('imgs/Black_Rook.png'),0,7,'Right')
    BR_rook.setScale(pygame.transform.scale(BR_rook.img,(50,50)))
    pieces.alive_pieces.append(BR_rook)

    BL_knight = pieces.Knight('Black',pygame.image.load('imgs/Black_Knight.png'),0,1)
    BL_knight.setScale(pygame.transform.scale(BL_knight.img,(50,50)))
    pieces.alive_pieces.append(BL_knight)

    BR_knight = pieces.Knight('Black',pygame.image.load('imgs/Black_Knight.png'),0,6)
    BR_knight.setScale(pygame.transform.scale(BR_knight.img,(50,50)))
    pieces.alive_pieces.append(BR_knight)
   
    BL_bishop = pieces.Bishop('Black',pygame.image.load('imgs/Black_Bishop.png'),0,2)
    BL_bishop.setScale(pygame.transform.scale(BL_bishop.img,(50,50)))
    pieces.alive_pieces.append(BL_bishop)

    BR_bishop = pieces.Bishop('Black',pygame.image.load('imgs/Black_Bishop.png'),0,5)
    BR_bishop.setScale(pygame.transform.scale(BR_bishop.img,(50,50)))
    pieces.alive_pieces.append(BR_bishop)

    B_Queen = pieces.Queen('Black',pygame.image.load('imgs/Black_Queen.png'),0,3)
    B_Queen.setScale(pygame.transform.scale(B_Queen.img,(50,50)))
    pieces.alive_pieces.append(B_Queen)

    B_King = pieces.King('Black',pygame.image.load('imgs/Black_King.png'),0,4)
    B_King.setScale(pygame.transform.scale(B_King.img,(50,50)))
    pieces.alive_pieces.append(B_King)

    B_Pawn1 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,0)
    B_Pawn1.setScale(pygame.transform.scale(B_Pawn1.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn1)

    B_Pawn2 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,1)
    B_Pawn2.setScale(pygame.transform.scale(B_Pawn2.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn2)

    B_Pawn3 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,2)
    B_Pawn3.setScale(pygame.transform.scale(B_Pawn3.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn3)

    B_Pawn4 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,3)
    B_Pawn4.setScale(pygame.transform.scale(B_Pawn4.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn4)

    B_Pawn5 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,4)
    B_Pawn5.setScale(pygame.transform.scale(B_Pawn5.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn5)

    B_Pawn6 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,5)
    B_Pawn6.setScale(pygame.transform.scale(B_Pawn6.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn6)

    B_Pawn7 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,6)
    B_Pawn7.setScale(pygame.transform.scale(B_Pawn7.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn7)

    B_Pawn8 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,7)
    B_Pawn8.setScale(pygame.transform.scale(B_Pawn8.img,(50,50)))
    pieces.alive_pieces.append(B_Pawn8)

def draw_pieces():
    for piece in pieces.alive_pieces:
        game_screen.blit(piece.img,cal_screen_position(piece.row,piece.column))
    
def cal_board_index(mouseX,mouseY):
    row = (mouseY - BOARD_UPPER_LENGTH) // BOX_LENGTH
    col = (mouseX - BOARD_SIDE_LENGTH) // BOX_LENGTH
    return [row,col]

def cal_screen_position(row,col):
    # pieceX = (col * BOX_LENGTH) + BOARD_SIDE_LENGTH
    # pieceY = (row * BOX_LENGTH) + BOARD_UPPER_LENGTH

    pieceX = (col * BOX_LENGTH) + BOARD_SIDE_LENGTH + (BOX_LENGTH // 7)
    pieceY = (row * BOX_LENGTH) + BOARD_UPPER_LENGTH + (BOX_LENGTH // 7)
    return (pieceX,pieceY)

# def check_piece_on_box(row,col):
#     for piece in pieces.alive_pieces:
#         if piece.row == row and piece.column == col :
#             return piece
#     return None

def change_turn():
    # global pieces.turn
    if pieces.turn == 'White':
        pieces.turn = 'Black'
    else:
        pieces.turn = 'White'

def draw_allowedMoves(piece):
    
    i=0
    for box in piece.allowedMoves(True):

        cord = cal_screen_position(box[0],box[1])

        b_color = 200 - i
        b_color = max(b_color, 0)

        pygame.draw.circle(game_screen,(34,67,b_color),[cord[0]+BOX_LENGTH//3,cord[1]+BOX_LENGTH//3],BOX_LENGTH//4)
        pygame.display.flip()
        i+=10

def move_piece(piece):

    piece_seleceted = True

    # print(piece.allowedMoves(True))

    # pygame.display.flip()
    piece_cord = cal_screen_position(piece.row,piece.column)
    pygame.draw.rect(game_screen,'red',[piece_cord[0]-9,piece_cord[1]-10,BOX_LENGTH,BOX_LENGTH],2)
    pygame.display.flip()

    while piece_seleceted:
        # game_screen.fill('dark gray',[15,345,180,100])
        check_timer()
        # pygame.display.flip()
        # pygame.display.update([15,345,180,100])

        draw_allowedMoves(piece)

        for event2 in pygame.event.get():

            if event2.type==pygame.QUIT:
                global game_boolean
                game_boolean = False
                piece_seleceted = False
                break

            if event2.type == pygame.MOUSEBUTTONDOWN:
                mouseX2 = pygame.mouse.get_pos()[0]
                mouseY2 = pygame.mouse.get_pos()[1]

                cordinate2 = cal_board_index(mouseX2,mouseY2)

                if cordinate2 in piece.allowedMoves(True):

                    des_piece = pieces.check_piece_on_box(cordinate2[0],cordinate2[1])

                    move = Move(piece.color,piece,[piece.row,piece.column],cordinate2,des_piece)
                    game_moves.add(move)
                    game_moves_stack.push(move)
                    game_moves_temp_stack.clear()

                    if des_piece is not None:
                        pieces.alive_pieces.remove(des_piece)
                        eaten_pieces.append(des_piece)
                    piece.setPosition(cordinate2[0],cordinate2[1])
                    check_castling(move)
                    global t0
                    t0 = time.time()
                    if piece.__str__() == 'Pawn':
                        # if not piece.has_moved:
                        #     piece.has_moved = True
                        piece.move_count += 1

                        if piece.color == 'White':
                            if piece.row == 0:
                                pawn_promotion(piece)
                        else:
                            if piece.row == 7:
                                pawn_promotion(piece)

                    if piece.__str__() == 'Rook' or piece.__str__() == 'King':
                        piece.move_count += 1

                    for pie in pieces.alive_pieces :
                        if pie.__str__()=='King' and pie.color==pieces.turn:
                            if pie.is_checked:
                                pie.setCheck(False)
                                print('not check anymore')
                            break


                    change_turn()

                    check_bool = check_condition()
                    CheckMate_condition()
                    update_gameLog(['normal move',check_bool])

                piece_seleceted = False

# def cause_check(pieceee,consider_destination):


#     temp_piece_holder = []
#     dest_piece_in_cord = pieces.check_piece_on_box(consider_destination[0],consider_destination[1])
#     if dest_piece_in_cord is not None:
#         # if dest_piece_in_cord.color != pieceee.color:
#         # if dest_piece_in_cord is not pieceee:
#         temp_piece_holder.append(dest_piece_in_cord)
#         pieces.alive_pieces.remove(dest_piece_in_cord)
    
#     origin_row = pieceee.row
#     origin_column = pieceee.column


#     # pieces.alive_pieces.remove(pieceee)
#     pieceee.row = consider_destination[0]
#     pieceee.column = consider_destination[1]
#     # pieces.alive_pieces.append(pieceee)

    

#     #check for check conidtion
#     for checking_piece in pieces.alive_pieces:
#         if checking_piece.color != pieces.turn:
#             for loc in checking_piece.allowedMoves():
#                 dest_piece = pieces.check_piece_on_box(loc[0],loc[1])

#                 if dest_piece is not None:
#                     #                                      dest_piece.color == pieces.turn
#                        if dest_piece.__str__()=='King' and dest_piece.color != checking_piece.color :
#                         # dest_piece.setCheck(True)
#                         pieceee.row = origin_row
#                         pieceee.column = origin_column
#                         print('not allowed to move!')
#                         pieces.alive_pieces.extend(temp_piece_holder)
#                         return True
#     pieceee.row = origin_row
#     pieceee.column = origin_column
#     pieces.alive_pieces.extend(temp_piece_holder)
#     return False

def check_condition():

    for piece in pieces.alive_pieces:

        # if pieces.turn != piece.color:
        for loc in piece.allowedMoves():

            dest_piece = pieces.check_piece_on_box(loc[0],loc[1])

            if dest_piece is not None:
                if dest_piece.__str__()=='King' and dest_piece.color != piece.color :
                    dest_piece.setCheck(True)
                    print('CHECK!!!!!!!')
                    return True
                
    return False

def check_Undo(mouseX , mouseY):
    
    # problem: if soldier undos into first move it should be able to move 2 rooms again
    # solution: replace "bool has_moved" with "int move_count"

    # problem: eaten piece have to come back to life
    # solution: add an eaten_piece variable to Move class

    if mouseX >=50 and mouseX <=150 and mouseY>=50 and mouseY<=150:
        print('UNDO')
        try:
            move:Move = game_moves_stack.pop()
            game_moves_temp_stack.push(move)

            global t0
            t0 = time.time()

            if move.pawn_promotion:
                enemy_eaten_piece , promoted_pawn = move.eaten_piece
                promoted_pawn.setPosition(move.origin_loc[0],move.origin_loc[1])
                promoted_pawn.move_count -= 1
                pieces.alive_pieces.remove(move.piece)
                pieces.alive_pieces.append(promoted_pawn)
                if enemy_eaten_piece is not None:
                    pieces.alive_pieces.append(enemy_eaten_piece)
                    eaten_pieces.remove(enemy_eaten_piece)
                # move.piece = promoted_pawn
            elif move.castling:
                rook_origin_loc = {
                    1 : [7,7],
                    2 : [7,0],
                    3 : [0,7],
                    4 : [0,0]
                }
                moven_king , moven_rook , castling_type = move.piece
                moven_king.setPosition(move.origin_loc[0],move.origin_loc[1])
                moven_king.move_count -= 1
                rook_origin_row , rook_origin_col = rook_origin_loc[castling_type]
                moven_rook.setPosition(rook_origin_row , rook_origin_col)
            elif move.en_passant:
                pass
            else:
                move.piece.setPosition(move.origin_loc[0],move.origin_loc[1])
                if move.piece.__str__() == 'Pawn' or move.piece.__str__() == 'Rook' or move.piece.__str__() == 'King':
                    move.piece.move_count -= 1
                if move.eaten_piece is not None:
                    eaten_pieces.remove(move.eaten_piece)
                    pieces.alive_pieces.append(move.eaten_piece)
            change_turn()
            update_gameLog(['undo',move])
        except:
            print('no moves has been made!')

def check_Redo(mouseX , mouseY):

    if mouseX >=50 and mouseX <=150 and mouseY>=200 and mouseY<=300:
        print('REDO')
        try:
            move:Move = game_moves_temp_stack.pop()
            game_moves_stack.push(move)

            global t0
            t0 = time.time()

            if move.pawn_promotion:
                # enemy_eaten_piece , promoted_pawn = move.eaten_piece
                # promoted_pawn.setPosition(move.origin_loc[0],move.origin_loc[1])
                # promoted_pawn.move_count -= 1
                # pieces.alive_pieces.remove(move.piece)
                # pieces.alive_pieces.append(promoted_pawn)
                # if enemy_eaten_piece is not None:
                #     pieces.alive_pieces.append(enemy_eaten_piece)
                #     eaten_pieces.remove(enemy_eaten_piece)
                # move.piece = promoted_pawn
                enemy_eaten_piece , promoted_pawn = move.eaten_piece
                promoted_pawn.setPosition(move.destination[0],move.destination[1])
                promoted_pawn.move_count += 1
                pieces.alive_pieces.remove(promoted_pawn)
                pieces.alive_pieces.append(move.piece)
                if enemy_eaten_piece is not None:
                    pieces.alive_pieces.remove(enemy_eaten_piece)
                    eaten_pieces.append(enemy_eaten_piece)

            elif move.castling:
                # rook_origin_loc = {
                #     1 : [7,7],
                #     2 : [7,0],
                #     3 : [0,7],
                #     4 : [0,0]
                # }
                # moven_king , moven_rook , castling_type = move.piece
                # moven_king.setPosition(move.origin_loc[0],move.origin_loc[1])
                # moven_king.move_count -= 1
                # rook_origin_row , rook_origin_col = rook_origin_loc[castling_type]
                # moven_rook.setPosition(rook_origin_row , rook_origin_col)
                rook_dest_dict = {
                    1 : [7,5],
                    2 : [7,3],
                    3 : [0,5],
                    4 : [0,3],
                }
                moven_king , moven_rook , castling_type = move.piece
                moven_king.setPosition(move.destination[0],move.destination[1])
                moven_king.move_count += 1
                rook_dest_row , rook_dest_col = rook_dest_dict[castling_type]
                moven_rook.setPosition(rook_dest_row , rook_dest_col)
            elif move.en_passant:
                pass
            else:
                move.piece.setPosition(move.destination[0],move.destination[1])
                if move.piece.__str__() == 'Pawn':
                    move.piece.move_count += 1
                if move.eaten_piece is not None:
                    pieces.alive_pieces.remove(move.eaten_piece)
                    eaten_pieces.append(move.eaten_piece)
            change_turn()
            update_gameLog(['redo',move])
        except:
            print('no moves to redo')

def draw_eaten_pieces():

    game_screen.blit(font_small.render('White eaten pieces',True,'black'),(805,10))

    # pygame.draw.rect(game_screen,'black',[810,40,50,50])
    # pygame.draw.rect(game_screen,'black',[870,40,50,50])
    # pygame.draw.rect(game_screen,'black',[930,40,50,50])

    # pygame.draw.rect(game_screen,'black',[810,100,50,50])
    # pygame.draw.rect(game_screen,'black',[870,100,50,50])
    # pygame.draw.rect(game_screen,'black',[930,100,50,50])

    # pygame.draw.rect(game_screen,'black',[810,160,50,50])
    # pygame.draw.rect(game_screen,'black',[870,160,50,50])
    # pygame.draw.rect(game_screen,'black',[930,160,50,50])

    # pygame.draw.rect(game_screen,'black',[810,220,50,50])
    # pygame.draw.rect(game_screen,'black',[870,220,50,50])
    # pygame.draw.rect(game_screen,'black',[930,220,50,50])

    # pygame.draw.rect(game_screen,'black',[810,280,50,50])
    # pygame.draw.rect(game_screen,'black',[870,280,50,50])
    # pygame.draw.rect(game_screen,'black',[930,280,50,50])

    game_screen.blit(font_small.render('Black eaten pieces',True,'black'),(805,350))

    # pygame.draw.rect(game_screen,'white',[810,380,50,50])
    # pygame.draw.rect(game_screen,'white',[870,380,50,50])
    # pygame.draw.rect(game_screen,'white',[930,380,50,50])

    # pygame.draw.rect(game_screen,'white',[810,440,50,50])
    # pygame.draw.rect(game_screen,'white',[870,440,50,50])
    # pygame.draw.rect(game_screen,'white',[930,440,50,50])

    # pygame.draw.rect(game_screen,'white',[810,500,50,50])
    # pygame.draw.rect(game_screen,'white',[870,500,50,50])
    # pygame.draw.rect(game_screen,'white',[930,500,50,50])

    # pygame.draw.rect(game_screen,'white',[810,560,50,50])
    # pygame.draw.rect(game_screen,'white',[870,560,50,50])
    # pygame.draw.rect(game_screen,'white',[930,560,50,50])

    # pygame.draw.rect(game_screen,'white',[810,620,50,50])
    # pygame.draw.rect(game_screen,'white',[870,620,50,50])
    # pygame.draw.rect(game_screen,'white',[930,620,50,50])

    white_grave = [
        (810,40),
        (870,40),
        (930,40),
        (810,100),
        (870,100),
        (930,100),
        (810,160),
        (870,160),
        (930,160),
        (810,220),
        (870,220),
        (930,220),
        (810,280),
        (870,280),
        (930,280)
    ]

    black_grave = [
        (810,380),
        (870,380),
        (930,380),
        (810,440),
        (870,440),
        (930,440),
        (810,500),
        (870,500),
        (930,500),
        (810,560),
        (870,560),
        (930,560),
        (810,620),
        (870,620),
        (930,620)
    ]

    i = 0
    j = 0

    for piece in eaten_pieces:
        if piece.color == 'White':
            game_screen.blit(piece.img,white_grave[i])
            i+=1
        else:
            game_screen.blit(piece.img,black_grave[j])
            j+=1

def update_gameLog(content):

    moves_dictionary = {
        tuple([0, 0]) : 'a8',
        tuple([1, 0]) : 'a7',
        tuple([2, 0]) : 'a6',
        tuple([3, 0]) : 'a5',
        tuple([4, 0]) : 'a4',
        tuple([5, 0]) : 'a3',
        tuple([6, 0]) : 'a2',
        tuple([7, 0]) : 'a1',
        tuple([0, 1]) : 'b8',
        tuple([1, 1]) : 'b7',
        tuple([2, 1]) : 'b6',
        tuple([3, 1]) : 'b5',
        tuple([4, 1]) : 'b4',
        tuple([5, 1]) : 'b3',
        tuple([6, 1]) : 'b2',
        tuple([7, 1]) : 'b1',
        tuple([0, 2]) : 'c8',
        tuple([1, 2]) : 'c7',
        tuple([2, 2]) : 'c6',
        tuple([3, 2]) : 'c5',
        tuple([4, 2]) : 'c4',
        tuple([5, 2]) : 'c3',
        tuple([6, 2]) : 'c2',
        tuple([7, 2]) : 'c1',
        tuple([0, 3]) : 'd8',
        tuple([1, 3]) : 'd7',
        tuple([2, 3]) : 'd6',
        tuple([3, 3]) : 'd5',
        tuple([4, 3]) : 'd4',
        tuple([5, 3]) : 'd3',
        tuple([6, 3]) : 'd2',
        tuple([7, 3]) : 'd1',
        tuple([0, 4]) : 'e8',
        tuple([1, 4]) : 'e7',
        tuple([2, 4]) : 'e6',
        tuple([3, 4]) : 'e5',
        tuple([4, 4]) : 'e4',
        tuple([5, 4]) : 'e3',
        tuple([6, 4]) : 'e2',
        tuple([7, 4]) : 'e1',
        tuple([0, 5]) : 'f8',
        tuple([1, 5]) : 'f7',
        tuple([2, 5]) : 'f6',
        tuple([3, 5]) : 'f5',
        tuple([4, 5]) : 'f4',
        tuple([5, 5]) : 'f3',
        tuple([6, 5]) : 'f2',
        tuple([7, 5]) : 'f1',
        tuple([0, 6]) : 'g8',
        tuple([1, 6]) : 'g7',
        tuple([2, 6]) : 'g6',
        tuple([3, 6]) : 'g5',
        tuple([4, 6]) : 'g4',
        tuple([5, 6]) : 'g3',
        tuple([6, 6]) : 'g2',
        tuple([7, 6]) : 'g1',
        tuple([0, 7]) : 'h8',
        tuple([1, 7]) : 'h7',
        tuple([2, 7]) : 'h6',
        tuple([3, 7]) : 'h5',
        tuple([4, 7]) : 'h4',
        tuple([5, 7]) : 'h3',
        tuple([6, 7]) : 'h2',
        tuple([7, 7]) : 'h1'
    }

    mode , context = content


    file = open('GameLog.txt','at')

    if mode=='normal move':

        last_move = game_moves_stack.properties[game_moves_stack.top]

        if last_move.pawn_promotion:

            check_bool = context
            
            # last_move = game_moves_stack.properties[game_moves_stack.top]

            sep = False

            if last_move.eaten_piece[0] is not None:
                crash = ' Crash'
                sep = True
            else:
                crash = ''

            if check_bool:
                check = ' Check'
                sep = True
            else:
                check = ''

            if game_boolean:
                check_mate = ''
            else:
                if winner=='Draw':
                    check_mate = ' Draw'
                else:
                    check_mate = ' Check Mate'
                    check = ''
                sep = True

            if sep:
                seperator = '-'
            else:
                seperator = ''

            file.write(f'{last_move.color} {last_move.eaten_piece[1].__str__()} to {moves_dictionary[tuple(last_move.destination)]} promoted to {last_move.piece.__str__()} {seperator}{crash}{check}{check_mate}\n')
        elif last_move.castling:
            castling_type = last_move.piece[2]
            if castling_type == 1 or castling_type == 3:
                castling = 'O-O'
            else:
                castling = 'O-O-O'

            file.write(f'{last_move.piece[0].color} King Castling {castling}\n')
        elif last_move.en_passant:
            pass
        else:
            check_bool = context
            
            # last_move = game_moves_stack.properties[game_moves_stack.top]

            sep = False

            if last_move.eaten_piece is not None:
                crash = ' Crash'
                sep = True
            else:
                crash = ''

            if check_bool:
                check = ' Check'
                sep = True
            else:
                check = ''

            if game_boolean:
                check_mate = ''
            else:
                if winner=='Draw':
                    check_mate = ' Draw'
                else:
                    check_mate = ' Check Mate'
                    check = ''
                sep = True

            if sep:
                seperator = '-'
            else:
                seperator = ''

            file.write(f'{last_move.color} {last_move.piece.__str__()} to {moves_dictionary[tuple(last_move.destination)]} {seperator}{crash}{check}{check_mate}\n')

    elif mode == 'undo':
        move = context
        if move.pawn_promotion:
            file.write(f'--Undo {move.piece.color} {move.piece.__str__()} depromoted to {move.eaten_piece[1].__str__()} back to {moves_dictionary[tuple(move.origin_loc)]}\n')
        elif move.castling:
            castling_type = move.piece[2]
            if castling_type == 1 or castling_type == 3:
                castling = 'O-O'
            else:
                castling = 'O-O-O'

            file.write(f'--Undo {move.piece[0].color} King Castling {castling}\n')
        elif move.en_passant:
            pass
        else:
            file.write(f'--Undo {move.piece.color} {move.piece.__str__()} back to {moves_dictionary[tuple(move.origin_loc)]}\n')
    elif mode =='redo':
        move = context
        if move.pawn_promotion:
            file.write(f'--Redo {move.piece.color} {move.eaten_piece[1].__str__()} promoted to {move.piece.__str__()} on to {moves_dictionary[tuple(move.destination)]}\n')
        elif move.castling:
            castling_type = move.piece[2]
            if castling_type == 1 or castling_type == 3:
                castling = 'O-O'
            else:
                castling = 'O-O-O'

            file.write(f'--Redo {move.piece[0].color} King Castling {castling}\n')
        elif move.en_passant:
            pass
        else:
            file.write(f'--Redo {move.piece.color} {move.piece.__str__()} on to {moves_dictionary[tuple(move.destination)]}\n')

        # if mode=='normal move':
        #     (f'{last_move.color} {last_move.piece.__str__()} to {moves_dictionary[tuple(last_move.destination)]} {seperator}{crash}{check}{check_mate}\n')
        

        # elif mode == 'undo':
        #     print('normal undo')
        #     move = context
        #     file.write(f'--Undo {move.piece.color} {move.piece.__str__()} back to {moves_dictionary[tuple(move.origin_loc)]}\n')
        # elif mode =='redo':
        #     move = context
        #     file.write(f'--Redo {move.piece.color} {move.piece.__str__()} on to {moves_dictionary[tuple(move.destination)]}\n')










    # if last_move.pawn_promotion:

    #     if mode=='normal move':
        
    #         check_bool = context
            
    #         # last_move = game_moves_stack.properties[game_moves_stack.top]

    #         sep = False
    #         # iffff=Move(2,2,2,2,2,2,2,2)
    #         # iffff.pawn_promotion
    #         # iffff.castling
    #         # iffff.en_passant

    #         if last_move.eaten_piece[0] is not None:
    #             crash = ' Crash'
    #             sep = True
    #         else:
    #             crash = ''

    #         if check_bool:
    #             check = ' Check'
    #             sep = True
    #         else:
    #             check = ''

    #         if game_boolean:
    #             check_mate = ''
    #         else:
    #             if winner=='Draw':
    #                 check_mate = ' Draw'
    #             else:
    #                 check_mate = ' Check Mate'
    #                 check = ''
    #             sep = True

    #         if sep:
    #             seperator = '-'
    #         else:
    #             seperator = ''

    #         file.write(f'{last_move.color} {last_move.eaten_piece[1].__str__()} to {moves_dictionary[tuple(last_move.destination)]} promoted to {last_move.piece.__str__()} {seperator}{crash}{check}{check_mate}\n')

    #     elif mode == 'undo':
    #         print('undo pawn promotion')
    #         move = context
    #         file.write(f'--Undo {move.piece.color} {move.piece.__str__()} depromoted to {move.eaten_piece[1].__str__()} back to {moves_dictionary[tuple(move.origin_loc)]}\n')
    #     elif mode =='redo':
    #         move = context
    #         file.write(f'--Redo {move.piece.color} {move.eaten_piece[1].__str__()} promoted to {move.piece.__str__()} on to {moves_dictionary[tuple(move.destination)]}\n')
        
    # elif last_move.castling:
    #     pass
    # elif last_move.en_passant:
    #     pass
    # else:

    #     if mode=='normal move':
        
    #         check_bool = context
            
    #         # last_move = game_moves_stack.properties[game_moves_stack.top]

    #         sep = False
    #         # iffff=Move(2,2,2,2,2,2,2,2)
    #         # iffff.pawn_promotion
    #         # iffff.castling
    #         # iffff.en_passant

    #         if last_move.eaten_piece is not None:
    #             crash = ' Crash'
    #             sep = True
    #         else:
    #             crash = ''

    #         if check_bool:
    #             check = ' Check'
    #             sep = True
    #         else:
    #             check = ''

    #         if game_boolean:
    #             check_mate = ''
    #         else:
    #             if winner=='Draw':
    #                 check_mate = ' Draw'
    #             else:
    #                 check_mate = ' Check Mate'
    #                 check = ''
    #             sep = True

    #         if sep:
    #             seperator = '-'
    #         else:
    #             seperator = ''

    #         file.write(f'{last_move.color} {last_move.piece.__str__()} to {moves_dictionary[tuple(last_move.destination)]} {seperator}{crash}{check}{check_mate}\n')

    #     elif mode == 'undo':
    #         print('normal undo')
    #         move = context
    #         file.write(f'--Undo {move.piece.color} {move.piece.__str__()} back to {moves_dictionary[tuple(move.origin_loc)]}\n')
    #     elif mode =='redo':
    #         move = context
    #         file.write(f'--Redo {move.piece.color} {move.piece.__str__()} on to {moves_dictionary[tuple(move.destination)]}\n')


    file.close()

def CheckMate_condition():
    
    enemy_king:pieces.King

    enemy_moves = []

    for piece in pieces.alive_pieces :
        if piece.color == pieces.turn:
            enemy_moves.extend(piece.allowedMoves(True))
            if piece.__str__()=='King':
                # print('king initilizied')
                enemy_king = piece
        

        # else:
        #     if piece.__str__()=='King':
        #         # print('kinge khodi initlized')
        #         kingeKhodi = piece

    # print(f'enemey move = {enemy_moves} len = {len(enemy_moves)}')
    # print(f'enemy king = {enemy_king.allowedMoves(True)}')
                
    # if enemy_king.is_checked:
    #     print('ey vaaaaaaaaaay')
    # print(f'enemy king = {enemy_king.color}  vaziate kish = {enemy_king.is_checked}')
    # print(f'kinge khodi = {kingeKhodi.color}  vaziate kish = {kingeKhodi.is_checked}')

        
    if len(enemy_moves)==0:
        # print('game over')
        global game_boolean
        game_boolean = False
        global winner
        if enemy_king.is_checked:
            if pieces.turn=='White':
                winner = 'Black'
            else:
                winner = 'White'
        else:
            winner = 'Draw'

def draw_final_board():

    run = True

    while run:

        timer.tick(fps)

        game_screen.fill('dark gray')
        
        game_screen.blit(game_board,(200,0))

        draw_pieces()

        draw_eaten_pieces()

        pygame.draw.rect(game_screen,'black',[50,50,100,100])
        game_screen.blit(font_big.render('Undo',True,'white'),(57,85))

        pygame.draw.rect(game_screen,'black',[50,200,100,100])
        game_screen.blit(font_big.render('Redo',True,'white'),(57,235))

        if winner == 'Draw':
            game_screen.blit(font_big.render('Draw !!!',True,'black'),(430,625))
        else:
            game_screen.blit(font_big.render(f'Winner is {winner} !',True,'black'),(350,625))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()

def check_timer():

    sec = TIMER_DURATION - (time.time() - t0)
    sec = '%.1f' % sec

    game_screen.fill('dark gray',[15,345,180,100])
    pygame.draw.rect(game_screen,'black',[15,345,180,100],2)
    game_screen.blit(font_big.render('Time Left:',True,'black'),(20,350))
    game_screen.blit(font_big.render(sec,True,'black'),(75,400))
    pygame.display.update([15,345,180,100])
    # pygame.display.flip()

    if float(sec) <= 0 :
        global game_boolean
        game_boolean = False
        global winner
        winner = 'Black' if pieces.turn=='White' else 'White'

def pawn_promotion(pawn:pieces.Pawn):

    queen_img = pygame.image.load(f'imgs/{pawn.color}_Queen.png')
    queen_img = pygame.transform.scale(queen_img, (50,50))
    knight_img = pygame.image.load(f'imgs/{pawn.color}_Knight.png')
    knight_img = pygame.transform.scale(knight_img, (50,50))
    bishop_img = pygame.image.load(f'imgs/{pawn.color}_Bishop.png')
    bishop_img = pygame.transform.scale(bishop_img, (50,50))
    rook_img = pygame.image.load(f'imgs/{pawn.color}_Rook.png')
    rook_img = pygame.transform.scale(rook_img, (50,50))

    piece_selected = False
    while not piece_selected:
        game_screen.fill('dark gray',[430,230,140,140])
        # game_screen.blit(piece.img,cal_screen_position(piece.row,piece.column))
        game_screen.blit(queen_img,cal_screen_position(3,3))
        game_screen.blit(knight_img,cal_screen_position(3,4))
        game_screen.blit(bishop_img,cal_screen_position(4,3))
        game_screen.blit(rook_img,cal_screen_position(4,4))

        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        if mouseX>=430 and mouseX<=500 and mouseY>=230 and mouseY<=300:
            pygame.draw.rect(game_screen,'red',[430,230,70,70],2)
        elif mouseX>=500 and mouseX<=570 and mouseY>=230 and mouseY<=300:
            pygame.draw.rect(game_screen,'red',[500,230,70,70],2)
        elif mouseX>=430 and mouseX<=500 and mouseY>=300 and mouseY<=370:
            pygame.draw.rect(game_screen,'red',[430,300,70,70],2)
        elif mouseX>=500 and mouseX<=570 and mouseY>=300 and mouseY<=370:
            pygame.draw.rect(game_screen,'red',[500,300,70,70],2)
        

        pygame.display.update([430,230,140,140])

        check_timer()


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.MOUSEBUTTONDOWN:

                promoted_piece = None

                if mouseX>=430 and mouseX<=500 and mouseY>=230 and mouseY<=300:
                    promoted_piece = pieces.Queen(pawn.color,queen_img,pawn.row,pawn.column)
                elif mouseX>=500 and mouseX<=570 and mouseY>=230 and mouseY<=300:
                    promoted_piece = pieces.Knight(pawn.color,knight_img,pawn.row,pawn.column)
                elif mouseX>=430 and mouseX<=500 and mouseY>=300 and mouseY<=370:
                    promoted_piece = pieces.Bishop(pawn.color,bishop_img,pawn.row,pawn.column)
                elif mouseX>=500 and mouseX<=570 and mouseY>=300 and mouseY<=370:
                    promoted_piece = pieces.Rook(pawn.color,rook_img,pawn.row,pawn.column)

                if promoted_piece is not None:
                    piece_selected = True
                    last_move:Move = game_moves_stack.pop()
                    last_move.pawn_promotion = True
                    last_move.piece = promoted_piece
                    last_move.eaten_piece = [last_move.eaten_piece,pawn]
                    game_moves_stack.push(last_move)
                    pieces.alive_pieces.remove(pawn)
                    pieces.alive_pieces.append(promoted_piece)




    # new_queen_img = 'imgs/White_Queen.png' if pawn.color=='White' else 'imgs/Black_Queen.png'
                    
    # new_queen_img = f'imgs/{pawn.color}_Queen.png'
    # new_queen = pieces.Queen(pawn.color,pygame.image.load(new_queen_img),pawn.row,pawn.column)
    # new_queen.setScale(pygame.transform.scale(new_queen.img,(50,50)))

    # WL_rook.setScale(pygame.transform.scale(WL_rook.img,(50,50)))

    # last_move:Move = game_moves_stack.pop()
    # last_move.piece = new_queen
    # game_moves_stack.push(last_move)
    # pieces.alive_pieces.remove(pawn)
    # pieces.alive_pieces.append(new_queen)

    # pygame.draw.rect(game_screen,'red',[430,230,140,140],2)

def check_castling(move:Move):

    origin_row , origin_col = move.origin_loc
    des_row , des_col = move.destination

    for piece in pieces.alive_pieces:
        if piece.__str__() == 'Rook':
            if piece.color == 'White':
                if piece.type == 'Right':
                    RW_Rook:pieces.Rook = piece
                elif piece.type == 'Left':
                    LW_Rook:pieces.Rook = piece
            else:
                if piece.type == 'Right':
                    RB_Rook:pieces.Rook = piece
                elif piece.type == 'Left':
                    LB_Rook:pieces.Rook = piece

    
    if move.piece.__str__() == 'King':

        if move.piece.color=='White':

            if origin_row==7 and origin_col==4:
                if des_row==7 and des_col==6:
                    # right white castling
                    move.castling = True
                    # [king, [moven rook , rook starting position , rook destination], castling type]
                    # castling types:
                    # right white = 1
                    # left white = 2
                    # right black = 3
                    # left black = 4
                    # move.piece = [move.piece, [RW_Rook,[7,7],[7,5]],1]
                    move.piece = [move.piece, RW_Rook, 1]
                    RW_Rook.setPosition(7,5)
                elif des_row==7 and des_col==2:
                    # left white castling
                    move.castling = True
                    move.piece = [move.piece, LW_Rook, 2]
                    LW_Rook.setPosition(7,3)
                    
        else:

            if origin_row==0 and origin_col==4:
                if des_row==0 and des_col==6:
                    # right black castling 
                    move.castling = True
                    move.piece = [move.piece, RB_Rook, 3]
                    RB_Rook.setPosition(0,5)
                elif des_row==0 and des_col==2:
                    # left black castling
                    move.castling = True
                    move.piece = [move.piece, LB_Rook, 4]
                    LB_Rook.setPosition(0,3)

#top of board = 228 , 30
# size of squares = 66
winner = 'no one'
BOARD_UPPER_LENGTH = 30
BOARD_SIDE_LENGTH = 228
BOX_LENGTH = 68
TIMER_DURATION = 30

pygame.init()

WIDTH = 1000
HEIGHT = 680

game_screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Chess Project')
font_small = pygame.font.Font('freesansbold.ttf',20)
font_big = pygame.font.Font('freesansbold.ttf',35)
timer = pygame.time.Clock()
fps = 60



game_board = pygame.image.load('imgs/chess_board.jpg')

game_board = pygame.transform.scale(game_board,(600,600))


# pieces.alive_pieces = []
eaten_pieces = []

game_moves = Queue(12000)

game_moves_stack = Stack(12000)
game_moves_temp_stack = Stack(12000)

initialize_pieces()
#top of board = 228 , 30
# size of squares = 66

# pieces.turn = 'White'

#clear file
file = open('GameLog.txt','wt')
file.close()

t0 = time.time()

game_boolean = True
while game_boolean:

    timer.tick(fps)

    game_screen.fill('dark gray')
    
    game_screen.blit(game_board,(200,0))
    
    draw_pieces()

    draw_eaten_pieces()


    pygame.draw.rect(game_screen,'black',[50,50,100,100])
    game_screen.blit(font_big.render('Undo',True,'white'),(57,85))

    pygame.draw.rect(game_screen,'black',[50,200,100,100])
    game_screen.blit(font_big.render('Redo',True,'white'),(57,235))

    game_screen.blit(font_big.render(f'{pieces.turn}\'s turn',True,'black'),(400,625))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_boolean = False
            # print("good exit ")
            pygame.quit()
            sys.exit()
            # break
        
        #select a piece
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            # print(cal_board_index(mouseX,mouseY))
            cordinate = cal_board_index(mouseX,mouseY)

            check_Undo(mouseX,mouseY)
            check_Redo(mouseX,mouseY)

            piece = pieces.check_piece_on_box(cordinate[0],cordinate[1])
            print(piece)
            
            if piece is not None:
         
                if piece.color == pieces.turn:
                    
                    # print('----------------\neaten pieces:')
                    # for pie in eaten_pieces:
                    #     print(pie)
                    # # print(eaten_pieces)
                    # print('----------------')

                   
                    move_piece(piece)
      
                    # check_bool = check_condition()

                    # update_gameLog(['normal move',check_bool])

                    
                else:
                    print('NOT YOUR TURN!!')



    # print(pygame.mouse.get_pos())
                    
    

    # initialize_pieces()

    # game_screen.blit(WL_rook.img,WL_rook.starting_position)
    check_timer()

    pygame.display.flip()


file = open('GameLog.txt','at')
if winner=='Draw':
    file.write('Draw !')
else:
    file.write(f'Winner is: {winner} !')
file.close()

if winner != 'no one':
    draw_final_board()

pygame.quit()