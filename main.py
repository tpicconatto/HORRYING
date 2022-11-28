# import the pygame module, so you can use it
import pygame
from player import Player1
from player import Player2
from level import Level
from pygame import mixer
# initialize the pygame module


pygame.init()

display_width = 1200
display_height = 800

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("HORRIFYING")

clock = pygame.time.Clock()

level1 = Level(1,display)

player1 = Player1(800, 20, 0)
player2 = Player2(100, 20, 0)

level1.player1Ref = player1
level1.player2Ref = player2

player1.levelReference = level1
player2.levelReference = level1

mixer.init()
mixer.music.load('Assets/Enigma-Long-Version-Complete-Version.mp3')
mixer.music.set_volume(0.9)
mixer.music.play()

counter, text = 3, '3'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
#draws
def drawObj(disp, image, topleft, angle):
    # idk how this works but it does
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    disp.blit(rotated_image, new_rect)

level1 = Level(1,display)

running = True
lookingatcontrol = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Go!'
            if counter>0:
                player1.stopComplete()
                player2.stopComplete()
            elif counter<0:
                text=""
                player1.stopCom = False
                player2.stopCom = False

#manages the control screen
        while lookingatcontrol:
            keys = pygame.key.get_pressed()
            font = pygame.font.Font('freesansbold.ttf', 32)
            textP1 = font.render('Player 1 control: arrows', True, 'green', 'blue')
            textP2 = font.render('Player 2 control: WASD', True, 'green', 'blue')
            textCon = font.render('Press any key to play', True, 'green', 'blue')
            textRectP1 = textP1.get_rect()
            textRectP2 = textP2.get_rect()
            textRectCon = textCon.get_rect()
            textRectP1.center = (display_width // 2, display_height // 2)
            textRectP2.center = (display_width // 2, display_height // 2 +32)
            textRectCon.center = (display_width // 2, display_height // 2 + 64)
            display.fill('black')
            display.blit(textP1, textRectP1)
            display.blit(textP2, textRectP2)
            display.blit(textCon, textRectCon)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    lookingatcontrol = False


    display.fill('black')
    level1.level1()

    if player1.position.x >= display_width-50 or player1.position.y >= display_height-70:
        player1.stop()
    if player1.position.x<= 0 or player1.position.y <=50:
        player1.stop()
    if player2.position.x >= display_width - 50 or player2.position.y >= display_height-70:
        player2.stop()
    if player2.position.x<= 0 or player2.position.y <= 50:
        player2.stop()

    # check collision:
    player1.checkCollision()
    player2.checkCollision()


    player1.changeImage()
    player2.changeImage()

    # draw with proper position and rotation
    drawObj(display, player1.image, player1.position, player1.rotation)
    drawObj(display, player2.image, player2.position, player2.rotation)
    player1.update()
    player2.update()

    pygame.display.update()

    clock.tick(60)



