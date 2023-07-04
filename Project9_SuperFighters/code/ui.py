import pygame
from settings import *

class UI():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.offset_x = UI_OFFSET_X
        self.offset_y = UI_OFFSET_Y
        # founts
        self.font_15px = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\graphics\\fonts\\joystix.ttf",15)
        self.font_25px = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\graphics\\fonts\\joystix.ttf",25)
    
    def draw_text(self,text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.display_surface.blit(img, (x, y))
    
    def show_bar(self,current_health,max_health,index):
        bar_offset_x = UI_BAR_OFFSET_X
        bar_offset_y = UI_BAR_OFFSET_Y
        bar_length = BAR_WIDTH
        bar_height = BAR_HEIGHT
        retio = max_health / bar_length
        pygame.draw.rect(self.display_surface,
                         WHITE_UI_COLOR,
                         ((index*200)+bar_offset_x,
                          bar_offset_y,
                          bar_length,
                          bar_height),
                          3)
        pygame.draw.rect(self.display_surface,
                         RED,
                         ((index*200)+bar_offset_x,
                          bar_offset_y,
                          int(current_health/retio),
                          bar_height))
        
    def show_inventory(self,player):
        ui_surf = pygame.surface.Surface((175,110))
        ui_rect = ui_surf.get_rect(topleft = ((self.index*200)+self.offset_x,self.offset_y))
        ui_surf.fill(BLACK)
        self.display_surface.blit(ui_surf,((self.index*200)+self.offset_x,self.offset_y))
        
        # melee weapon display
        if player.weapons["melee_weapon"][0] != "punch":
            hit_weapon_image = pygame.image.load("{}\\assets\\weapons\\melee_weapons\{}.png".format(PROJECT_FOLDER,player.weapons["melee_weapon"][0])).convert_alpha()
            hit_weapon_rect = hit_weapon_image.get_rect(bottomleft = ((player.index*200)+self.offset_x,ui_rect.bottom))
            self.display_surface.blit(hit_weapon_image,hit_weapon_rect)
        
        # range weapon display
        range_weapon_image = pygame.image.load("{}\\weapons\\range_weapons\{}.png".format(PROJECT_FOLDER,player.weapons["range_weapon"][0])).convert_alpha()
        range_weapon_rect = range_weapon_image.get_rect(bottomleft = ((player.index*200)+50,ui_rect.bottom))
        self.display_surface.blit(range_weapon_image,range_weapon_rect)
        
        # bomb display
        bomb_image = pygame.image.load("{}\\weapons\\bombs\\{}.png".format(PROJECT_FOLDER,player.weapons["bomb"][0])).convert_alpha()
        bomb_rect = bomb_image.get_rect(topleft = (range_weapon_rect.right+10 ,ui_rect.bottom))
        self.display_surface.blit(bomb_image,bomb_rect)

        self.draw_text(f"Player {player.index+1}",self.font_15px,(255,255,255),(player.index*200)+self.offset_x,0)
        self.draw_text(f"x{player.weapons[1][1]}",self.font_15px,(255,255,255),range_weapon_rect.centerx-(player.range_weapon_rect.size[0]//2),55)
        self.draw_text(f"x{player.weapons[2][1]}",self.font_15px,(255,255,255),bomb_rect.centerx-(player.bomb_rect.size[0]//2),55)
    
    def display(self,player):
        self.show_inventory(player)

        self.show_bar()