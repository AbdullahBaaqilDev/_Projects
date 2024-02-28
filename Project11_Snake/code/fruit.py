import pygame
from pygame.math import Vector2 as Vec
from random import choice
from settings import *

class Fruit(pygame.sprite.Sprite):
    loaded_fruit_types = []

    def __init__(self, fruit_type, empty_squares, groups):
        super().__init__(groups)

        self.original_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\fruits\\{fruit_type}.png")
        self.image = pygame.transform.scale(self.original_image,(SQUARE_SIZE,SQUARE_SIZE))
        Fruit.loaded_fruit_types.append({"type": fruit_type, "image": self.original_image})
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = Vec(0,0)
        self.reposition(empty_squares)

        self.size_change_value = 0.003
        self.size = 0.3
        self.max_size = 0.4
        self.min_size = 0.2
    
    def change_type(self, new_type):
        if new_type not in [fruit_type["type"] for fruit_type in Fruit.loaded_fruit_types]:
            self.original_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\fruits\\{new_type}.png")
            self.image = pygame.transform.scale(self.original_image,(SQUARE_SIZE,SQUARE_SIZE))
            Fruit.loaded_fruit_types.append({"type": new_type, "image": self.original_image})
        else:
            for fruit_type in Fruit.loaded_fruit_types:
                if fruit_type["type"] == new_type:
                    self.original_image = fruit_type["image"]
                    self.image = pygame.transform.scale(self.original_image,(SQUARE_SIZE,SQUARE_SIZE))
    
    def reposition(self, empty_squares):
        self.pos = choice(empty_squares)
        self.rect.center = self.pos * SQUARE_SIZE + Vec(SQUARE_SIZE//2,SQUARE_SIZE//2)
    
    def update(self):
        self.size += self.size_change_value
        if self.size >= self.max_size or self.size <= self.min_size: self.size_change_value *= -1
        self.image = pygame.transform.scale_by(self.original_image,self.size)
        self.rect = self.image.get_rect(center = self.rect.center)