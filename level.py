from Planet import Planet
#from Planet import Earth
import pygame

class Level():
    def __init__(self,number,screen):
        self.number = number
        self.screen = screen
        self.bodiesList = []
        if self.number == 1:
            self.level1()
    def level1(self):
        planet1= Planet(self.screen, pygame.math.Vector2(600, 400))
        planet1.display()
        self.bodiesList.append(planet1)
        #planet2 = Planet(self.screen, pygame.math.Vector2(100, 500))
        #planet2.display()
        #self.bodiesList.append(planet2)
        #planet3 = Planet(self.screen, 500, 200)
        #planet3.display()
        #planet4 = Planet(self.screen, 1000, 500)
        #planet4.display()
        #earth = Earth(self.screen,1100,700)
        #earth.display()
        #self.bodiesList.append(earth)

