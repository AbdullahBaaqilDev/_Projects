import pygame
import random
from settings import *

class Food(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pos
        self.body_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.border_color = (0,0,0)
        self.size = random.randint(FOOD_SIZE_RANGE[0],FOOD_SIZE_RANGE[1])
        self.rect = pygame.Rect(pos[0],pos[1],self.size*2,self.size*2)