import pygame
import math

PI = 3.141592653589793238462
GCONST = 0.000000000066743

# 1 PIXEL = 106301.667 meters

class Player(pygame.sprite.Sprite): #creates general player class
    def __init__ (self, x, y, rot, levelRef): #defines variables that are needed later
        super().__init__()
        self.image = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Assets/SpaceShip.png'), 90), (50, 50))
        self.rect = self.image.get_rect(center = (x,y))
        self.position = pygame.math.Vector2(x,y)
        self.rotation = rot # deg
        self.scale = pygame.math.Vector2(1, 1)

        self.levelReference = levelRef

        self.rotSpeed = 2.5  # deg/s
        self.rotDir = 0 # input control var

        self.acceleration = pygame.math.Vector2(0,0)
        self.velocity = pygame.math.Vector2(0,0)
        self.thrustAcceleration = 50 # the acceleration added by the rocket
        self.thrust = 1 # input control var

        self.dragCoef = .998
        self.accelerationOfBody = 3
        self.stopCom = False
        self.gameOver = False
        self.checkCollisionRunning = True

    def update(self): #Updates the position of the player based on user input
        self.get_input()
        self.rotation += self.rotDir * self.rotSpeed

        if self.stopCom == False: #if completeStop isn't called
        # add acceleration of rocket if thrusting
            self.acceleration.x = .005 * self.thrust * self.thrustAcceleration * math.cos((self.rotation+90) * PI/180.0)
            self.acceleration.y = .005 * self.thrust * self.thrustAcceleration * math.sin((self.rotation-90) * PI/180.0)

        #***************
        # accleration of gravity
            for b in self.levelReference.bodiesList: #array of all the planets
                distVector = b.position - self.position
                distance = distVector.length() #* 106301.667 # in meters

                accelVector = distVector.normalize() * (self.accelerationOfBody / math.pow(distance, .2))
                self.acceleration += accelVector * .06
        #*************

            self.velocity.x += self.acceleration.x
            self.velocity.y += self.acceleration.y

            if self.velocity.length() > 10: #so that velocity never exceeds 10
                self.velocity.scale_to_length(10)

            self.velocity *= self.dragCoef

            self.position.x += self.velocity.x
            self.position.y += self.velocity.y

            self.rect.topleft = self.position.x, self.position.y



    def changeImage(self, image): #changes the image to the parameter
        self.image = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load(image), 90), (50, 50))

    def stop(self): #sets player velocity to zero slowing them down (used when player hits the edge)
        self.velocity = pygame.math.Vector2(0, 0)

    def stopComplete(self): #only allows players to rotate (used during countdown)
        self.velocity = pygame.math.Vector2(0, 0)
        self.stopCom = True


    def game_over(self): #handles what happens after collision and "explodes" the player
        self.stopComplete()
        self.levelReference.explosionRef.position = self.position
        self.levelReference.explosionRef.imageIndex = 0
        self.checkCollisionRunning = False
        self.image = pygame.image.load("Assets/transparent.png")
        self.gameOver = True





class Player1(Player): #defined class for player1
    def __init__(self,x,y,rot, levelRef): #includes same paramaters as Player
        super().__init__(x,y,rot,levelRef)

    def get_input(self): #sets player1 keys as arrows
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: #right arrow rotate right
            self.rotDir = -1
        elif keys[pygame.K_LEFT]: #left arrow rotate left
            self.rotDir = 1
        else: #if neither pressed don't rotate
            self.rotDir = 0

        if keys[pygame.K_UP]: #up arrow thurst forward
            self.thrust = 1
        else: #no up don't thrust
            self.thrust = 0

    def checkCollision(self): #checks the players for collisions
        if self.checkCollisionRunning == True: #should be checking collisions

            #**********
            # Determines is player1 has collided with a planet
            for b in self.levelReference.bodiesList: #runs through planets in level
                if pygame.sprite.collide_mask(self, b) != None: #collided with a planet thus kills the player
                    self.game_over()
                    self.levelReference.player2Score += 1
                    return True
            #**********

            #*********
            # Determines and handles if players collide
            if self.levelReference.player2Ref.checkCollisionRunning == True: #suppose to be checking collisions
                if pygame.sprite.collide_mask(self, self.levelReference.player2Ref) != None: #they collided
                    if self.velocity.magnitude() > self.levelReference.player2Ref.velocity.magnitude(): #player1 was moving faster and scores a point
                        self.levelReference.player2Ref.game_over()
                        self.levelReference.player1Score +=1
                        return True
                    if self.velocity.magnitude() < self.levelReference.player2Ref.velocity.magnitude(): #player2 was moving faster and scores a point
                        self.game_over()
                        self.levelReference.player2Score +=1
                        return True
            #*****************

class Player2(Player): #defines player two
    def __init__(self,x,y,rot,levelRef): #contains same parameters as Player
        super().__init__(x,y,rot,levelRef)


    def get_input(self): #sets player1 keys as WAS
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]: #pressed d rotate right
            self.rotDir = -1
        elif keys[pygame.K_a]: #pressed a rotate left
            self.rotDir = 1
        else: #didn't press rotate don't rotate
            self.rotDir = 0

        if keys[pygame.K_w]: #pressed w thrust forward
            self.thrust = 1
        else: #did not thrust don't thrust
            self.thrust = 0

    def checkCollision(self): #check if player 2 is colliding with any planets
        if self.checkCollisionRunning == True: #should be checking collision
            for b in self.levelReference.bodiesList: #runs through all the planets
                if pygame.sprite.collide_mask(self, b) != None: #collided with planet thus kills the player
                    self.game_over()
                    self.levelReference.player1Score += 1
                    return True