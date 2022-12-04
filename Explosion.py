import pygame

class Explosion(pygame.sprite.Sprite): #constructions the explosions

    def __init__(self,screen,pos): #imports all the images needed in proper location
        self.image = pygame.transform.scale(pygame.image.load("Assets/Explosion5.png"), (60, 60))
        self.rect = self.image.get_rect(center=(pos.x,pos.y))
        self.position = pygame.math.Vector2(pos.x, pos.y)
        self.screen = screen
        self.position = pos
        self.counter = 10
        self.imageIndex = 0

        self.exImg1 = pygame.image.load('Assets/Explosion1.png')
        self.exImg2 = pygame.image.load('Assets/Explosion2.png')
        self.exImg3 = pygame.image.load('Assets/Explosion3.png')
        self.exImg4 = pygame.image.load('Assets/Explosion4.png')
        self.exImg5 = pygame.image.load('Assets/Explosion5.png')
        self.exImg6 = pygame.image.load('Assets/Explosion6.png')
        self.exImg7 = pygame.image.load('Assets/Explosion7.png')
        self.exImg8 = pygame.image.load('Assets/Explosion8.png')
        self.exImg9 = pygame.image.load('Assets/Explosion9.png')
        self.exImg10 = pygame.image.load('Assets/Explosion10.png')

        self.explosionImgArray = [self.exImg1, self.exImg2, self.exImg3, self.exImg4, self.exImg5, self.exImg6, self.exImg7,
                                  self.exImg8, self.exImg9, self.exImg10]


    def display(self): #displays the images
        if (self.imageIndex >= 10): #if it has gone through all the images make it transparent
            self.image = pygame.image.load("Assets/transparent.png")
        else: #otherwise filter through explosion animation
            self.image = self.explosionImgArray[self.imageIndex]
            self.imageIndex += 1
        self.rect.topleft = self.position.x, self.position.y

        self.screen.blit(self.image, self.rect)
