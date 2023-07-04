import pygame
import random
from pygame.math import Vector2
from settings import *
from spritesheet import *

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.reposition()
        
        fruits_image = pygame.image.load(f"{ASSETS_FOLDER}\\assets\\images\\fruits.png").convert_alpha()
        fruit_width = fruits_image.get_size()[0] // FRUITS_NUMBER
        fruit_height = fruits_image.get_size()[1]
        self.index = FRUITS_DECT[FRUIT_TYPE]
        sprite_sheet = SpriteSheet(fruits_image,self.index*fruit_width,0,fruit_width,fruit_height)
        self.image = pygame.transform.scale(sprite_sheet.get(),(SQUARE_SIZE,SQUARE_SIZE))
        self.rect = self.image.get_rect()
    
    def reposition(self):
        self.pos = Vector2(random.randint(0,BOARD_SIZE[0]-1),random.randint(0,BOARD_SIZE[1]-1))

    def draw(self):
        self.rect = pygame.Rect(self.pos.x * SQUARE_SIZE,self.pos.y * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
        self.display_surface.blit(self.image,self.rect)