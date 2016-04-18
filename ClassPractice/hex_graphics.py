import pygame
import math
from hex import *

# THE WONDERFUL WORLD OF COLOR! (Copyright: The Walt Disney Company)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# Setup the Window and a bunch of variables
cell_size = 4
cell_gap = 35
width = 15
height = width
screen_width = (cell_size + cell_gap) * width + height * (cell_size + cell_gap) / 2
screen_height = 20 + (cell_size + cell_gap - 5) * height
pygame.init()
# Fonts
font = pygame.font.SysFont('Calibri', 48, False, False)
fonttwo = pygame.font.SysFont('Calibri', 16, False, False)
fontthree = pygame.font.SysFont('Calibri', 32, False, False)
fontfour = pygame.font.SysFont('Calibri', 36, True, False)
# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
# *Sings* What's the name of the game #ABBA
pygame.display.set_caption("Hex")

# Draws the pretty li'l hexagons on the screen
def drawBoard(A):
    for row in range(height):
        y_pos = 10 + (cell_size + cell_gap - 5) * row
        for col in range(width):
            x_pos = 10 + (cell_size + cell_gap) * col + (height - row) * (cell_size + cell_gap) / 2
            vertices = [(x_pos, y_pos), (x_pos+4*cell_size, y_pos+2*cell_size),
                        (x_pos+4*cell_size, y_pos+7*cell_size),(x_pos, y_pos+9*cell_size),
                        (x_pos-4*cell_size, y_pos+7*cell_size),(x_pos-4*cell_size, y_pos+2*cell_size)]
            if A.tiles[row][col] == "O":
                pygame.draw.polygon(screen, WHITE, vertices)
            elif A.tiles[row][col] == "H":
                pygame.draw.polygon(screen, BLUE, vertices)
            elif A.tiles[row][col] == "V":
                pygame.draw.polygon(screen, RED, vertices)

# Where our friend Jerry is and Tom would like to be
def mouseData():
    """
    :return: Concise summary of mouse data
    """
    output = [False, 0, 0]
    if pygame.mouse.get_pressed()[0] == 1:
        output[0] = True
    mouseloc = pygame.mouse.get_pos()
    output[1] = mouseloc[0]
    output[2] = mouseloc[1]
    return output

# Plays a piece at a certain square
def clickInput(board, type):
    """
    :param type: Type of piece to be played
    :return: Checks the location of the cursor and registers a click on a particular tile
    """
    played = False
    mouseinf = mouseData()
    row = int(math.floor((mouseinf[2] - 10)/(cell_size + cell_gap - 5)))
    column = int(math.floor(((mouseinf[1] - (10 + ((height - (row + 1)) *
                                                   (cell_size + cell_gap) / 2)))/(cell_size + cell_gap))))
    if (0 <= row < height) and (0 <= column < width):
        played = board.play(type, row, column)
    return played

# I hope you can guess what this function does
def printRules():
    rulesa = fonttwo.render("Blue connects across", True, CYAN)
    rulesb = fonttwo.render("Red connects down", True, CYAN)
    rulesc = fonttwo.render("Blue goes first", True, CYAN)
    screen.blit(rulesa, [10, 10])
    screen.blit(rulesb, [10, 30])
    screen.blit(rulesc, [10, 50])

# Prints the AI selection text
def printAIText():
    headertext = fontfour.render("Pick an AI difficulty level by", True, WHITE)
    headertext2 = fontfour.render("pressing the appropriate key", True, WHITE)
    aitext1 = fontthree.render("1) Random AI", True, WHITE)
    aitext2 = fontthree.render("2) Easy AI", True, WHITE)
    aitext3 = fontthree.render("3) Medium AI", True, WHITE)
    aitext4 = fontthree.render("4) Hard AI", True, WHITE)
    screen.blit(headertext, [screen_width/2 - 180, screen_height/2 - 150])
    screen.blit(headertext2, [screen_width/2 - 180, screen_height/2 - 110])
    screen.blit(aitext1, [screen_width/2 - 100, screen_height/2 - 60])
    screen.blit(aitext2, [screen_width/2 - 100, screen_height/2 - 30])
    screen.blit(aitext3, [screen_width/2 - 100, screen_height/2 - 0])
    screen.blit(aitext4, [screen_width/2 - 100, screen_height/2 + 30])

# Prints a more complete explanation of the rules
def printAllRules():
    rules1 = fontthree.render("Hex is a two-player board game played on a board", True, WHITE)
    rules2 = fontthree.render("of hexagons. On a turn, each player colors any", True, WHITE)
    rules3 = fontthree.render("unoccupied tile on the board with the goal of", True, WHITE)
    rules4 = fontthree.render("connecting their two sides of the board with a", True, WHITE)
    rules5 = fontthree.render("congruent line of tiles. In this version, you", True, WHITE)
    rules6 = fontthree.render("will be playing the blue tiles and trying to", True, WHITE)
    rules7 = fontthree.render("connect the left and right sides of the board", True, WHITE)
    rules8 = fontthree.render("while the computer will be trying to connect", True, WHITE)
    rules9 = fontthree.render("the top and bottom with red.  Click to continue.", True, WHITE)
    screen.blit(rules1, [screen_width/2 - 300, screen_height/2 - 200])
    screen.blit(rules2, [screen_width/2 - 300, screen_height/2 - 160])
    screen.blit(rules3, [screen_width/2 - 300, screen_height/2 - 120])
    screen.blit(rules4, [screen_width/2 - 300, screen_height/2 - 80])
    screen.blit(rules5, [screen_width/2 - 300, screen_height/2 - 40])
    screen.blit(rules6, [screen_width/2 - 300, screen_height/2 - 0])
    screen.blit(rules7, [screen_width/2 - 300, screen_height/2 + 40])
    screen.blit(rules8, [screen_width/2 - 300, screen_height/2 + 80])
    screen.blit(rules9, [screen_width/2 - 300, screen_height/2 + 120])

# Another slew of variables
# Conditionals for the four game loopz
done = False
done2 = False
done3 = False
done4 = False
# Creates the game board
board = Board(width)
# Sets default value of variables
turn = "H"
played = True
winner = "Nobody"
hcheck = [False, "N"]
vcheck = [False, "N"]
aitype = 0
# Are there 2 AIs
# This is hardcoded to have a player, but it can easily be changed
aplayer = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            done2 = True
            done3 = True
            done4 = True
    # Print the full rules
    printAllRules()
    pygame.display.flip()
    pygame.draw.rect(screen, BLACK, [0, 0, screen_width, screen_height])
    if mouseData()[0]:
        done = True

while not done2:
    # Select AI type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done2 = True
            done3 = True
            done4 = True
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_1]:
                aiType = 1
                done2 = True
            elif pygame.key.get_pressed()[pygame.K_2]:
                aiType = 2
                done2 = True
            elif pygame.key.get_pressed()[pygame.K_3]:
                aiType = 3
                done2 = True
            elif pygame.key.get_pressed()[pygame.K_4]:
                aiType = 4
                done2 = True
    printAIText()
    pygame.display.flip()
    pygame.draw.rect(screen, BLACK, [0, 0, screen_width, screen_height])

while not done3:
    # Blue wins across, Red wins down
    # Blue goes first
    printRules()
    if turn == "V":
        # AI playing
        if aiType == 1:
            hexLv1("V").play(board)
        elif aiType == 2:
            hexLv2("V").play(board)
        elif aiType == 3:
            hexLv3("V").play(board)
        elif aiType == 4:
            hexLv4("V").play(board)
        turn = "H"
    mouseinfo = mouseData()
    if aplayer:
        if turn == "H":
            if aiType == 1:
                hexLv1("H").play(board)
            elif aiType == 2:
                hexLv2("H").play(board)
            elif aiType == 3:
                hexLv3("H").play(board)
            elif aiType == 4:
                hexLv4("H").play(board)
            turn = "V"
    else:
        if mouseinfo[0] and turn == "H":
            played = False
            played = clickInput(board, turn)
            if played:
                if turn == "H":
                    turn = "V"
                else:
                    turn = "H"
    # Checks for winners
    hcheck = board.checkWinHz("H")
    vcheck = board.checkWinVt("V")
    if hcheck[0] or vcheck[0]:
        done3 = True
    drawBoard(board)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done3 = True
            done4 = True

while not done4:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done4 = True
    pygame.draw.rect(screen, BLACK, [0, 0, screen_width, screen_height])
    if hcheck[1] == "H":
        winner = "Blue"
    else:
        winner = "Red"
    drawBoard(board)
    wintexta = font.render(winner, True, CYAN)
    wintextb = font.render("Wins!", True, CYAN)
    screen.blit(wintexta, [5, 5])
    screen.blit(wintextb, [5, 60])
    pygame.display.flip()
