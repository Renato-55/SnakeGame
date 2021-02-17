""" - Snake Main -- ALL MENUS -- Program
Import section
"""
import pygame
from pygame.locals import *
from menu import *
from instructions import *
from snakeGame import *
from random import seed
seed(a=None, version=2)

op = ""
while op != "exit":
    pygame.init() # inicialize
    pygame.display.set_caption("SNAKE - RENATO BARBOSA")
    screen = pygame.display.set_mode((800,800))

    op = displayMenu(screen)

    if op == "play":
        op = displayGame(screen)
    elif op == "highscore":
        print("Gonna learn data base first")
    elif op == "instructions":
        op = displayInstructions(screen)
    elif op == "exit":
        print("Gonna go out cy@")


pygame.quit()

