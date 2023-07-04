import pygame
from player import *
from food import *
from settings import *
from debug import debug

class World():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = CameraGroup()
        self.food_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.offset = pygame.math.Vector2(0,0)
        self.square_size = SQUARE_SIZE


        self.player = Player(0,0)
        self.visible_sprites.add(self.player)
        self.player_group.add(self.player)

    def spawn_food(self,offset = None):
        if offset == None:
            offset = self.visible_sprites.get_offset(self.player)
        food = Food((random.randint(0-offset.x,WORLD_MAP[0]*SQUARE_SIZE),random.randint(0-offset.y,WORLD_MAP[1]*SQUARE_SIZE)))
        self.food_group.add(food)
        self.visible_sprites.add(food)

    def collisions(self):
        for food in self.food_group.sprites():
            if self.player.rect.colliderect(food.rect):
                self.player.resize(food.size)
                food.kill()

    def update(self):
        self.visible_sprites.update()
        self.spawn_food()
        self.collisions()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(0,0)

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for x in range(WORLD_MAP[0]+1):
            pygame.draw.line(self.display_surface,(127,127,127),(x*SQUARE_SIZE-self.offset.x,0),(x*SQUARE_SIZE-self.offset.x,(WORLD_MAP[1]*SQUARE_SIZE)),1)
        for y in range(WORLD_MAP[1]+1):
            pygame.draw.line(self.display_surface,(127,127,127),(0,y*SQUARE_SIZE-self.offset.y),((WORLD_MAP[0]*SQUARE_SIZE),y*SQUARE_SIZE-self.offset.y),1)


        for sprite in self.sprites():
            offset_pos = sprite.rect.center - self.offset
            pygame.draw.circle(self.display_surface,sprite.body_color,offset_pos,sprite.size)
            pygame.draw.circle(self.display_surface,sprite.border_color,offset_pos,sprite.size,int(1))

    def get_offset(self,player):
        self.offset = pygame.math.Vector2(0,0)
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        return self.offset
