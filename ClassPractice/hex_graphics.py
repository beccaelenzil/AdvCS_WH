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
screen_width = 1000
screen_height = 1000
pygame.init()
font = pygame.font.SysFont('Calibri', 12, False, False)
# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Segregation")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True







