import pygame
from pygame.math import Vector2
from settings import *

class Snake():
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.body = [Vector2(5,BOARD_SIZE[0]//2),Vector2(4,BOARD_SIZE[0]//2),Vector2(3,BOARD_SIZE[0]//2)]
        self.direction = Vector2(0,0)
        self.move_cooldown = FPS//6
        self.eatting = False

    def add_body(self):
        self.eatting = True
    
    def key_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.x = 0
            self.direction.y = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.x = 0
            self.direction.y = 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.y = 0
            self.direction.x = 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.y = 0
            self.direction.x = -1
    
    def move(self):
        if self.move_cooldown <= 0:
            if self.eatting:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.eatting = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]

    def cooldowns(self):
        if self.move_cooldown <= 0:
            self.move_cooldown = FPS//6
        self.move_cooldown -= 1

    def draw(self):
        for body in self.body:
            snake_rect = pygame.Rect(body.x * SQUARE_SIZE,body.y * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
            pygame.draw.rect(self.display_surface,SNAKE_COLOR,snake_rect)

    def update(self):
        self.key_inputs()
        self.cooldowns()
        self.move()
        self.draw()