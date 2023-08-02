import pygame
from pygame.math import Vector2 as Vec
from random import randint
from spritesheet import SpriteSheet
from settings import *

class Fruit(pygame.sprite.Sprite):
    def __init__(self,fruit_type,groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        sprite_sheet = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\fruits.png")
        self.image: pygame.Surface = pygame.transform.scale(SpriteSheet(
        image = sprite_sheet,
        x = FRUITS_DICT[fruit_type] * sprite_sheet.get_height(),
        y = 0,
        width = sprite_sheet.get_height(),
        height = sprite_sheet.get_height()).get(),(SQUARE_SIZE,SQUARE_SIZE))
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = Vec(0,0)
        self.reposition()
    
    def reposition(self):
        random_pos = Vec(randint(0,BOARD_SIZE.x - 1),randint(0,BOARD_SIZE.y - 1))
        self.pos = random_pos
        self.rect.topleft = random_pos * SQUARE_SIZE

    def draw(self):
        self.display_surface.blit(self.image,self.rect)

    def update(self):
        self.draw()