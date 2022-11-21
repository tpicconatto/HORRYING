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
class SandPlanet(Planet):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.image = pygame.transform.scale(pygame.image.load('Assets/DesertPlanet.png'), (60, 60))
        self.rect = self.image.get_rect(center=(pos.x, pos.y))
