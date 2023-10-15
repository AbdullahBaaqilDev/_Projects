import pygame
from settings import *

class Piece(pygame.sprite.Sprite):
    symbol_from_id = {1: "k", 2: "q", 3: "r", 4: "b", 5: "n", 6: "p"}

    def __init__(self, id, image, square, groups):
        super().__init__(groups)
        self.screen = pygame.display.get_surface()
        self.id = id
        self.moved = False
        self.square = square
        self.image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(topleft = square.pos * SQUARE_SIZE)
    
    def move_to(self, square):
        self.rect = self.image.get_rect(topleft = square.pos * SQUARE_SIZE)
        self.square = square
        self.moved = True
    
    def is_selected(self, selected_piece):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos) and mouse_pressed and not selected_piece or \
            mouse_pressed and selected_piece == self:
            self.rect.center = mouse_pos
            return self
        return None

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
class King(Piece):
    def __init__(self, color_value, image, pos, groups):
        super().__init__(1 * color_value, image, pos, groups)

class Qween(Piece):
    def __init__(self, color_value, image, pos, groups):
        super().__init__(2 * color_value, image, pos, groups)

class Rook(Piece):
    def __init__(self, color_value, image, pos, groups):
        super().__init__(3 * color_value, image, pos, groups)

class Bishop(Piece):
    def __init__(self, color_value, image, pos, groups):
        super().__init__(4 * color_value, image, pos, groups)

class Knight(Piece):
    def __init__(self, color_value, image, pos, groups):
        super().__init__(5 * color_value, image, pos, groups)

class Pawn(Piece):
    def __init__(self, color_value, image, pos, groups):
        super().__init__(6 * color_value, image, pos, groups)
        self.en_passant = False