import pygame
import random
from settings import *
from snake import *
from fruit import *
from debug import *

class Board():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.fruits_group = pygame.sprite.Group()
        self.eat_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\assets\\sounds\\eat.wav")
        self.score = 0
        self.player = Snake()
        for _ in range(FRUITS_SPAWN):
            fruit = Fruit()
            self.fruits_group.add(fruit)

    def draw_squares(self):
        for row in range(BOARD_SIZE[0]):
            for col in range(BOARD_SIZE[1]):
                square_rect = pygame.Rect(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.display_surface,DARK,square_rect)
                else:
                    pygame.draw.rect(self.display_surface,LIGHT,square_rect)

    def collisions(self):
        for fruit in self.fruits_group.sprites():
            if fruit.pos == self.player.body[0]:
                self.eat_sound.play()
                fruit.reposition()
                self.score += 1
    
    def draw_fruits(self):
        for fruit in self.fruits_group.sprites():
            fruit.draw()

    def update(self):
        self.collisions()
        self.draw_squares()
        self.draw_fruits()
        self.player.update()