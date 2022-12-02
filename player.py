import pygame
import math

PI = 3.141592653589793238462
GCONST = 0.000000000066743

# 1 PIXEL = 106301.667 meters

class Player(pygame.sprite.Sprite):
    def __init__ (self, x, y, rot, levelRef):
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

        self.dragCoef = 1
        self.accelerationOfBody = 3
        self.stopCom = False
        self.gameOver = False
        self.checkCollisionRunning = True

    def update(self):
        self.get_input()
        self.rotation += self.rotDir * self.rotSpeed

        if self.stopCom == False:
        # add acceleration of rocket
            self.acceleration.x = .005 * self.thrust * self.thrustAcceleration * math.cos((self.rotation+90) * PI/180.0)
            self.acceleration.y = .005 * self.thrust * self.thrustAcceleration * math.sin((self.rotation-90) * PI/180.0)

        # accleration of gravity
            for b in self.levelReference.bodiesList:
                distVector = b.position - self.position
                distance = distVector.length() #* 106301.667 # in meters

                accelVector = distVector.normalize() * (self.accelerationOfBody / math.pow(distance, .2))
                self.acceleration += accelVector * .06

            #M = 59721900000000000000000
            #accelerationOfBody = (GCONST * M) / (distance*distance) # m/s^2
            #print(accelerationOfBody)
            #accelVector = distVector.normalize() * accelerationOfBody
            #self.acceleration += accelVector * .06

            self.velocity.x += self.acceleration.x
            self.velocity.y += self.acceleration.y

            if self.velocity.length() > 10:
                self.velocity.scale_to_length(10)

            self.velocity *= self.dragCoef

            self.position.x += self.velocity.x
            self.position.y += self.velocity.y

            self.rect.topleft = self.position.x, self.position.y



    def changeImage(self, image):
        self.image = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load(image), 90), (50, 50))

    def stop(self):
        self.velocity = pygame.math.Vector2(0, 0)

    def stopComplete(self):
        self.velocity = pygame.math.Vector2(0, 0)
        self.stopCom = True


    def game_over(self):
        self.stopComplete()
        print("collided")
        self.levelReference.explosionRef.position = self.position
        self.levelReference.explosionRef.imageIndex = 0
        self.checkCollisionRunning = False
        self.image = pygame.image.load("Assets/transparent.png")
        self.gameOver = True



        #self.levelReference.player1Ref.velocity = pygame.math.Vector2(0, 0)
        #self.levelReference.player1Ref.thrustAcceleration = 0
        #self.levelReference.player1Ref.accelerationOfBody = 0
        #self.levelReference.player1Ref.acceleration = pygame.math.Vector2(0, 0)
        #self.levelReference.player2Ref.velocity = pygame.math.Vector2(0, 0)
        #self.levelReference.player2Ref.thrustAcceleration = 0
        #self.levelReference.player2Ref.accelerationOfBody = 0
        #self.levelReference.player2Ref.acceleration = pygame.math.Vector2(0, 0)




class Player1(Player):
    def __init__(self,x,y,rot, levelRef):
        super().__init__(x,y,rot,levelRef)
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rotDir = -1
        elif keys[pygame.K_LEFT]:
            self.rotDir = 1
        else:
            self.rotDir = 0

        if keys[pygame.K_UP]:
            self.thrust = 1
        else:
            self.thrust = 0

    def checkCollision(self):
        if self.checkCollisionRunning == True:

            for b in self.levelReference.bodiesList:
                if pygame.sprite.collide_mask(self, b) != None:
                    #return None
                    print(" ")
                    self.game_over()
                    self.levelReference.player2Score += 1
                    return True

            # only for p1:
            if self.levelReference.player2Ref.checkCollisionRunning == True:
                if pygame.sprite.collide_mask(self, self.levelReference.player2Ref) != None:
                    #print("collide player")
                    if self.velocity.magnitude() > self.levelReference.player2Ref.velocity.magnitude():
                        self.levelReference.player2Ref.game_over()
                        self.levelReference.player1Score +=1
                        return True
                    if self.velocity.magnitude() < self.levelReference.player2Ref.velocity.magnitude():
                        self.game_over()
                        self.levelReference.player2Score +=1
                        return True

class Player2(Player):
    def __init__(self,x,y,rot,levelRef):
        super().__init__(x,y,rot,levelRef)


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotDir = -1
        elif keys[pygame.K_a]:
            self.rotDir = 1
        else:
            self.rotDir = 0

        if keys[pygame.K_w]:
            self.thrust = 1
        else:
            self.thrust = 0

    def checkCollision(self):
        if self.checkCollisionRunning == True:
            for b in self.levelReference.bodiesList:
                if pygame.sprite.collide_mask(self, b) != None:
                    self.game_over()
                    self.levelReference.player1Score += 1
                    return True