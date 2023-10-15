import pygame
from pygame.math import Vector2 as Vec
from math import sin
from random import randint
from settings import *

class Fruit(pygame.sprite.Sprite):
    def __init__(self,fruit_type,groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()

        self.original_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\fruits\\{fruit_type}.png")
        self.image = pygame.transform.scale(self.original_image,(SQUARE_SIZE,SQUARE_SIZE))
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = Vec(0,0)
        self.reposition()

        self.size_change_value = 0.003
        self.size = 0.3
        self.max_size = 0.4
        self.min_size = 0.15
    
    def reposition(self):
        random_pos = Vec(randint(0,BOARD_SIZE.x - 1),randint(0,BOARD_SIZE.y - 1))
        self.pos = random_pos
        self.rect.center = random_pos * SQUARE_SIZE + Vec(SQUARE_SIZE//2,SQUARE_SIZE//2)
    
    def update(self):
        self.size += self.size_change_value
        if self.size >= self.max_size or self.size <= self.min_size: self.size_change_value *= -1
        self.image = pygame.transform.scale_by(self.original_image,self.size)
        self.rect = self.image.get_rect(center = self.rect.center)