import pygame

class SpriteSheet():
    def __init__(self,image,width,height):
        self.width = width
        self.height = height
        self.image = image

    def get(self,x,y):
        self.rect = pygame.rect.Rect(x * self.width,y * self.height,self.width,self.height)
        return self.image.subsurface(self.rect)