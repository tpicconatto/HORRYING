import pygame

class Circle():
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 60
        self.width = 20

    def display(self):
        pygame.draw.circle(self.screen, 'white',(self.x,self.y),self.size,self.width)

    def update(self,x_shift):
        self.x += x_shift