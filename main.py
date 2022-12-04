#*************
#Notes on Comenting
#Comments on large chunks of code follow the same format:
# Astericks
# Description
# Code
# Asterick
#*********#
# import the pygame module, so you can use it
import pygame
from player import Player1
from player import Player2
from level import Level
from pygame import mixer
from Explosion import Explosion
import time



pygame.init()

#*********
#initalizes the screen
display_width = 1200
display_height = 800

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("HORRIFYING")

clock = pygame.time.Clock()
#************

#********
# Creates players and level
levelReference = Level(1,display)
player1 = Player1(50, 700, 0, levelReference)
player1.stopComplete()
player2 = Player2(1150, 700, 0, levelReference)
player2.stopComplete()
levelReference.player1Ref = player1
levelReference.player2Ref = player2
explosion1 = Explosion(display, pygame.math.Vector2(600, 400))
levelReference.explosionRef = explosion1
#*******

#*******
# Creates and plays music
mixer.init()
mixer.music.load('Assets/Enigma-Long-Version-Complete-Version.mp3')
mixer.music.set_volume(0.9)
mixer.music.play()
#**********

#********
#creates timer
counter, text = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
#********

#*********
# Draws and opbect on the screen
def drawObj(disp, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    disp.blit(rotated_image, new_rect)
#************

running = True
lookingAtControl = True
findingLevel = True
slowDown = 0

#Runs the program
while running:
    for event in pygame.event.get(): #looks at user events
        if event.type == pygame.QUIT: #if user clicks out of the program
            running = False
        if event.type == pygame.USEREVENT: #creates counter for when players enter game
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Go!'
            if counter>0: #if counter >0 players cannot move
                player1.stopComplete()
                player2.stopComplete()
            elif counter<0: #once counter if less than zero the can move
                text=""
                player1.stopCom = False
                player2.stopCom = False

    #******************
    # Displays level select screen
    # Allows players to select which level they want to play
        while(findingLevel):
            display.fill('black')
            keys = pygame.key.get_pressed()
            font = pygame.font.Font('freesansbold.ttf', 32)
            textl1 = font.render('Level 1', True, 'green', 'blue')
            textl2 = font.render('Level 2', True, 'green', 'blue')
            textl3 = font.render('Level 3', True, 'green', 'blue')
            textl4 = font.render('Level 4', True, 'green', 'blue')
            textl5 = font.render('Level 5', True, 'green', 'blue')
            textRectl1 = textl1.get_rect()
            textRectl2 = textl2.get_rect()
            textRectl3 = textl3.get_rect()
            textRectl4 = textl4.get_rect()
            textRectl5 = textl5.get_rect()
            textRectl1.center = (display_width // 2, display_height // 2)
            textRectl2.center = (display_width // 2, display_height // 2 + 32)
            textRectl3.center = (display_width // 2, display_height // 2 + 64)
            textRectl4.center = (display_width // 2, display_height // 2 + 96)
            textRectl5.center = (display_width // 2, display_height // 2 + 128)
            display.fill('black')
            display.blit(textl1, textRectl1)
            display.blit(textl2, textRectl2)
            display.blit(textl3, textRectl3)
            display.blit(textl4, textRectl4)
            display.blit(textl5, textRectl5)
            pygame.display.update()
            for event in pygame.event.get(): #filters to see if user selected level
                if event.type == pygame.MOUSEBUTTONUP: #player click on a level
                    pos = pygame.mouse.get_pos()
                    levelnum = 0
                    if pygame.Rect.collidepoint(textRectl1,pos): #choose level 1
                        levelnum = 1
                        levelReference = Level(levelnum,display)
                        player1.levelReference = levelReference
                        player1.stopComplete()
                        player2.levelReference = levelReference
                        player2.stopComplete()
                        levelReference.player1Ref = player1
                        levelReference.player2Ref = player2
                        levelReference.explosionRef = explosion1
                        findingLevel = False
                        lookingAtControl = True
                    if pygame.Rect.collidepoint(textRectl2, pos): #chose level 2
                        levelnum = 2
                        levelReference = Level(levelnum, display)
                        player1.levelReference = levelReference
                        player1.stopComplete()
                        player2.levelReference = levelReference
                        player2.stopComplete()
                        levelReference.player1Ref = player1
                        levelReference.player2Ref = player2
                        levelReference.explosionRef = explosion1
                        findingLevel = False
                        lookingAtControl = True
                    if pygame.Rect.collidepoint(textRectl3,pos): #chose level 3
                        levelnum =3
                        levelReference = Level(levelnum, display)
                        player1.levelReference = levelReference
                        player1.stopComplete()
                        player2.levelReference = levelReference
                        player2.stopComplete()
                        levelReference.player1Ref = player1
                        levelReference.player2Ref = player2
                        levelReference.explosionRef = explosion1
                        findingLevel = False
                        lookingAtControl = True
                    if pygame.Rect.collidepoint(textRectl4,pos): #chose level 4
                        levelnum = 4
                        levelReference = Level(levelnum, display)
                        player1.levelReference = levelReference
                        player1.stopComplete()
                        player2.levelReference = levelReference
                        player2.stopComplete()
                        levelReference.player1Ref = player1
                        levelReference.player2Ref = player2
                        levelReference.explosionRef = explosion1
                        findingLevel = False
                        lookingAtControl = True
                    if pygame.Rect.collidepoint(textRectl5,pos): #chose level 5
                        levelnum = 5
                        levelReference = Level(levelnum, display)
                        player1.levelReference = levelReference
                        player1.stopComplete()
                        player2.levelReference = levelReference
                        player2.stopComplete()
                        levelReference.player1Ref = player1
                        levelReference.player2Ref = player2
                        levelReference.explosionRef = explosion1
                        findingLevel = False
                        lookingAtControl = True
                    else: #keep running if chose nothing
                        continue
                #************

    #********************
    # Manages the Instructions/Controls Screen
        while lookingAtControl: #while reading controls
            keys = pygame.key.get_pressed()
            font = pygame.font.Font('freesansbold.ttf', 32)
            textP1 = font.render('Player 1 control(left): arrows', True, 'green', 'blue')
            textP2 = font.render('Player 2 control(right): WASD', True, 'green', 'blue')
            textCon = font.render('Press any key to Play', True, 'green', 'blue')
            textInstructions = font.render('Avoid Planets and Other Players', True, 'green', 'blue')
            textRectP1 = textP1.get_rect()
            textRectP2 = textP2.get_rect()
            textRectCon = textCon.get_rect()
            textRectInst = textInstructions.get_rect()
            textRectP1.center = (display_width // 2, display_height // 2)
            textRectP2.center = (display_width // 2, display_height // 2 +32)
            textRectCon.center = (display_width // 2, display_height // 2 + 96)
            textRectInst.center = (display_width // 2, display_height // 2 + 64)
            display.fill('black')
            display.blit(textP1, textRectP1)
            display.blit(textP2, textRectP2)
            display.blit(textCon, textRectCon)
            display.blit(textInstructions, textRectInst)
            pygame.display.update()
            for event in pygame.event.get(): #if any button is pressed
                if event.type == pygame.KEYUP:
                    lookingAtControl = False
        #*************

    #***********
    # Displays level score and player to the screen
    display.fill('black')
    display.blit(font.render(text, True,'white', (0, 0, 0)), (600, 300))
    levelReference.display()
    p1score = levelReference.player1Score
    p2score = levelReference.player2Score
    textScore = font.render(str(p1score)+" - "+str(p2score), True, 'white')
    textRectScore = textScore.get_rect()
    textRectScore.center = (display_width // 2, 50)
    display.blit(textScore, textRectScore)
    #*************



    #*********
    # Restricts player movement if they are near the edge
    if player1.position.x >= display_width-50 or player1.position.y >= display_height-70: #when p1 on horizontal edges
        player1.stop()
    if player1.position.x<= 0 or player1.position.y <= 0: #when p1 on vertical edges
        player1.stop()
    if player2.position.x >= display_width - 50 or player2.position.y >= display_height-70: #when p2 on horizontal edges
        player2.stop()
    if player2.position.x<= 0 or player2.position.y <= 0: #when p2 is on vertical edges
        player2.stop()
    #*********

    # check collision:
    player1.checkCollision()
    player2.checkCollision()


    #******
    # Makes the player disapear after its collides with something
    if player1.gameOver == True: #for player one
        player1.changeImage('Assets/transparent.png')
    else: #allows other player to continue unchange
        if player1.thrust != 0: #thrusting
            player1.changeImage('Assets/MovingSpaceShip.png')
        else: #not thrusting
            player1.changeImage('Assets/SpaceShip.png')


    if player2.gameOver == True: #for player two
        player2.changeImage('Assets/transparent.png')
    else: #allows other player to continue unchange
        if player2.thrust != 0: #thrusting
            player2.changeImage('Assets/MovingSpaceShip.png')
        else: #not thrusting
            player2.changeImage('Assets/SpaceShip.png')
    #***********

    #**********
    # Displays an explosion animation
    if player1.gameOver == True: #for player one
        explosion1.display()

    if player2.gameOver == True: #for player two
        explosion1.display()
    #**********

    #*********
    # Draws and updates the players
    drawObj(display, player1.image, player1.position, player1.rotation)
    drawObj(display, player2.image, player2.position, player2.rotation)
    player1.update()
    player2.update()
    #***********

    #**********
    # Resets the players to starting point after they collide
    if (player1.gameOver == True or player2.gameOver == True) and levelReference.explosionRef.imageIndex>=10: #somebody collided with something and exploded
        player1 = Player1(50, 700, 0, levelReference)
        player1.stopComplete()
        player2 = Player2(1150, 700, 0, levelReference)
        player2.stopComplete()
        levelReference.player1Ref = player1
        levelReference.player2Ref = player2
        player1.gameOver = False
        player2.gameOver = False
        counter = 3
        text = str(counter).rjust(3) if counter > 0 else 'Go!'
        player1.checkCollisionRunning = True
        player2.checkCollisionRunning = True
    #*************

    #************
    # Displays end screen once one player scores more than five points
    if levelReference.player1Score >= 5 or levelReference.player2Score >=5: #someone has five points
        levelEnded = True
        while (levelEnded): #displays end screen
            keys = pygame.key.get_pressed()
            font = pygame.font.Font('freesansbold.ttf', 32)
            winFont = pygame.font.Font('freesansbold.ttf', 50)
            if levelReference.player1Score > levelReference.player2Score: #determines if player 1 won and changes text accordingly
                textWin = winFont.render('Player 1 Wins', True, 'green', 'blue')
            else: #determines if player2 one and changes text accordingly
                textWin = textWin = winFont.render('Player 2 Wins', True, 'green', 'blue')
            textPlayAgain = font.render('Play New Level', True, 'green', 'blue')
            textQuit = font.render('Quit', True, 'green', 'blue')
            textRectWin = textWin.get_rect()
            textRectPlayAgain = textPlayAgain.get_rect()
            textRectQuit = textQuit.get_rect()
            textRectWin.center = (display_width // 2, display_height // 2)
            textRectPlayAgain.center = (display_width // 2 - 90, display_height // 2 + 70)
            textRectQuit.center = (display_width // 2 + 90, display_height // 2 + 70)
            display.fill('black')
            display.blit(textWin, textRectWin)
            display.blit(textPlayAgain, textRectPlayAgain)
            display.blit(textQuit, textRectQuit)
            pygame.display.update()
            for event in pygame.event.get(): #looks to see if user did anything
                if event.type == pygame.MOUSEBUTTONUP: #if user clicks with mouse determines what they selected
                    pos = pygame.mouse.get_pos()
                    print("mouse pushes")
                    if pygame.Rect.collidepoint(textRectPlayAgain, pos): #user chose play again. brings them back to level select
                        print("hit play again")
                        levelReference.player1Score = 0
                        levelReference.player2Score = 0
                        findingLevel = True
                        levelEnded = False
                        display.fill('black')
                    if pygame.Rect.collidepoint(textRectQuit, pos): #user chose to quit. quits
                        running = False
                        levelEnded = False
                    else: #user didn't chose anything keep displaying endscreen
                        continue
                #*************



    # draw with proper position and rotation

    pygame.display.update()

    clock.tick(60)



