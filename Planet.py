import pygame
from os import walk
class Planet(pygame.sprite.Sprite):
    def __init__(self,screen,pos):
        self.image = pygame.transform.scale(pygame.image.load('Assets/PurplePlanet.png'), (60, 60))
        self.rect = self.image.get_rect(center=(pos.x,pos.y))
        self.screen = screen
    def display(self):
        self.screen.blit(self.image,self.rect)
    #def __init__(self,screen, pos):
        #super().__init__()
        #self.screen = screen
        #self.position = pos
        #self.size = 60
        #self.width = 20
    #def display(self):
        #pygame.draw.circle(self.screen, 'white',(self.position.x+self.size,self.position.y+self.size),self.size,self.width)

    #def update(self,x_shift):
        #self.position.x += x_shift
class SandPlanet:
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 60
        self.width = 20


    def display(self):
        pygame.draw.circle(self.screen, 'green',(self.x,self.y),self.size,self.width)

    def update(self,x_shift):
        self.x += x_shift

    # Class enemySpaceShips(pygame.sprite.Sprite):
    # def __init__(self,screen,x,y):
    # super().self.image = pygame.Surface((32,64))
    # self.image.fill('grey')
    # self.rect = self.image.get_rect(topleft = pos)
    # self.direction = pygame.math.Vector2(0,0)
    # self.speed = 3