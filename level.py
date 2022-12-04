from Planet import Planet
# from Planet import Earth
import pygame


class Level(): #Creates the level
    def __init__(self, number, screen): #defines variables that are needed elsewhere
        self.number = number
        self.screen = screen
        self.bodiesList = [] #where all the planets are stored
        #******
        # used to keep track of collisions
        self.player1Ref = None
        self.player2Ref = None
        #*********

        self.explosionRef = None

        self.player1Score = 0
        self.player2Score = 0

        if self.number == 1: #makes this level be level 1
            self.level1()
        elif self.number == 2: #makes this level be level 2
            self.level2()
        elif self.number == 3: #makes this level be level 3
            self.level3()
        elif self.number == 4: ##makes this level be level 4
            self.level4()
        elif self.number == 5: #makes this level be level 5
            self.level5()


    def level1(self): #adds level 1 planets to bodieslist
        return True
        #planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        #self.bodiesList.append(planet1)

    def level2(self): #adds level 2 planets to bodieslist
        planet1 = Planet(self.screen, pygame.math.Vector2(300, 500), 'Assets/PurplePlanet.png')
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(900, 300), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet2)


    def level3(self): #adds level 3 planets to bodieslist
        planet1 = Planet(self.screen, pygame.math.Vector2(500, 400), 'Assets/PurplePlanet.png')
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(700, 600), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet2)

        planet3 = Planet(self.screen, pygame.math.Vector2(800, 250), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet3)

    def level4(self): #adds level 4 planets to bodieslist
        planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(750, 300), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet2)

        planet3 = Planet(self.screen, pygame.math.Vector2(800, 600), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet3)

        planet4 = Planet(self.screen, pygame.math.Vector2(200, 300), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet4)



    def level5(self): #adds level 5 planets to bodieslist
        planet1 = Planet(self.screen, pygame.math.Vector2(600, 400), 'Assets/PurplePlanet.png')
        self.bodiesList.append(planet1)

        planet2 = Planet(self.screen, pygame.math.Vector2(100, 100), 'Assets/PurplePlanet.png')
        self.bodiesList.append(planet2)

        planet3 = Planet(self.screen, pygame.math.Vector2(950, 150), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet3)

        planet4 = Planet(self.screen, pygame.math.Vector2(550, 650), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet4)

        planet5 = Planet(self.screen, pygame.math.Vector2(400, 250), 'Assets/DesertPlanet.png')
        self.bodiesList.append(planet5)





    def Score(self, p): #adds a point when someone scores
        if p == 1: #if player 1 scored
            self.player1Score += 1
        if p == 2: #if player 2 scored
            self.player2Score += 1

    def display(self): #displays the level
        for b in self.bodiesList: #cycles through planets in bodiesList and displays them
            b.display()
