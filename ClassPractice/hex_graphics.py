import pygame
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
screen_width = 600
screen_height = 600
width = 8
height = 8
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
            vertices = [(x_pos,y_pos),(x_pos+4*cell_size,y_pos+2*cell_size)\
                ,(x_pos+4*cell_size,y_pos+7*cell_size),(x_pos,y_pos+9*cell_size)\
                ,(x_pos-4*cell_size,y_pos+7*cell_size),(x_pos-4*cell_size,y_pos+2*cell_size)]
            if A.tiles[row][col] == "O":
                pygame.draw.polygon(screen, WHITE, vertices)
            elif A.tiles[row][col] == "W":
                pygame.draw.polygon(screen, BLUE, vertices)
            elif A.tiles[row][col] == "X":
                pygame.draw.polygon(screen, RED, vertices)

done = False

clock = pygame.time.Clock()
board = Board(8)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, BLACK, [0, 0, 1000, 1000])
    mousestats = pygame.mouse.get_pressed()
    mouseloc = pygame.mouse.get_pos()
    drawBoard(board)
    text = font.render(str(mousestats), True, WHITE)
    text2 = font.render(str(mouseloc), True, WHITE)
    screen.blit(text, [300, 300])
    screen.blit(text2, [350, 300])
    pygame.display.flip()



