""" - Snake Program
Import section
"""
import pygame
from pygame.locals import *
from random import seed, randint
from collections import deque

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
black = (0, 0, 0)


class Snake:

    def __init__(self, x, y):
        self.xSpeed = 0  # initial x Speed
        self.ySpeed = 0  # initial y Speed
        self.x = []
        self.y = []
        self.x.append(x)
        self.y.append(y)
        self.eating = False
        self.score = 0
        self.foodX = 0
        self.foodY = 0
        self.oldX = 0
        self.oldY = 0
        self.generateFood()

    def move(self, dir):

        if dir == "DOWN" and self.ySpeed != -20:
            self.ySpeed = 20
            self.xSpeed = 0
        elif dir == "UP" and self.ySpeed != 20:
            self.ySpeed = -20
            self.xSpeed = 0
        elif dir == "LEFT" and self.xSpeed != 20:
            self.ySpeed = 0
            self.xSpeed = -20
        elif dir == "RIGHT" and self.xSpeed != -20:
            self.ySpeed = 0
            self.xSpeed = 20
        else:
            pass

        self.oldX = self.x[len(self.x) - 1]
        self.oldY = self.y[len(self.y) - 1]

    def drawSnake(self, screen, dir):
        self.eating = False

        if self.x[0] == 200 or self.x[0] == 600:  # if the head is touching the boards
            return "GAME OVER"

        if self.y[0] == 200 or self.y[0] == 600:  # if the head is touching the boards
            return "GAME OVER"

        for i in range(1, len(self.x)):
            if self.x[i] == self.x[0] and self.y[i] == self.y[0]:
                return "GAME OVER"

        if self.x[0] == self.foodX:
            if self.y[0] == self.foodY:
                self.eating = True
                self.x.append(self.oldX)
                self.y.append(self.oldY)
                self.score += 10

        self.move(dir)

        if len(self.x) > 1:
            self.x.pop(len(self.x) - 1)
            self.y.pop(len(self.y) - 1)
            self.x.insert(0, self.x[0] + self.xSpeed)
            self.y.insert(0, self.y[0] + self.ySpeed)
        else:
            self.x[0] += self.xSpeed
            self.y[0] += self.ySpeed

        for i in range(len(self.x)):
            pygame.draw.rect(screen, blue, [self.x[i], self.y[i], 20, 20])
            pygame.display.update()

    def placeFood(self, screen):
        if self.eating:
            self.generateFood()

        self.updateScore(screen)
        pygame.draw.rect(screen, green, [self.foodX, self.foodY, 20, 20])
        pygame.display.update()

    def updateScore(self,screen):
        font = pygame.font.Font("freesansbold.ttf", 16)
        str = f"Score = {self.score} "
        text = font.render(str, True, white)
        textRect = text.get_rect()
        textRect.center = (300, 50)
        screen.blit(text, textRect)

    def generateFood(self):

        while True:
            self.foodX = randint(1, 19) * 20 + 200
            self.foodY = randint(1, 19) * 20 + 200
            if self.foodX not in self.x or self.foodY not in self.y:
                break


snake = Snake(380, 220)


def displayGame(screen):
    direction = "DOWN"
    while True:

        image = pygame.image.load(
            "Imagens/Background/backgroundSnakeGame.jpg")  # Upload the background image to the background menu
        screen.blit(image, [0, 0])  # display the image

        createBoard(screen)

        snake.placeFood(screen)  # display the food on the screen

        if snake.drawSnake(screen, direction) == "GAME OVER":  # draw all the snake
            print("GAME OVER - Gotta work on this")
            return "exit"

        pygame.display.update()  # update the snake and the food if needed

        # check which key is pressed
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "exit"
                elif event.key == K_a:
                    direction = "LEFT"

                elif event.key == K_s:
                    direction = "DOWN"

                elif event.key == K_d:
                    direction = "RIGHT"

                elif event.key == K_w:
                    direction = "UP"

                elif event.type == QUIT:
                    return "exit"

        pygame.time.delay(50)


def createBoard(screen):
    pygame.draw.rect(screen, red, [190, 190, 420, 420])  # screen, color (r,g,b) , [x,y,width,height]
    pygame.draw.rect(screen, black, [200, 200, 400, 400])
