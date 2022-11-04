import pygame
from Blocks import Tile
from settings import tile_size
from player import Player
class Level:
    def __init__(self,level_data,surface):
        #level setup
        self.display_surface = surface
        self.setUpLevel(level_data)

        self.camera = 0
    def setUpLevel(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for rowIndex, row in enumerate(layout):
            for columnIndex, column in enumerate(row):
                x = columnIndex * tile_size
                y = rowIndex * tile_size
                if column == 'x':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if column == 'p':
                    playerDrawing = Player((x, y))
                    self.player.add(playerDrawing)


    def run(self):
        self.tiles.update(self.camera)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)