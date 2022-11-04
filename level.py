import pygame
from Blocks import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setUpLevel(level_data)
    def setUpLevel(self,layout):
        self.tiles = pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for columnIndex, column in enumerate(row):
                if column == 'x':
                    x = columnIndex * tile_size
                    y = rowIndex * tile_size
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(-1)
        self.tiles.draw(self.display_surface)