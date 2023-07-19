import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self,press_cooldown,**config):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.Surface(config["size"])
        self.rect = self.image.get_rect(topleft = config["pos"])
        self.press_cooldown = press_cooldown
        self.can_press = True
        self.press_time = None
        self.text = config["text"]
        self.cost = config["cost"]

        self.bg = config["bg"]
        self.fg = config["fg"]
        self.bg_actv = config["bg_actv"]
        self.fg_actv = config["fg_actv"]
        self.border_width = config["border_width"]
        self.border_color = config["border_color"]
        self.border_color_actv = config["border_color_actv"]
        self.bg_no_change = config["bg"]
        self.fg_no_change = config["fg"]
        self.bg_actv_no_change = config["bg_actv"]
        self.fg_actv_no_change = config["fg_actv"]
        self.border_width_no_change = config["border_width"]
        self.border_color_no_change = config["border_color"]
        self.border_color_actv_no_change = config["border_color_actv"]
        
        self.command = config["command"]
        self.index = config["index"]
        self.font = config["font"]
        self.hovered = False
        self.pressed = False

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if not self.can_press:
            if current_time - self.press_time >= self.press_cooldown:
                self.can_press = True

    def collision(self):
        if self.can_press:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if self.rect.collidepoint(mouse_pos):
                if not mouse_pressed[0]:
                    self.pressed = False
                if mouse_pressed[0] and not self.pressed:
                    if not self.press_cooldown:
                        self.press()
                    elif self.can_press:
                        self.press()
                        self.can_press = False
                        self.press_time = pygame.time.get_ticks()
                    self.hovered = False
                    self.pressed = True
                else:
                    self.hovered = True
            else:
                self.hovered = False
            self.bg = self.bg_no_change
            self.bg_actv = self.bg_actv_no_change
            self.fg = self.fg_no_change
            self.fg_actv = self.fg_actv_no_change
            self.border_color = self.border_color_no_change
            self.border_color_actv = self.border_color_actv_no_change
        else:
            self.bg = DISABLED_UI_BG_COLOR
            self.bg_actv = DISABLED_UI_BG_COLOR_SELECTED
            self.fg = DISABLED_TEXT_COLOR
            self.fg_actv = DISABLED_TEXT_COLOR_SELECTED
            self.border_color = DISABLED_UI_BORDER_COLOR
            self.border_color_actv = DISABLED_UI_BORDER_COLOR_SELECTED

    def draw_name(self):
        color = self.fg if not self.hovered else self.fg_actv

        text_surf = self.font.render(self.text,True,color,)
        text_rect = text_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        self.display_surface.blit(text_surf,text_rect)

    def draw_cost(self):
        color = self.fg if not self.hovered else self.fg_actv

        text_surf = self.font.render(str(round(self.cost,2)),True,color,)
        text_rect = text_surf.get_rect(midbottom = self.rect.midbottom + pygame.math.Vector2(0,-20))
        self.display_surface.blit(text_surf,text_rect)

    def draw(self):
        color = self.bg if not self.hovered else self.bg_actv
        border_color = self.border_color if not self.hovered else self.border_color_actv
        self.image.fill(color)
        self.display_surface.blit(self.image,self.rect)
        pygame.draw.rect(self.display_surface,border_color,self.rect,self.border_width)
        self.draw_name()
        if self.cost: self.draw_cost()

    def press(self):
        if self.cost:
            if self.command(self.cost): self.cost *= 1.4
        else: self.command()

    def update(self):
        self.cooldown()
        self.collision()
        self.draw()