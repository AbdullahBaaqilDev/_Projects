import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,**config):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.Surface(config["size"])
        self.rect = self.image.get_rect(topleft = config["pos"])
        self.text = config["text"]
        self.cost = config["cost"]
        self.bg = config["bg"]
        self.fg = config["fg"]
        self.bg_actv = config["bg_actv"]
        self.fg_actv = config["fg_actv"]
        self.border_width = config["border_width"]
        self.border_color = config("border_color")
        self.border_color_actv = config("border_color_actv")
        self.command = config["command"]
        self.index = config["index"]
        self.font = config["font"]
        self.hovered = False

    def collision(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0] and self.can_press:
                self.command()
                self.press_time = pygame.time.get_ticks()
                self.can_press = False
                self.hovered = False
            else:
                self.hovered = True
        else:
            self.hovered = False

    def draw_name(self):
        color = self.fg if not self.hovered else self.fg_actv

        text_surf = self.font.render(self.text,True,color,)
        text_rect = text_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        self.display_surface.blit(text_surf,text_rect)

    def draw_cost(self):
        color = self.fg if not self.hovered else self.fg_actv

        text_surf = self.font.render(str(self.cost),True,color,)
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
        self.cost *= 1.4
        self.command()

    def update(self):
        self.collision()
        self.draw()