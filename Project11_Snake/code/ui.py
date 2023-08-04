import pygame

class Button(pygame.sprite.Sprite):
    pass

class UI():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def display_main_menu(self):
        pass

    def display_text(self,
            font: pygame.font.Font = None,
            text: str = "Hellow, World",
            antialias: bool = True,
            color: tuple = (0,0,0),
            pos = (0,0)):
        surf = font.render(text,antialias,color)
        rect = surf.get_rect(topleft = pos)
        self.display_surface.blit(surf,rect)