# from . import pieces
import pieces

import pygame

import sys

# import copy

# def draw_borad():
#     for i in range(32):
#         column=i%4
#         row = i//4
#         if row % 2 == 0:
#             pygame.draw.rect(game_screen,'light gray',[450-(column*150), row*75, 75, 75])
#         else:
#             pygame.draw.rect(game_screen,'light gray',[525-(column*150), row*75, 75, 75])

class move:

    def __init__(self,color,piece,origin_loc,destination) -> None:
        self.color = color
        self.piece = piece
        self.origin_loc = origin_loc
        self.destination = destination

    def Undo(self):
        pass

    def Redo(self):
        pass

def initialize_pieces():

    WL_rook = pieces.Rook('White',pygame.image.load('imgs/White_Rook.png'),7,0)
    WL_rook.setScale(pygame.transform.scale(WL_rook.img,(50,50)))
    # WL_rook.setStartingPosition(WL_rook.img.get_rect())
    # WL_rook.starting_position.topleft = (250,500)
    pieces.alive_pieces.append(WL_rook)

    WR_rook = pieces.Rook('White',pygame.image.load('imgs/White_Rook.png'),7,7)
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




    BL_rook = pieces.Rook('Black',pygame.image.load('imgs/Black_Rook.png'),0,0)
    BL_rook.setScale(pygame.transform.scale(BL_rook.img,(50,50)))
    pieces.alive_pieces.append(BL_rook)

    BR_rook = pieces.Rook('Black',pygame.image.load('imgs/Black_Rook.png'),0,7)
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
    # game_screen.blit(W_Pawn1.img,W_Pawn1.starting_position)
    # game_screen.blit(W_Pawn2.img,W_Pawn2.starting_position)
    # game_screen.blit(W_Pawn3.img,W_Pawn3.starting_position)
    # game_screen.blit(W_Pawn4.img,W_Pawn4.starting_position)
    # game_screen.blit(W_Pawn5.img,W_Pawn5.starting_position)
    # game_screen.blit(W_Pawn6.img,W_Pawn6.starting_position)
    # game_screen.blit(W_Pawn7.img,W_Pawn7.starting_position)
    # game_screen.blit(W_Pawn8.img,W_Pawn8.starting_position)

    # game_screen.blit(WL_rook.img,WL_rook.starting_position)
    # game_screen.blit(WL_knight.img,WL_knight.starting_position)
    # game_screen.blit(WL_bishop.img,WL_bishop.starting_position)
    # game_screen.blit(W_Queen.img,W_Queen.starting_position)
    # game_screen.blit(W_King.img,W_King.starting_position)
    # game_screen.blit(WR_bishop.img,WR_bishop.starting_position)
    # game_screen.blit(WR_knight.img,WR_knight.starting_position)
    # game_screen.blit(WR_rook.img,WR_rook.starting_position)

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

# def pieces.check_piece_on_box(row,col):
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

def draw_allowedMoves():
    pass

def move_piece(piece):

    piece_seleceted = True

    print(3)

    print(piece.allowedMoves(True))

    print(4)

    piece_cord = cal_screen_position(piece.row,piece.column)
    pygame.draw.rect(game_board,'red',[piece_cord[0],piece_cord[1],BOX_LENGTH,BOX_LENGTH],2)

    while piece_seleceted:

        # for box in piece.allowedMoves(True):
        # #     # pygame.draw.circle(game_board,(45,35,199),[box[0],box[1]],40)
        #     cord = cal_screen_position(box[0],box[1])
        #     # pygame.draw.rect(game_board,'red',[cord[0]-BOARD_SIDE_LENGTH,cord[1],BOX_LENGTH,BOX_LENGTH])
        #     pygame.draw.circle(game_board,'blue',[cord[0]-BOARD_SIDE_LENGTH+BOX_LENGTH//1.5,cord[1]+BOARD_UPPER_LENGTH],BOX_LENGTH//4)

        for event2 in pygame.event.get():

            if event2.type==pygame.QUIT:
                global game_boolean
                game_boolean = False
                piece_seleceted = False
                break
            
            # print(f'piece selected={piece_seleceted}')

            if event2.type == pygame.MOUSEBUTTONDOWN:
                mouseX2 = pygame.mouse.get_pos()[0]
                mouseY2 = pygame.mouse.get_pos()[1]

                cordinate2 = cal_board_index(mouseX2,mouseY2)


                if cordinate2 in piece.allowedMoves(True):
                    des_piece = pieces.check_piece_on_box(cordinate2[0],cordinate2[1])
                    if des_piece is not None:
                        pieces.alive_pieces.remove(des_piece)
                        eaten_pieces.append(des_piece)
                    piece.setPosition(cordinate2[0],cordinate2[1])
                    if piece.__str__() == 'Pawn':
                        if not piece.has_moved:
                            piece.has_moved = True
                    change_turn()
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

    # if pieceee is not None and consider_destination is not None:

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
    #                     #                                   dest_piece.color == pieces.turn
    #                     if dest_piece.__str__()=='King' and dest_piece.color != checking_piece.color :
    #                         # dest_piece.setCheck(True)
    #                         pieceee.row = origin_row
    #                         pieceee.column = origin_column
    #                         print('not allowed to move!')
    #                         repieces.turn True
    #     pieceee.row = origin_row
    #     pieceee.column = origin_column
    #     repieces.turn False
    
    # else:
    

        # for loc in piece.allowedMoves():

        #     dest_piece = pieces.check_piece_on_box(loc[0],loc[1])

        #     if dest_piece is not None:
        #         if dest_piece.__str__()=='King' and dest_piece.color != piece.color :
        #             dest_piece.setCheck(True)
        #             print('CHECK!!!!!!!')
        # white_king_found = False
        # black_king_found = False

        # white_king:pieces.King
        # black_king:pieces.King

        # for piece in pieces.alive_pieces:
        #     if piece.__str__()=='King':
        #         if piece.color == 'White':
        #             white_king = piece
        #             white_king_found = True
        #         else:
        #             black_king = piece
        #             black_king_found = True
        #         if white_king_found and black_king_found:
        #             break

        # if pieces.turn=='White':
        #     underS_king = white_king
        # else:
        #     underS_king = black_king

        


                    

        # if kingcheck:
        #     for piece in pieces.alive_pieces:
        #         if pieces.turn != piece.color:
        #             for loc in piece.allowedMoves():
        #                 dest_piece = pieces.check_piece_on_box(loc[0],loc[1])

        #                 if dest_piece is not None:
        #                     if dest_piece.__str__()=='King' and dest_piece.color != piece.color :
        #                         dest_piece.setCheck(True)
        #                         # print('CHECK!!!!!!!')
        #                         kingcheck = True
        #                         break
        #                     else:
        #                         # dest_piece.setCheck(False)
        #                         kingcheck = False

        # print(f'{pieces.turn} King check status = {kingcheck}')

        for piece in pieces.alive_pieces:

            # if pieces.turn != piece.color:
            for loc in piece.allowedMoves():

                dest_piece = pieces.check_piece_on_box(loc[0],loc[1])

                if dest_piece is not None:
                    if dest_piece.__str__()=='King' and dest_piece.color != piece.color :
                        # dest_piece.setCheck(True)
                        print('CHECK!!!!!!!')


#top of board = 228 , 30
# size of squares = 66

BOARD_UPPER_LENGTH = 30
BOARD_SIDE_LENGTH = 228
BOX_LENGTH = 68

pygame.init()

WIDTH = 1000
HEIGHT = 680

game_screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Chess Project')
font_small = pygame.font.Font('freesansbold.ttf',20)
font_big = pygame.font.Font('freesansbold.ttf',50)
timer = pygame.time.Clock()
fps = 60



game_board = pygame.image.load('imgs/chess_board.jpg')

game_board = pygame.transform.scale(game_board,(600,600))


# pieces.alive_pieces = []
eaten_pieces = []

initialize_pieces()
#top of board = 228 , 30
# size of squares = 66

# pieces.turn = 'White'

# pygame.draw.circle(game_board,(53,156,200,50),[200,300],50)

game_boolean = True
while game_boolean:

    timer.tick(fps)

    game_screen.fill('dark gray')
    # game_screen.fill(pygame.Color.a)
    # draw_borad()
    # game_screen.blit(game_board,brect)

    game_screen.blit(game_board,(200,0))
    # game_screen.blit(game_board,(-28,-28))
    # game_screen.blit(game_board,(-96,0))

    draw_pieces()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_boolean = False
            # print("good exit gmnlskn")
            sys.exit()
            # break
        
        #select a piece
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            # print(cal_board_index(mouseX,mouseY))
            cordinate = cal_board_index(mouseX,mouseY)
            piece = pieces.check_piece_on_box(cordinate[0],cordinate[1])
            print(piece)
            # pygame.draw.rect(game_board,'red',[mouseX,mouseY,BOX_LENGTH,BOX_LENGTH])
            if piece is not None:
                print(1)
                if piece.color == pieces.turn:
                    # for box in piece.allowedMoves():
           
                        # print('rect!!!!!!')
                        # cord = cal_screen_position(box[0],box[1])
                        # pygame.draw.rect(game_board,'red',[cord[0]-BOARD_SIDE_LENGTH,cord[1],BOX_LENGTH,BOX_LENGTH])
                        # pygame.draw.circle(game_board,'blue',[cord[0]-BOARD_SIDE_LENGTH,cord[1]+BOARD_UPPER_LENGTH],BOX_LENGTH//2)
                    
                    # print('----------------\neaten pieces:')
                    # for pie in eaten_pieces:
                    #     print(pie)
                    # # print(eaten_pieces)
                    # print('----------------')

                    # for box in piece.allowedMoves():
                    #     print('circle!!!')
                    #     pygame.draw.circle(game_board,(45,35,199),cal_screen_position(box[0],box[1]),30)
                    print(2)
                    move_piece(piece)
                    print(5)
                    check_condition()

                    # piece_seleceted = True
                    # while piece_seleceted:

                    #     for event2 in pygame.event.get():
                    #         if event2.type==pygame.QUIT:
                    #             game_boolean = False
                    #             piece_seleceted = False
                    #             break
                            
                    #         if event2.type == pygame.MOUSEBUTTONDOWN:
                    #             mouseX2 = pygame.mouse.get_pos()[0]
                    #             mouseY2 = pygame.mouse.get_pos()[1]
                    #             # print(cal_board_index(mouseX,mouseY))
                    #             cordinate2 = cal_board_index(mouseX2,mouseY2)
                    #             print(cordinate2)
                    #             piece.setPosition(cordinate2[0],cordinate2[1])
                    #             print(f'piece: {piece}')
                    #             print(f'piece row : {piece.row}')
                    #             print(f'piece col : {piece.column}')
                    #             change_pieces.turn()
                    #             piece_seleceted = False
                else:
                    print('NOT YOUR TURN!!')



    # print(pygame.mouse.get_pos())
                    
    


    

    # initialize_pieces()

    # game_screen.blit(WL_rook.img,WL_rook.starting_position)

    pygame.display.flip()

pygame.quit()