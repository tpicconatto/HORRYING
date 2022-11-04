# import the pygame module, so you can use it
import pygame
from settings import *
from Blocks import Tile
from level import Level

# initialize the pygame module


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HORRIFYING")
level = Level(level1_map, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)


