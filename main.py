# import the pygame module, so you can use it
import pygame
from player import Player
from level import Level
# initialize the pygame module


pygame.init()

display_width = 1200
display_height = 900

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("HORRIFYING")

clock = pygame.time.Clock()


level1 = Level(1,display)
player1 = Player(600, 400, 0, level1)

#draws
def drawObj(disp, image, topleft, angle):
    # idk how this works but it does
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    disp.blit(rotated_image, new_rect)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill('black')
    level1.level1()
    player1.update()
    if player1.position.x >= display_width-50 or player1.position.y >= display_height -50:
        player1.stop()

    # draw with proper position and rotation
    drawObj(display, player1.image, player1.position, player1.rotation)

    pygame.display.update()
    clock.tick(60)


