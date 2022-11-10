import pygame
import math

PI = 3.141592653589793238462

class Player(pygame.sprite.Sprite):
    def __init__ (self, x, y, rot):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('pygameImg.png'), (200,200))
        self.rect = self.image.get_rect(center = (x,y))
        self.position = pygame.math.Vector2(x,y)
        self.rotation = rot # deg
        self.scale = pygame.math.Vector2(1, 1)

        self.rotSpeed = 2.5  # deg/s
        self.rotDir = 0 # input control var

        self.velocity = pygame.math.Vector2(0,0)
        self.thrustAcceleration = .5
        self.thrust = 0 # input control var

        self.dragCoef = .975


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

    def update(self):
        self.get_input()
        #self.rect.x += self.direction.x * self.speed
        self.rotation += self.rotDir * self.rotSpeed

        self.velocity.x += self.thrust * self.thrustAcceleration * math.cos((self.rotation+90) * PI/180.0)
        self.velocity.y += self.thrust * self.thrustAcceleration * math.sin((self.rotation-90) * PI/180.0)

        self.velocity *= self.dragCoef

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
    def stop(self):
        self.velocity = 0
