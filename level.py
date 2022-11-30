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

        self.explosionRef = None

        self.player1Score = 0
        self.player2Score = 0

        if self.number == 1:
            self.level1()
        elif self.number == 2:
            self.level2()
        elif self.number == 3:
            self.level3()
        elif self.number == 4:
            self.level4()
        elif self.number == 5:
            self.level5()


    def level1(self):
        return True
        #planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        #planet1.display()
        #self.bodiesList.append(planet1)

    def level2(self):
        planet1 = Planet(self.screen, pygame.math.Vector2(300, 500), 'Assets/PurplePlanet.png')
        planet1.display()
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(900, 300), 'Assets/DesertPlanet.png')
        planet2.display()
        self.bodiesList.append(planet2)


    def level3(self):
        planet1 = Planet(self.screen, pygame.math.Vector2(500, 400), 'Assets/PurplePlanet.png')
        planet1.display()
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(700, 600), 'Assets/DesertPlanet.png')
        planet2.display()
        self.bodiesList.append(planet2)

        planet3 = Planet(self.screen, pygame.math.Vector2(800, 250), 'Assets/DesertPlanet.png')
        planet3.display()
        self.bodiesList.append(planet3)

    def level4(self):
        planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        planet1.display()
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(750, 300), 'Assets/DesertPlanet.png')
        planet2.display()
        self.bodiesList.append(planet2)

        planet3 = Planet(self.screen, pygame.math.Vector2(800, 600), 'Assets/DesertPlanet.png')
        planet3.display()
        self.bodiesList.append(planet3)

        planet4 = Planet(self.screen, pygame.math.Vector2(200, 300), 'Assets/DesertPlanet.png')
        planet4.display()
        self.bodiesList.append(planet4)



    def level5(self):
        planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        planet1.display()
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(100, 100), 'Assets/PurplePlanet.png')
        planet2.display()
        self.bodiesList.append(planet2)

        planet3 = Planet(self.screen, pygame.math.Vector2(950, 150), 'Assets/DesertPlanet.png')
        planet3.display()
        self.bodiesList.append(planet3)

        planet4 = Planet(self.screen, pygame.math.Vector2(550, 650), 'Assets/DesertPlanet.png')
        planet4.display()
        self.bodiesList.append(planet4)

        planet5 = Planet(self.screen, pygame.math.Vector2(400, 250), 'Assets/DesertPlanet.png')
        planet5.display()
        self.bodiesList.append(planet5)





    def Score(self, p):
        if p == 1:
            self.player1Score += 1
        if p == 2:
            self.player2Score += 1

        if self.player1Score >= 5:
            print("PLAYER 1 WINS")
        elif self.player2Score >= 5:
            print("PLAYER 2 WINS")
