# from . import pieces
import pieces

import pygame

# def draw_borad():
#     for i in range(32):
#         column=i%4
#         row = i//4
#         if row % 2 == 0:
#             pygame.draw.rect(game_screen,'light gray',[450-(column*150), row*75, 75, 75])
#         else:
#             pygame.draw.rect(game_screen,'light gray',[525-(column*150), row*75, 75, 75])

def initialize_pieces():

    WL_rook = pieces.Rook('White',pygame.image.load('imgs/White_Rook.png'),7,0)
    WL_rook.setScale(pygame.transform.scale(WL_rook.img,(50,50)))
    # WL_rook.setStartingPosition(WL_rook.img.get_rect())
    # WL_rook.starting_position.topleft = (250,500)
    alive_pieces.append(WL_rook)

    WR_rook = pieces.Rook('White',pygame.image.load('imgs/White_Rook.png'),7,7)
    WR_rook.setScale(pygame.transform.scale(WR_rook.img,(50,50)))
    # WR_rook.setStartingPosition(WR_rook.img.get_rect())
    # WR_rook.starting_position.topleft = (700,500)
    alive_pieces.append(WR_rook)

    WL_knight = pieces.Knight('White',pygame.image.load('imgs/White_Knight.png'),7,1)
    WL_knight.setScale(pygame.transform.scale(WL_knight.img,(50,50)))
    # WL_knight.setStartingPosition(WL_knight.img.get_rect())
    # WL_knight.starting_position.topleft = (320,500)
    alive_pieces.append(WL_knight)

    WR_knight = pieces.Knight('White',pygame.image.load('imgs/White_Knight.png'),7,6)
    WR_knight.setScale(pygame.transform.scale(WR_knight.img,(50,50)))
    # WR_knight.setStartingPosition(WR_knight.img.get_rect())
    # WR_knight.starting_position.topleft = (630,500)
    alive_pieces.append(WR_knight)
   
    WL_bishop = pieces.Bishop('White',pygame.image.load('imgs/White_Bishop.png'),7,2)
    WL_bishop.setScale(pygame.transform.scale(WL_bishop.img,(50,50)))
    # WL_bishop.setStartingPosition(WL_bishop.img.get_rect())
    # WL_bishop.starting_position.topleft = (380,500)
    alive_pieces.append(WL_bishop)

    WR_bishop = pieces.Bishop('White',pygame.image.load('imgs/White_Bishop.png'),7,5)
    WR_bishop.setScale(pygame.transform.scale(WR_bishop.img,(50,50)))
    # WR_bishop.setStartingPosition(WR_bishop.img.get_rect())
    # WR_bishop.starting_position.topleft = (570,500)
    alive_pieces.append(WR_bishop)

    W_Queen = pieces.Queen('White',pygame.image.load('imgs/White_Queen.png'),7,3)
    W_Queen.setScale(pygame.transform.scale(W_Queen.img,(50,50)))
    # W_Queen.setStartingPosition(W_Queen.img.get_rect())
    # W_Queen.starting_position.topleft = (440,500)
    alive_pieces.append(W_Queen)

    W_King = pieces.King('White',pygame.image.load('imgs/White_King.png'),7,4)
    W_King.setScale(pygame.transform.scale(W_King.img,(50,50)))
    # W_King.setStartingPosition(W_King.img.get_rect())
    # W_King.starting_position.topleft = (510,500)
    alive_pieces.append(W_King)

    W_Pawn1 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,0)
    W_Pawn1.setScale(pygame.transform.scale(W_Pawn1.img,(50,50)))
    # W_Pawn1.setStartingPosition(W_Pawn1.img.get_rect())
    # W_Pawn1.starting_position.topleft = (250,430)
    alive_pieces.append(W_Pawn1)

    W_Pawn2 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,1)
    W_Pawn2.setScale(pygame.transform.scale(W_Pawn2.img,(50,50)))
    # W_Pawn2.setStartingPosition(W_Pawn2.img.get_rect())
    # W_Pawn2.starting_position.topleft = (320,430)
    alive_pieces.append(W_Pawn2)

    W_Pawn3 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,2)
    W_Pawn3.setScale(pygame.transform.scale(W_Pawn3.img,(50,50)))
    # W_Pawn3.setStartingPosition(W_Pawn3.img.get_rect())
    # W_Pawn3.starting_position.topleft = (380,430)
    alive_pieces.append(W_Pawn3)

    W_Pawn4 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,3)
    W_Pawn4.setScale(pygame.transform.scale(W_Pawn4.img,(50,50)))
    # W_Pawn4.setStartingPosition(W_Pawn4.img.get_rect())
    # W_Pawn4.starting_position.topleft = (440,430)
    alive_pieces.append(W_Pawn4)

    W_Pawn5 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,4)
    W_Pawn5.setScale(pygame.transform.scale(W_Pawn5.img,(50,50)))
    # W_Pawn5.setStartingPosition(W_Pawn5.img.get_rect())
    # W_Pawn5.starting_position.topleft = (510,430)
    alive_pieces.append(W_Pawn5)

    W_Pawn6 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,5)
    W_Pawn6.setScale(pygame.transform.scale(W_Pawn6.img,(50,50)))
    # W_Pawn6.setStartingPosition(W_Pawn6.img.get_rect())
    # W_Pawn6.starting_position.topleft = (570,430)
    alive_pieces.append(W_Pawn6)

    W_Pawn7 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,6)
    W_Pawn7.setScale(pygame.transform.scale(W_Pawn7.img,(50,50)))
    # W_Pawn7.setStartingPosition(W_Pawn7.img.get_rect())
    # W_Pawn7.starting_position.topleft = (630,430)
    alive_pieces.append(W_Pawn7)

    W_Pawn8 = pieces.Pawn('White',pygame.image.load('imgs/White_Pawn.png'),6,7)
    W_Pawn8.setScale(pygame.transform.scale(W_Pawn8.img,(50,50)))
    # W_Pawn8.setStartingPosition(W_Pawn8.img.get_rect())
    # W_Pawn8.starting_position.topleft = (700,430)
    alive_pieces.append(W_Pawn8)




    BL_rook = pieces.Rook('Black',pygame.image.load('imgs/Black_Rook.png'),0,0)
    BL_rook.setScale(pygame.transform.scale(BL_rook.img,(50,50)))
    alive_pieces.append(BL_rook)

    BR_rook = pieces.Rook('Black',pygame.image.load('imgs/Black_Rook.png'),0,7)
    BR_rook.setScale(pygame.transform.scale(BR_rook.img,(50,50)))
    alive_pieces.append(BR_rook)

    BL_knight = pieces.Knight('Black',pygame.image.load('imgs/Black_Knight.png'),0,1)
    BL_knight.setScale(pygame.transform.scale(BL_knight.img,(50,50)))
    alive_pieces.append(BL_knight)

    BR_knight = pieces.Knight('Black',pygame.image.load('imgs/Black_Knight.png'),0,6)
    BR_knight.setScale(pygame.transform.scale(BR_knight.img,(50,50)))
    alive_pieces.append(BR_knight)
   
    BL_bishop = pieces.Bishop('Black',pygame.image.load('imgs/Black_Bishop.png'),0,2)
    BL_bishop.setScale(pygame.transform.scale(BL_bishop.img,(50,50)))
    alive_pieces.append(BL_bishop)

    BR_bishop = pieces.Bishop('Black',pygame.image.load('imgs/Black_Bishop.png'),0,5)
    BR_bishop.setScale(pygame.transform.scale(BR_bishop.img,(50,50)))
    alive_pieces.append(BR_bishop)

    B_Queen = pieces.Queen('Black',pygame.image.load('imgs/Black_Queen.png'),0,3)
    B_Queen.setScale(pygame.transform.scale(B_Queen.img,(50,50)))
    alive_pieces.append(B_Queen)

    B_King = pieces.King('Black',pygame.image.load('imgs/Black_King.png'),0,4)
    B_King.setScale(pygame.transform.scale(B_King.img,(50,50)))
    alive_pieces.append(B_King)

    B_Pawn1 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,0)
    B_Pawn1.setScale(pygame.transform.scale(B_Pawn1.img,(50,50)))
    alive_pieces.append(B_Pawn1)

    B_Pawn2 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,1)
    B_Pawn2.setScale(pygame.transform.scale(B_Pawn2.img,(50,50)))
    alive_pieces.append(B_Pawn2)

    B_Pawn3 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,2)
    B_Pawn3.setScale(pygame.transform.scale(B_Pawn3.img,(50,50)))
    alive_pieces.append(B_Pawn3)

    B_Pawn4 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,3)
    B_Pawn4.setScale(pygame.transform.scale(B_Pawn4.img,(50,50)))
    alive_pieces.append(B_Pawn4)

    B_Pawn5 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,4)
    B_Pawn5.setScale(pygame.transform.scale(B_Pawn5.img,(50,50)))
    alive_pieces.append(B_Pawn5)

    B_Pawn6 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,5)
    B_Pawn6.setScale(pygame.transform.scale(B_Pawn6.img,(50,50)))
    alive_pieces.append(B_Pawn6)

    B_Pawn7 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,6)
    B_Pawn7.setScale(pygame.transform.scale(B_Pawn7.img,(50,50)))
    alive_pieces.append(B_Pawn7)

    B_Pawn8 = pieces.Pawn('Black',pygame.image.load('imgs/Black_Pawn.png'),1,7)
    B_Pawn8.setScale(pygame.transform.scale(B_Pawn8.img,(50,50)))
    alive_pieces.append(B_Pawn8)


def draw_pieces():
    for piece in alive_pieces:
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

# WL_rook = pieces.Rook('White',(0,0),pygame.image.load('White_Rook.png'))
# WL_rook.setScale(pygame.transform.scale(WL_rook.img,(50,50)))
# WL_rook.setStartingPosition(WL_rook.img.get_rect())
# WL_rook.starting_position.topleft = (255,495)

game_board = pygame.image.load('imgs/chess_board.jpg')

game_board = pygame.transform.scale(game_board,(600,600))
# brect = game_board.get_rect()

# brect.topleft = (200,0)

alive_pieces = []
eaten_pieces = []

initialize_pieces()
#top of board = 228 , 30
# size of squares = 66

game_boolean = True
while game_boolean:

    timer.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_boolean = False
            break
        
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            print(cal_board_index(mouseX,mouseY))

    # print(pygame.mouse.get_pos())

    game_screen.fill('dark gray')
    # draw_borad()
    # game_screen.blit(game_board,brect)

    game_screen.blit(game_board,(200,0))
    # game_screen.blit(game_board,(-28,-28))
    # game_screen.blit(game_board,(-96,0))

    draw_pieces()

    # initialize_pieces()
    # game_screen.blit(WL_rook.img,WL_rook.starting_position)

    pygame.display.flip()

pygame.quit()