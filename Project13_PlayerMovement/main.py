import pygame
import sys
import os
import csv

# pygame setup
pygame.init()
PROJECT_FOLDER = "D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\.Small\\GoodPlayerMovement"
FPS = 60
WIDTH = 960
HEIGHT = 640
TILE_SIZE = 64
pygame.display.set_caption("Player Movement.")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None,30)


def debug(info,y = 10, x = 0):
	screen = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(screen,'Black',debug_rect)
	screen.blit(debug_surf,debug_rect)

def import_folder(path):
    files_list = os.listdir(path)
    images = []
    for file in files_list:
        full_path = f"{path}\\{file}"
        image = pygame.image.load(full_path).convert_alpha()
        images.append(image)
    return images

def import_csv(path):
    world_map = []
    with open(path) as level_map:
        layout = csv.reader(level_map,delimiter = ',')
        for row in layout:
            world_map.append(list(row))
        return world_map

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,surface):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

class Adventurer(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = 1
        self.vel_y = 0
        self.gravity = 0.55
        self.jump_space = 10
        self.speed = 0
        self.crouch_walk_speed = 1.5
        self.walk_speed = 3
        self.run_speed = 5
        self.run_fast_speed = 7
        self.speed_potion = False
        self.flip = False
        self.in_air = True
        self.crouch = False
        self.walk = False
        self.run = False
        self.attack = False
        self.hand_attack = False
        self.sword_attack = False
        self.bow_attack = False
        self.changing_weapon = False
        self.status = "idle"
        self.weapons = ["hand","sword","bow"]
        self.weapon_index = 0
        self.weapon = self.weapons[self.weapon_index]
        self.import_assets()
        self.switch_weapon_time = pygame.time.get_ticks()
        self.switch_cooldown = 600
        self.can_switch_weapon = True
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def get_speed(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LCTRL]:
            self.speed = self.run_speed
        elif keys[pygame.K_LSHIFT]:
            self.speed = self.crouch_walk_speed
        elif not keys[pygame.K_LSHIFT] and not keys[pygame.K_LCTRL]:
            self.speed = self.walk_speed

    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        # movement
        if keys[pygame.K_LSHIFT]:
            self.crouch = True
        elif not keys[pygame.K_LSHIFT]:
            self.crouch = False
        if keys[pygame.K_LCTRL]:
            self.run = True
        elif not keys[pygame.K_LCTRL]:
            self.run = False
        if not keys[pygame.K_a] or not keys[pygame.K_d]:
            self.walk = False
        if keys[pygame.K_w] and not self.in_air or keys[pygame.K_SPACE] and not self.in_air:
            self.vel_y = -self.jump_space
            self.in_air = True
        if keys[pygame.K_d]:
            self.walk = True
            self.get_speed()
            self.direction = 1
            self.flip = False
            self.move(self.speed)
        if keys[pygame.K_a]:
            self.walk = True
            self.get_speed()
            self.direction = -1
            self.flip = True
            self.move(self.speed)
        # weapon
        if keys[pygame.K_e] and self.can_switch_weapon:
            self.switch_weapon_time = pygame.time.get_ticks()
            self.changing_weapon = True
            self.can_switch_weapon = False
            self.weapon_index += 1
            if self.weapon_index == len(self.weapons):
                self.weapon_index = 0
            self.weapon = self.weapons[self.weapon_index]
        # attack
        if mouse[0] or mouse[2]:
            if self.weapon == "sword":
                self.attack = True
                self.sword_attack = True
            elif self.weapon == "hand":
                self.attack = True
                self.hand_attack = True
            elif self.weapon == "bow":
                self.attack = True
                self.bow_attack = True
        else:
            self.attack = False
            self.hand_attack = False
            self.bow_attack = False
            self.sword_attack = False
                

    def move(self,speed):
        if not self.attack:
            self.rect.x += self.direction * speed
            self.collisions("horizontal")

    def import_assets(self):
        self.animations = {
            "idle":[],"idle_sword":[],
            "air_attack_side":[],"air_attack_up":[],"air_attack_down":[],
            "attack_side":[],"attack_up":[],"attack_down":[],
            "bow":[],"air_bow":[],
            "sword_draw":[],"sword_sheathe":[],
            "punch_side":[],"kick_side":[],"kick_down":[],
            "run":[],"run_sword":[],"run_fast":[],"run_punch":[],"run_wall":[],"walk":[],"crouch_walk":[],
            "climp":[],"crouch":[],"get_up":[],"grap":[],"hurt":[],"slide":[],"wall_slide":[],"smrslt":[],
            "swim":[],"water_tread":[],
            "die":[],"ladder":[],"knock_down":[],
            "jump":[],"fall":[],
        }
        for animation in self.animations.keys():
            animation_path = f"{PROJECT_FOLDER}\\assets\\adventurer\\{animation}"
            self.animations[animation] = import_folder(animation_path)

    def collisions(self,direction):
        if direction == "horizontal":
            for sprite in obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction == 1:# moving right
                        self.rect.right = sprite.rect.left
                    if self.direction == -1:# moving left
                        self.rect.left = sprite.rect.right
        elif direction == "vertical":
            for sprite in obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.vel_y > 0:# falling
                        self.rect.bottom = sprite.rect.top
                        self.in_air = False
                    if self.vel_y < 0:# jumping
                        self.vel_y = 0
                        self.rect.top = sprite.rect.bottom

    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y
        self.collisions("vertical")

    def get_status(self):
        previuos_status = self.status
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if self.hand_attack:
            if mouse[0]:
                if self.run:
                    self.status = "run_punch"
                    self.walk = False
                    self.run = False
                    self.speed = 0
                else:
                    self.status = "punch_side"
                return None
            if mouse[2]:
                if self.in_air:
                    self.status = "kick_down"
                else:
                    self.status = "kick_side"
                return None
                
        if self.sword_attack:
            if mouse[0]:
                if self.in_air:
                    if keys[pygame.K_w]:
                        self.status = "air_attack_up"
                    if keys[pygame.K_s]:
                        self.status = "air_attack_down"
                        self.vel_y = 3
                    else:
                        self.status = "air_attack_side"
                    return None
                else:
                    if keys[pygame.K_w]:
                        self.status = "attack_up"
                    if keys[pygame.K_s]:
                        self.status = "attack_down"
                    else:
                        self.status = "attack_side"
                    return None

        if self.bow_attack:
            if mouse[0]:
                if self.in_air:
                    self.status = "air_bow"
                else:
                    self.status = "bow"
                return None

        if self.in_air and self.vel_y > 0:
            self.status = "fall"
            return None
        elif self.in_air and self.vel_y < 0:
            self.status = "jump"
            return None
        

        if self.changing_weapon:
            if self.weapon == "sword":
                self.status = "sword_sheathe"
            else:
                self.status = "sword_draw"
            return None

        

        if self.run and not self.in_air:
            if self.weapon == "sword":
                self.status = "run_sword"
            if self.speed_potion:
                self.status = "run_fast"
            if self.hand_attack:
                self.status = "run_punch"
            else:
                self.status = "run"

        elif self.walk and not self.in_air and not self.run:
            if self.crouch:
                self.status = "crouch_walk"
            else:
                self.status = "walk"

        else:
            if self.weapon == "sword":
                self.status = "idle_sword"
            else:
                self.status = "idle"

        if self.status != previuos_status:
            self.frame_index = 0

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            if self.status in ["sword_sheathe","sword_draw"]:
                self.changing_weapon = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(topleft = self.rect.topleft)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.switch_weapon_time >= self.switch_cooldown:
            self.can_switch_weapon = True

    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)

    def update(self):
        self.input()
        self.apply_gravity()
        self.get_status()
        self.animate()
        self.cooldowns()
        self.draw()

class WorldMap():
    def __init__(self):
        self.tiles_group = pygame.sprite.Group()

    def load_map(self,csv):
        for row_index,row in enumerate(csv):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col != "-1":
                    if col == "0":
                        tile = Tile((x,y),[visible_sprites,obstacle_sprites],pygame.image.load(f"{PROJECT_FOLDER}\\assets\\block.png"))
                        self.tiles_group.add(tile)
    
    def draw(self):
        for tile in self.tiles_group.sprites():
            screen.blit(tile.image,tile.rect)

    def update(self):
        self.draw()


player = Adventurer((400,300))
visible_sprites = pygame.sprite.Group(player)
obstacle_sprites = pygame.sprite.Group()
data = import_csv(f"{PROJECT_FOLDER}\\assets\\map.csv")
world = WorldMap()
world.load_map(data)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))

    player.update()
    world.update()

    debug(f"run:{player.run}",
          0)
    debug(f"walk:{player.walk}",
          0,100)
    debug(f"crouch:{player.crouch}",
          0,215)
    debug(f"direction:{player.direction}",
          0,485)
    debug(f"in_air:{player.in_air}",
          25)
    debug(f"changing_weapon:{player.changing_weapon}",
          25,125)
    debug(f"speed:{player.speed}",
          25,375)
    debug(f"weapon:{player.weapon}",
          25,475)
    debug(f"frame_index:{round(player.frame_index,2)}",
          25,625)
    debug(f"can_switch_weapon:{player.can_switch_weapon}",
          50)
    debug(f"switch_cooldown:{player.switch_cooldown}",
          50,260)
    debug(f"status:{player.status}",
          75)

    pygame.display.update()
    clock.tick(60)