import pygame
from Blocks import Circle
from settings import tile_size
from player import Player
class Level:
    def __init__(self,level_data,surface):
        #level setup
        self.surface = surface
        self.asteroidsList = []
        self.setUpLevel(level_data)
        self.camera = 0

    #prints out the level and the player
    def setUpLevel(self,layout):
        self.player = pygame.sprite.GroupSingle()
        asteroids = []
        for rowIndex, row in enumerate(layout):
            for columnIndex, column in enumerate(row):
                x = columnIndex * tile_size
                y = rowIndex * tile_size
                if column == 'x':
                    newAsteroid = Circle(self.surface,x,y)
                    asteroids.append(newAsteroid)
                if column == 'p':
                    playerDrawing = Player((x, y))
                    self.player.add(playerDrawing)
        self.asteroidsList = asteroids

    def run(self):
        for i in range(len(self.asteroidsList)):
            self.asteroidsList[i].display()
            self.asteroidsList[i].update(0)

        self.player.update()
        self.player.draw(self.surface)