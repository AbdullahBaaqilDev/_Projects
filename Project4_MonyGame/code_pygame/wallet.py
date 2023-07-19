import pygame
from math import sin, cos, pi
from random import choice

class Wallet(pygame.sprite.Sprite):
    def __init__(self,image,money,parent,pos,groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.parent = parent
        self.image_ = image
        self.rect = self.image_.get_rect(center = pos)
        self.money = money
        self.rotate = 0

    def update(self):
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        self.rotate += 1
        if self.rotate == 360:
            self.rotate = 0
        self.image = pygame.transform.rotate(self.image_,self.rotate)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect.x += 4
        if self.rect.collidepoint(mouse_pos) and mouse_press[0]:
            circle_radius = self.money * 4
            angle = 2 * pi / self.money
            for number in range(self.money):
                x = self.rect.centerx + circle_radius * cos(number * angle)
                y = self.rect.centery + circle_radius * sin(number * angle)
                self.parent.money_button_command((x,y))
            choice(self.parent.wallet_sounds).play()
            self.kill()
        self.display_surface.blit(self.image,self.rect)
        