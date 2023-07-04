import pygame
import os
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.shoot_cooldown_e = 25
        self.shoot_cooldown_r = 6
        self.size = PLAYER_STATUS["size"]
        self.size_ = 0.1
        self.speed = PLAYER_STATUS["speed"]
        self.body_color = PLAYER_STATUS["body_color"]
        self.border_color = PLAYER_STATUS["border_color"]
        self.border_size = 0.1
        self.direction = pygame.math.Vector2(0,0)
        self.rect = pygame.Rect(x,y,self.size,self.size)
    
    def inputs(self):
        keys = pygame.key.get_pressed()
        # shoot ball
        if keys[pygame.K_e] and self.shoot_cooldown_e <= 0:
            self.shoot()
        elif keys[pygame.K_r] and self.shoot_cooldown_r <= 0:
            self.shoot()
    
    def resize(self,size = 1):
        self.size += size
        self.rect.w = self.size
        self.rect.h = self.size
        self.speed = abs(self.speed - size ** self.size_)
        self.size_ /= 2

    def move(self):
        mouse_pos = pygame.mouse.get_pos()
        direction_x = mouse_pos[0] - self.display_surface.get_width()//2
        direction_y = mouse_pos[1] - self.display_surface.get_height()//2
        direction_len = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if direction_len != 0:
            direction_x /= direction_len
            direction_y /= direction_len

        self.rect.x += direction_x * self.speed
        self.rect.y += direction_y * self.speed

    def cooldowns(self):
        if self.shoot_cooldown_e <= 0:
            self.shoot_cooldown_e = 25
        if self.shoot_cooldown_r <= 0:
            self.shoot_cooldown_r = 5
        self.shoot_cooldown_e -= 1
        self.shoot_cooldown_r -= 1

    def update(self):
        self.cooldowns()
        self.inputs()
        self.move()