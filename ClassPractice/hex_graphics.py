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

# Setup the Window etc
cell_size = 4
cell_gap = 35
width = 12
height = width
screen_width = (cell_size + cell_gap) * width + height * (cell_size + cell_gap) / 2
screen_height = 20 + (cell_size + cell_gap - 5) * height
pygame.init()
font = pygame.font.SysFont('Calibri', 48, False, False)
fonttwo = pygame.font.SysFont('Calibri', 16, False, False)
# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

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

# Where our friend Jerry is
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


def printRules():
    rulesa = fonttwo.render("Blue connects across", True, CYAN)
    rulesb = fonttwo.render("Red connects down", True, CYAN)
    rulesc = fonttwo.render("Blue goes first", True, CYAN)
    screen.blit(rulesa, [10, 10])
    screen.blit(rulesb, [10, 30])
    screen.blit(rulesc, [10, 50])

done = False
done2 = False
board = Board(width)
turn = "H"
played = True
winner = "Nobody"

while not done:
    # Blue wins across, Red wins down
    # Blue goes first
    printRules()
    mouseinfo = mouseData()
    if mouseinfo[0] and turn == "H":
        played = False
        played = clickInput(board, turn)
        if played:
            if turn == "H":
                turn = "V"
            else:
                turn = "H"
    if turn == "V":
        hexAI("V").smartPlay(board)
        turn = "H"
    # Checks for winners
    hcheck = board.checkWinHz("H")
    vcheck = board.checkWinVt("V")
    if hcheck[0] or vcheck[0]:
        done = True
    drawBoard(board)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            done2 = True

while not done2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done2 = True
    pygame.draw.rect(screen, BLACK, [0,0,screen_width,screen_height])
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


