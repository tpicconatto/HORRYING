from Planet import Planet
from Planet import SandPlanet
import pygame

class Level():
    def __init__(self,number,screen):
        self.number = number
        self.screen = screen
        self.bodiesList = []
    def level1(self):
        planet1= Planet(self.screen, pygame.math.Vector2(200, 200))
        planet1.display()
        self.bodiesList.append(planet1)
        planet2 = Planet(self.screen, pygame.math.Vector2(100, 500))
        planet2.display()
        self.bodiesList.append(planet2)
        planet3 = SandPlanet(self.screen,pygame.math.Vector2(800, 700) )
        planet3.display()
        #planet4 = Planet(self.screen, 1000, 500)
        #planet4.display()
        #earth = Earth(self.screen,1100,700)
        #earth.display()
        #self.bodiesList.append(earth)

