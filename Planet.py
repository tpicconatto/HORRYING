import pygame
from os import walk
class Planet():
    #def __init__(self,screen,x,y):
        #self.image = pygame.transform.scale(pygame.image.load('pixil-frame-0(1).png'), (60, 60))
        #self.x = x
        #self.screen = screen
        #self.y = y
    #def display(self):
        #self.screen.blit(self.image, new_rect)
    def __init__(self,screen, pos):
        super().__init__()
        self.screen = screen
        self.position = pos
        self.size = 60
        self.width = 20
    def display(self):
        pygame.draw.circle(self.screen, 'white',(self.position.x+self.size,self.position.y+self.size),self.size,self.width)

    def update(self,x_shift):
        self.position.x += x_shift
class Earth:
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