import pygame

class SpriteSheet():
    def __init__(self,image,x,y,width,height):
        self.rect = pygame.rect.Rect(x,y,width,height)
        self.image = image.subsurface(self.rect)
    def get(self):
        return self.image