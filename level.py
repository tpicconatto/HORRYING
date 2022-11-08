import pygame
from Blocks import Circle
from settings import tile_size
from player import Player
class Level:
    def __init__(self,level_data,surface):
        #level setup
        self.surface = surface
        self.setUpLevel(level_data)
        self.asteroids = []
        self.camera = 0

    #prints out the level and the player
    def setUpLevel(self,layout):
        self.player = pygame.sprite.GroupSingle()
        self.asteroids = []
        for rowIndex, row in enumerate(layout):
            for columnIndex, column in enumerate(row):
                x = columnIndex * tile_size
                y = rowIndex * tile_size
                if column == 'x':
                    newAsteroid = Circle(self.surface,x,y)
                    self.asteroids.append(newAsteroid)
                if column == 'p':
                    playerDrawing = Player((x, y))
                    self.player.add(playerDrawing)


    def run(self):
        print(len(self.asteroids))
        for i in range(len(self.asteroids)):
            self.asteroids[i].display()
            self.surface.update()

        self.player.update()
        self.player.draw(self.surface)