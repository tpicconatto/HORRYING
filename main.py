# import the pygame module, so you can use it
import pygame
from settings import *
from Blocks import Tile
# initialize the pygame module


#for row_index, row in enumerate(layout):
    #for col_index, cell in enumerate (row):
        #x = col_index * tile_size
        #y = row_index * tile_size
        #if cell == 'X':
            #tile = Tile((x,y),tile_size)
            #self.tiles.add(tile)
#class Ghost(pygame.sprite.Sprite):
    #def __init__(self,width,height,posX,posY,color):
        #super.__init__()
        #self.image = pygame.Surface([width,height])
        #self.image.fill(color)
        #self.rect = self.image.get_rect()


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HORRIFYING")
test_tile = pygame.sprite.Group(Tile((100,100),200))
test_tile.draw(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    test_tile.draw(screen)
    pygame.display.update()
    clock.tick(60)


