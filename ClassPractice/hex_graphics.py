import pygame
import math
import time
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
width = 8
height = width
screen_width = (cell_size + cell_gap) * width + height * (cell_size + cell_gap) / 2
screen_height = 20 + (cell_size + cell_gap - 5) * height
pygame.init()
font = pygame.font.SysFont('Calibri', 12, False, False)
# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hex")


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
            elif A.tiles[row][col] == "W":
                pygame.draw.polygon(screen, BLUE, vertices)
            elif A.tiles[row][col] == "X":
                pygame.draw.polygon(screen, RED, vertices)


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


def clickInput(board, type):
    """
    :param type: Type of piece to be played
    :return: Checks the location of the cursor and registers a click on a particular tile
    """
    mouseinfo = mouseData()
    row = int(math.floor((mouseinfo[2] - 10)/(cell_size + cell_gap - 5)))
    column = int(math.floor(((mouseinfo[1] - (10 + ((height - (row + 1)) *
                                                    (cell_size + cell_gap) / 2)))/(cell_size + cell_gap))))
    if (0 <= row < height) and (0 <= column < width):
        board.play(type, row, column)

done = False

clock = pygame.time.Clock()
board = Board(width)
turn = "W"
again = time.time()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    drawBoard(board)
    mouseinfo = mouseData()
    now = time.time()
    if mouseinfo[0] and (now - again > 1):
        clickInput(board, turn)
        if turn == "W":
            turn = "X"
        else:
            turn = "W"
        again = time.time()
    pygame.display.flip()



