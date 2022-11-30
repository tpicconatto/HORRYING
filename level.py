from Planet import Planet
# from Planet import Earth
import pygame


class Level():
    def __init__(self, number, screen):
        self.number = number
        self.screen = screen
        self.bodiesList = []
        self.player1Ref = None
        self.player2Ref = None

        self.player1Score = 0
        self.player2Score = 0

        if self.number == 1:
            self.level1()

    def level1(self):
        planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        planet1.display()
        self.bodiesList.append(planet1)
        planet2 = Planet(self.screen, pygame.math.Vector2(100, 100), 'Assets/PurplePlanet.png')
        planet2.display()
        self.bodiesList.append(planet2)
        planet5 = Planet(self.screen, pygame.math.Vector2(950, 150), 'Assets/DesertPlanet.png')
        planet5.display()
        self.bodiesList.append(planet5)
        planet6 = Planet(self.screen, pygame.math.Vector2(550, 650), 'Assets/DesertPlanet.png')
        planet6.display()
        self.bodiesList.append(planet6)
        planet7 = Planet(self.screen, pygame.math.Vector2(400, 250), 'Assets/DesertPlanet.png')
        planet7.display()
        self.bodiesList.append(planet7)
        # planet4 = Planet(self.screen, 1000, 500)
        # planet4.display()
        # earth = Earth(self.screen,1100,700)
        # earth.display()
        # self.bodiesList.append(earth)






    def Score(self, p):
        if p == 1:
            self.player1Score += 1
        if p == 2:
            self.player2Score += 1

        if self.player1Score >= 5:
            print("PLAYER 1 WINS")
        elif self.player2Score >= 5:
            print("PLAYER 2 WINS")
