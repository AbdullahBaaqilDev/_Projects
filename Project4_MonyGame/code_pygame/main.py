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
UI_BG_COLOR = (17,17,17)
UI_BG_COLOR_SELECTED = (238,238,238)
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
    def __init__(self,text,pos,size,command,press_cooldown,index,font:pygame.font.Font):
        self.display_surface = pygame.display.get_surface()
        self.text = text
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft = pos)
        self.command = command
        self.index = index
        self.font = font
        self.hovered = False

        self.press_cooldown = press_cooldown
        self.press_time = None
        self.can_press = True

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
                self.hovered = False
            else:
                self.hovered = True

    def draw_name(self):
        color = TEXT_COLOR if not self.hovered else TEXT_COLOR_SELECTED

        text_surf = self.font.render(self.text,True,color,)
        text_rect = text_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        self.display_surface.blit(text_surf,text_rect)

    def draw(self):
        self.image.fill(UI_BG_COLOR if not self.hovered else UI_BG_COLOR_SELECTED)
        self.display_surface.blit(self.image,self.rect)
        self.draw_name()

    def update(self):
        self.cooldowns()
        self.collision()
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

class Upgrades():
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.upgrades_commands = [self.upgrade1_command,self.upgrade2_command,self.upgrade3_command,self.upgrade4_command,]
    
    def upgrade1_command(self):
        pass
    
    def upgrade2_command(self):
        pass

    def upgrade3_command(self):
        pass

    def upgrade4_command(self):
        pass

class UI():
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.buttons_group = pygame.sprite.Group()
        self.font = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\font\\joystix.ttf")
        self.player = player
        # upgrades
        self.upgrades = Upgrades(self.player)
        self.upgrades_names = ["Money +","Clicks +","BOOST","Auto Clicker"]
        self.upgrade_button_width = self.display_surface.get_width() * 0.4
        self.upgrade_button_height = self.display_surface.get_height() * 0.4
        self.create_upgrades_buttons()

    def create_upgrades_buttons(self):
        self.buttons_list = []

        for index,button in enumerate(self.upgrades_names):
            full_width = self.display_surface.get_width()
            increment = full_width // len(self.upgrades_names)
            left = (index * increment) + (increment - self.upgrade_button_width) // 2
            
            top = self.display_surface.get_height() * 0.1

            # create the object
            button = Button(button,(left,top),(self.upgrade_button_width,self.upgrade_button_height),self.upgrades.upgrades_commands[index],0,index,self.font)
            self.buttons_list.append(button)
    
    def diplay_money(self):
        pass

    def diplay_clicks(self):
        pass

    def display_upgrads(self):
        pass

    def display_buttons(self):
        pass

    def display(self):
        pass

class Player():
    def __init__(self,money,clicks):
        self.money = money
        self.clicks = clicks

class Main():
    def __init__(self):
        self.player = Player(9999999,999)
        self.ui = UI(self.player)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill(SCREEN_COLOR)

            self.ui.display()
            
            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    game = Main()
    game.mainloop()