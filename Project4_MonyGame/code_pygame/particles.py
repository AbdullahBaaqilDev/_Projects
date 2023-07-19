import pygame
from random import randint
from settings import *
 
class Particle(pygame.sprite.Sprite):
    def __init__(self,image,pos,groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.animation_speed = 6
        self.alpha = 255

        self.image = pygame.transform.rotate(image,randint(-45,45))
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.alpha -= self.animation_speed
        if self.alpha <= 1:
            self.kill()

        self.image.set_alpha(self.alpha)
        self.rect.y -= 1

    def draw(self):
        self.display_surface.blit(self.image,self.rect)

    def update(self):
        self.animate()
        self.draw()