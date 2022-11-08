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
        self.playerReference = Player(0)

    #prints out the level and the player
    def setUpLevel(self,layout):
        #self.playerReference = pygame.sprite.GroupSingle()
        asteroids = []
        for rowIndex, row in enumerate(layout):
            for columnIndex, column in enumerate(row):
                x = columnIndex * tile_size
                y = rowIndex * tile_size
                if column == 'x':
                    print("add asteroid")
                    newAsteroid = Circle(self.surface,x,y)
                    asteroids.append(newAsteroid)
                if column == 'p':
                    #playerDrawing = Player((x, y))
                    self.playerReference = Player(pygame.math.Vector2(x,y))
        self.asteroidsList = asteroids

    def run(self):
        for i in range(len(self.asteroidsList)):
            self.asteroidsList[i].display()

        self.playerReference.update()

        #self.playerReference.draw(self.surface)