import pygame
from settings import *
from spritesheet import SpriteSheet


class Piece(pygame.sprite.Sprite):
    def __init__(self,id,value,is_long_range,square,pos):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.id = id * value
        self.value = value
        self.square = square
        self.is_long_range = is_long_range
        self.moved = False
        self.en_passant = False

        sprite_sheet = pygame.image.load(f"{ASSETS_FOLDER}\\images\\pieces.png").convert_alpha()
        piece_width = int(sprite_sheet.get_width() / 6)
        piece_height = int(sprite_sheet.get_height() / 2)
        img = SpriteSheet(sprite_sheet,
                          (abs(self.id)-1)*piece_width,
                          0 if self.value > 0 else piece_height,
                          piece_width,
                          piece_height)
        self.image = pygame.transform.scale(img.get(),(SQUARE_SIZE,SQUARE_SIZE))
        self.rect = self.image.get_rect(topleft = pos)

    def is_selected(self,selected_piece):
        """return if this is selected piece"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_left = pygame.mouse.get_pressed()[0]

        if selected_piece == self:
            self.rect.center = mouse_pos

        if self.rect.collidepoint(mouse_pos) and mouse_left and selected_piece == None or selected_piece == self:
            return self
        else:
            return None
        