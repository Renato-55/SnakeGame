""" -  This is where functions belonging to the
    - skane game menu will belong

Imports
"""

import pygame
from pygame.locals import *

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


# Display the menu of the game snake
def displayMenu(screen):
    while True:

        # Upload the background image to the background menu
        image = pygame.image.load("Imagens/Background/backgroundMenu.jpg")
        screen.blit(image, [0, 0])
        # display the image

        displayMenuText(screen)

        pygame.display.flip()

        # check which key is pressed
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "exit"
                elif event.key == K_p:  # This is the key to play the game
                    return "play"
                elif event.key == K_h:  # This is the key to go to Highscores
                    return "highscores"
                elif event.key == K_i:  # display the instructions
                    return "instructions"
                elif event.key == K_q:  # exit key
                    return "exit"
                elif event.type == QUIT:
                    return "exit"



def displayMenuText(screen):
    opcoes = ["PLAY SNAKE", "HIGHSCORES", "INSTRUCTIONS", "QUIT"]
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("SNAKE GAME", True, white)
    textRect = text.get_rect()
    textRect.center = (400, 100)
    screen.blit(text, textRect)

    for i in range(len(opcoes)):
        text = font.render(opcoes[i], True, green, blue)
        textRect.center = (400, (i * 100) + 300)
        screen.blit(text, textRect)


