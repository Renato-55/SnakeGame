""" - Instructions
Import section
"""
import pygame
from pygame.locals import *

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

def displayInstructions(screen):
    while True:

        # Upload the background image to the background menu
        image = pygame.image.load("Imagens/Background/backgroundInstructions.jpg")
        screen.blit(image, [0, 0])
        # display the image

        displayInstructionsText(screen)

        pygame.display.flip()

        # check which key is pressed
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "exit"
                elif event.key == K_b:  # This is the key to play the game
                    return "back"
                elif event.key == K_e:  # This is the key to play the game
                    return "exit"
                elif event.type == QUIT:
                    return "exit"


def displayInstructionsText(screen):
    text = "Use the W,A,S,D to move the snake.The objective of the game is to get as many points as you can.Points can be earned by collecting fruits." \
           "You should also avoid hiting the walls and your body ." \
           "Enjoy it." \
           "." \
           "." \
           "." \
           "B - Go Back." \
           "E - Exit the program."
    textList = text.split(".")
    font = pygame.font.Font("freesansbold.ttf", 16)
    text = font.render("Instructions", True, white)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    screen.blit(text, textRect)

    for i in range(len(textList)):
        text = font.render(textList[i], True, green, blue)
        textRect.center = (80, (i * 50) +100)
        screen.blit(text, textRect)

