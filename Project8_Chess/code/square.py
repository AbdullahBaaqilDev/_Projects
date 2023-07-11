import pygame
from settings import *

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,name,pos,is_dark):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.piece = None
        self.name = name
        self.pos = pygame.math.Vector2(pos)
        
        self.is_dark = is_dark
        self.highlighted = 0

        self.image = pygame.surface.Surface((SQUARE_SIZE,SQUARE_SIZE))
        self.rect = self.image.get_rect(topleft = (x,y))


    def update_color(self):
        self.image.fill(SQUARES_COLORS_DECT[self.is_dark][self.highlighted])

    def is_selected(self):
        """return if this is selected square"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_left = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos) and mouse_left:
            return self
        else:
            return None

    def update(self):
        self.update_color()