import pygame
from settings import *

class Square(pygame.sprite.Sprite):
    def __init__(self, is_light, pos, groups):
        super().__init__(groups)
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.is_light = is_light
        self.piece = None
        self.highlighted = "normal"

        self.image = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill(SQUARE_COLORS[is_light]["normal"])
        self.rect = self.image.get_rect(topleft = pos * SQUARE_SIZE)
    
    def is_selected(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed:
                return self
        return None
    
    def highlight(self, highlight_color):
        self.image.fill(SQUARE_COLORS[self.is_light][highlight_color])
    
    def draw(self):
        self.screen.blit(self.image, self.rect)