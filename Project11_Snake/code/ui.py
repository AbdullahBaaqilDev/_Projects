import pygame

class Button(pygame.sprite.Sprite):
    pass

class Text(pygame.sprite.Sprite):
    pass

class Image(pygame.sprite.Sprite):
    pass


class UI():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.buttons = []
        self.texts = []
        self.images = []

    def create_buttons(self):
        pass

    def create_texts(self):
        pass

    def create_images(self):
        pass

    def display_text(self,
            font: pygame.font.Font = None,
            text = "Hellow, World",
            antialias = True,
            color = (0,0,0),
            pos = (0,0)):
        
        surf = font.render(text,antialias,color)
        rect = surf.get_rect(topleft = pos)
        self.display_surface.blit(surf,rect)
    
    def display(self):
        pass