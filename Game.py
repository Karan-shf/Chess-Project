# from . import pieces
import pieces

import pygame

import sys

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

    def __init__(self,color,piece,origin_loc,destination,eaten_piece) -> None:
        self.color = color
        self.piece = piece
        self.origin_loc = origin_loc
        self.destination = destination
        self.eaten_piece = eaten_piece

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

        pygame.draw.circle(game_screen,(34,67,200-i),[cord[0]+BOX_LENGTH//3,cord[1]+BOX_LENGTH//3],BOX_LENGTH//4)
        pygame.display.flip()
        i+=10

def move_piece(piece):

    piece_seleceted = True

    print(piece.allowedMoves(True))

    # pygame.display.flip()
    piece_cord = cal_screen_position(piece.row,piece.column)
    pygame.draw.rect(game_screen,'red',[piece_cord[0]-9,piece_cord[1]-10,BOX_LENGTH,BOX_LENGTH],2)
    pygame.display.flip()

    while piece_seleceted:

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
                        # move.add_eaten_piece(des_piece)
                    piece.setPosition(cordinate2[0],cordinate2[1])
                    if piece.__str__() == 'Pawn':
                        # if not piece.has_moved:
                        #     piece.has_moved = True
                        piece.move_count += 1
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

    for piece in pieces.alive_pieces:

        # if pieces.turn != piece.color:
        for loc in piece.allowedMoves():

            dest_piece = pieces.check_piece_on_box(loc[0],loc[1])

            if dest_piece is not None:
                if dest_piece.__str__()=='King' and dest_piece.color != piece.color :
                    # dest_piece.setCheck(True)
                    print('CHECK!!!!!!!')

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
            move.piece.setPosition(move.origin_loc[0],move.origin_loc[1])
            if move.piece.__str__() == 'Pawn':
                move.piece.move_count -= 1
            if move.eaten_piece is not None:
                eaten_pieces.remove(move.eaten_piece)
                pieces.alive_pieces.append(move.eaten_piece)
            change_turn()
        except:
            print('no moves has been made!')

def check_Redo(mouseX , mouseY):

    if mouseX >=50 and mouseX <=150 and mouseY>=200 and mouseY<=300:
        print('REDO')
        try:
            move:Move = game_moves_temp_stack.pop()
            game_moves_stack.push(move)
            move.piece.setPosition(move.destination[0],move.destination[1])
            if move.piece.__str__() == 'Pawn':
                move.piece.move_count += 1
            if move.eaten_piece is not None:
                pieces.alive_pieces.remove(move.eaten_piece)
                eaten_pieces.append(move.eaten_piece)
            change_turn()
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

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_boolean = False
            # print("good exit ")
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
      
                    check_condition()

                    
                else:
                    print('NOT YOUR TURN!!')



    # print(pygame.mouse.get_pos())

    # initialize_pieces()

    # game_screen.blit(WL_rook.img,WL_rook.starting_position)

    pygame.display.flip()

pygame.quit()