# import the pygame module, so you can use it
import pygame
# initialize the pygame module
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
ACC = 0.5
FRIC = -0.12
FPS = 60

HEIGHT = 500
WIDTH = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HORRIFYING")
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


