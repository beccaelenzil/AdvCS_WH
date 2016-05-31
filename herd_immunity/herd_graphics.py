from herd_immunity import *
import pygame
import time

# THE WONDERFUL WORLD OF COLOR! (Shamelessly copied from my own code)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)

# Sizes of Board Shtuff
width = 80
height = 80
cell_size = 6
spacing = 1

# Setup the Window etc
screen_width = int((width)*(cell_size+spacing))
screen_height = int((height)*(cell_size+spacing))
pygame.init()
font = pygame.font.SysFont('Calibri', 12, False, False)
# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Diseases")
clock = pygame.time.Clock()
done = False

def drawBoard(A):
    for row in range(height):
        x_pos = (cell_size + spacing) * row
        for col in range(width):
            y_pos = (cell_size + spacing) * col
            tpz = getType(A, row, col)
            if tpz == "O":
                pygame.draw.rect(screen, GREEN, [x_pos,y_pos,cell_size,cell_size])
            elif tpz == "I":
                pygame.draw.rect(screen, RED, [x_pos,y_pos,cell_size,cell_size])
            elif tpz == "D":
                pygame.draw.rect(screen, GRAY, [x_pos,y_pos,cell_size,cell_size])
            elif tpz == "C":
                pygame.draw.rect(screen, CYAN, [x_pos,y_pos,cell_size,cell_size])
            elif tpz == "V":
                pygame.draw.rect(screen, WHITE, [x_pos,y_pos,cell_size,cell_size])

board = vaxedBoard(.5, width, height)

flu = disease(.7, .41, (1.2/100000), .2, 3)
ebola = disease(.6, .7, .5, .5, 3)
test = disease(.75, .3, 0, .2, 4)

generation = 0
pzerrow = random.choice(range(0, len(board)))
pzercol = random.choice(range(0, len(board[0])))
board[pzerrow][pzercol].infect(test.contagtime)
drawBoard(board)
pygame.display.flip()
# -------- Main Program Loop ----------
while not done and generation < 10000000:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    generation += 1
    board = oneStep(board, test)
    drawBoard(board)
    pygame.display.flip()