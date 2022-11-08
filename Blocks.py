import pygame

class Circle():
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 60
        self.width = 60

    def display(self):
        pygame.draw.circle(self.screen, 'white',(self.x,self.y),self.size,self.width)
        self.screen.update()
    def update(self,x_shift):
        self.circle.x += x_shift