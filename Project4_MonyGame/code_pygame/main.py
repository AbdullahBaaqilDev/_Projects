import pygame
import sys
from os import walk

FPS = 60
WIDTH = 500
HEIGHT = 400
SCREEN_COLOR = (31,31,31)
START_MONEY = 25
START_CLICKS = 0
PROJECT_FOLDER = "D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project4_MonyGame"
TEXT_COLOR = (238,238,238)
TEXT_COLOR_SELECTED = (17,17,17)
BAR_COLOR = (238,238,238)
BAR_COLOR_SELECTED = (17,17,17)
UPGRADE_BG_COLOR_SELECTED = (238,238,238)
pygame.init()
pygame.display.set_caption("Money Game")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        print(_,__,img_files)
        for image in img_files:
            full_path = path + "\\" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

def reflect_images(frames):
    new_frames = []
    for frame in frames:
        flipped_frame = pygame.transform.flip(frame,True,False)
        new_frames.append(flipped_frame)
    return new_frames

class Button(pygame.sprite.Sprite):
    def __init__(self,image,pos,command,press_cooldown):
        self.display_surface = pygame.display.get_surface()
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.command = command
        self.alpha = 200

        self.press_cooldown = press_cooldown
        self.press_time = None
        self.can_press = True
    
    def highlight(self):
        self.image.set_alpha(self.alpha)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if not self.can_press:
            if self.press_time - current_time >= self.press_cooldown:
                self.can_press = True

    def collision(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0] and self.can_press:
                self.command()
            else:
                self.alpha = 255
        else:
            self.alpha = 200

    def draw(self):
        self.display_surface.blit(self.image,self.rect)

    def update(self):
        self.cooldowns()
        self.collision()
        self.highlight()
        self.draw()

class ParticlesAnimationPlayer():
    def __init__(self):
        self.animations = {
            "money":[
                import_folder(f"{PROJECT_FOLDER}\\assets\\particles\\money"),
                reflect_images(import_folder(f"{PROJECT_FOLDER}\\assets\\particles\\money"))
                ]
        }

    def create_particle(self,animation,pos,groups):
        animation_frames = self.animations[animation]
        Particle(pos,animation_frames,groups)
                
class Particle(pygame.sprite.Sprite):
    def __init__(self,animation,pos,groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.animation = animation
        self.frame_index = 0
        self.animation_speed = 0.15

        self.image = animation[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.kill()

        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center = (self.rect.centerx+int(self.frame_index),self.rect.centery))

    def draw(self):
        self.display_surface.blit(self.image,self.rect)

    def update(self):
        self.animate()
        self.draw()

class Upgrads():
    def __init__(self,user,font):
        self.display_surface = pygame.display.get_surface()
        self.user = user
        self.upgrades_number = 4# 1.money per click 2.click per click 3.BOOST 4.auto clicker 5.
        self.width = self.display_surface.get_width() * 0.2
        self.height = self.display_surface.get_height() * 0.8
        self.font = font

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.upgrades_number)):
            # horizontal position
            full_width = self.display_surface.get_width()
            increment = full_width // self.upgrades_number
            left = (item * increment) + (increment - self.width) // 2
            
            # vertical position
            top = self.display_surface.get_height() * 0.1

            # create the object 
            item = Item(pygame.Rect(left,top,self.width,self.height),index,self.font)
            self.item_list.append(item)
    
    def upgrade1_command(self):
        pass
    
    def upgrade2_command(self):
        pass
    
    def upgrade3_command(self):
        pass

    def upgrade4_command(self):
        pass

class Item():
    def __init__(self,rect,index,font):
        self.display_surface = pygame.display.get_surface()
        self.rect = rect
        self.index = index
        self.font  = font

    def display_titles(self,surface,name,cost,selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # title
        name_surf = self.font.render(name,False,color)
        name_rect = name_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))

        # cost 
        cost_surf = self.font.render(f'{int(cost)}',False,color)
        cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))

        # draw 
        surface.blit(name_surf,name_rect)
        surface.blit(cost_surf,cost_rect)
    def trigger(self,player):
        upgrade_name = list(player.stats.keys())[self.index]

        if player.exp >= player.upgrade_cost[upgrade_name] and player.stats[upgrade_name] < player.max_stats[upgrade_name]:
            player.exp -= player.upgrade_cost[upgrade_name]
            player.stats[upgrade_name] *= 1.2
            player.upgrade_cost[upgrade_name] *= 1.4

        if player.stats[upgrade_name] > player.max_stats[upgrade_name]:
            player.stats[upgrade_name] = player.max_stats[upgrade_name]

class UI():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.buttons_group = pygame.sprite.Group()
        self.font = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\font\\joystix.ttf")
    
    def show_upgrads(self):
        pass

    def display(self):
        pass

class User():
    def __init__(self,start_money,start_clicks):
        self.money = start_money
        self.clicks = start_clicks


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(SCREEN_COLOR)
    
    pygame.display.update()
    clock.tick(FPS)