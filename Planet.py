import pygame
from os import walk
class Planet(pygame.sprite.Sprite): #constructs all planets
    def __init__(self,screen,pos,imageString): #sets up position and image of planet
        self.image = pygame.transform.scale(pygame.image.load(imageString), (60, 60))
        self.rect = self.image.get_rect(center=(pos.x,pos.y))
        self.position = pygame.math.Vector2(pos.x, pos.y)
        self.screen = screen
        self.position = pos
        self.mask = pygame.mask.from_surface(self.image)
    def display(self): #displays the planets
        self.screen.blit(self.image,self.rect)