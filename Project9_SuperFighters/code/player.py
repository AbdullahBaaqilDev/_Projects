import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,skin,index,groups,obstacle_sprites):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.obstacle_sprites = obstacle_sprites
        self.skin = skin
        self.index = index
        self.speed = PLAYERS_STATS["speed"]
        self.jump_space = PLAYERS_STATS["jump_space"]
        self.health = PLAYERS_STATS["health"]
        self.max_health = PLAYERS_STATS["max_health"]
        self.weapons = PLAYERS_STATS["weapons"]
        self.direction = 1
        self.flip = False
        self.shield = False
        
        self.hitting = False
        self.hit_cooldown = 300
        self.can_hit = True
        self.hit_time = None
        
        self.shooting = False
        self.shoot_cooldown = 300
        self.can_shoot = True
        self.shoot_time = None

        self.throwing = False
        self.throw_cooldown = 300
        self.can_throw = True
        self.throw_time = None

        self.in_air = True
        self.vel_y = 0
        self.status = "idle"
        self.frame_index = 0
        self.animation_speed = 0.20
        self.import_assets()
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))

    def import_assets(self):
        self.animations = {
            "idle":[],
            "run":[],
            "jump":[],
            "hit":[],
            "shoot":[],
        }
        for animation in self.animations.keys():
            animation_path = f"{PROJECT_FOLDER}\\assets\\skins\\{self.skin}\\{animation}"
            self.animations[animation] = import_folder(animation_path)

    def inputs(self):
        keys = pygame.key.get_pressed()
        if self.index == 0:
            if keys[pygame.K_UP]:
                self.jump()
            if keys[pygame.K_RIGHT]:
                self.direction = 1
                self.move()
            if keys[pygame.K_LEFT]:
                self.direction = -1
                self.move()
            if keys[pygame.K_j]:
                self.hit()
            if keys[pygame.K_k]:
                self.shoot()
            if keys[pygame.K_l]:
                self.throw_bomb()
        else:
            if keys[pygame.K_w]:
                self.jump()
            if keys[pygame.K_d]:
                self.direction = 1
                self.move()
            if keys[pygame.K_a]:
                self.direction = -1
                self.move()
            if keys[pygame.K_c]:
                self.hit()
            if keys[pygame.K_v]:
                self.shoot()
            if keys[pygame.K_b]:
                self.throw_bomb()

    def move(self):
        self.rect.x += self.direction * self.speed
        self.collisions("horizontal")

    def jump(self):
        if not self.in_air:
            self.vel_y = self.jump_space
            self.collisions("vertical")

    def hit(self):
        self.hitting = True

    def shoot(self):
        self.shooting = True

    def throw_bomb(self):
        self.throwing = True

    def collisions(self,direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction == 1:# moving right
                        self.rect.right = sprite.rect.left
                    if self.direction == -1:# moving left
                        self.rect.left = sprite.rect.right
        elif direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.vel_y > 0:# falling
                        self.rect.bottom = sprite.rect.top
                        self.in_air = False
                    if self.vel_y < 0:# jumping
                        self.vel_y = 0
                        self.rect.top = sprite.rect.bottom

    def get_status(self):
        if self.shooting:
            self.status = "shoot"
        if self.hitting:
            self.status = "hit"
        if self.throwing:
            self.status = "throw"
        if self.in_air:
            self.status = "jump"
            return None
        else:
            self.status = "idle"

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
    
    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y
        self.collisions("vertical")

    def draw(self):
        self.display_surface.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update(self):
        self.apply_gravity()
        self.get_status()
        self.animate()
        self.draw()