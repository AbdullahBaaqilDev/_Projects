import pygame
from pygame.math import Vector2 as Vec
from spritesheet import SpriteSheet
from move import Move
from square import Square
from pieces import *
from settings import *
from debug import debug

class Board():
    def __init__(self, fen = None):
        self.pieces = pygame.sprite.Group()
        self.squares = pygame.sprite.Group()
        self.create_squares()
        self.create_images()
        if fen: self.load_fen(fen)

    def create_images(self):
        pieces_image = pygame.image.load(PIECES_IMAGE)
        pieces_spritesheet = SpriteSheet(pieces_image, 106, 106)
        self.pieces_images = {
            "K": pieces_spritesheet.get(0, 0),
            "k": pieces_spritesheet.get(0, 1),
            "Q": pieces_spritesheet.get(1, 0),
            "q": pieces_spritesheet.get(1, 1),
            "B": pieces_spritesheet.get(2, 0),
            "b": pieces_spritesheet.get(2, 1),
            "N": pieces_spritesheet.get(3, 0),
            "n": pieces_spritesheet.get(3, 1),
            "R": pieces_spritesheet.get(4, 0),
            "r": pieces_spritesheet.get(4, 1),
            "P": pieces_spritesheet.get(5, 0),
            "p": pieces_spritesheet.get(5, 1),
        }
    
    def create_squares(self):
        for rank in range(8):
            for file in range(8):
                is_light = True if (rank + file) % 2 != 0 else False
                Square(is_light, Vec(file, rank), self.squares)

    def load_fen(self, fen):
        pieces_part, turn, castle_part, time_part = fen.split(" ")

        # create the pieces
        file, rank = 0, 0
        for symbol in pieces_part:
            if symbol.isdigit():
                file += int(symbol)
            elif symbol == "/":
                rank += 1
                file = 0
            else:
                color_value = 1 if symbol.isupper() else -1
                for square in self.squares:
                    if square.pos == Vec(file, rank): piece_square = square

                if symbol.lower() == "k":
                    piece_square.piece = King(color_value, self.pieces_images[symbol], piece_square, self.pieces)
                elif symbol.lower() == "q":
                    piece_square.piece = Qween(color_value, self.pieces_images[symbol], piece_square, self.pieces)
                elif symbol.lower() == "r":
                    piece_square.piece = Rook(color_value, self.pieces_images[symbol], piece_square, self.pieces)
                elif symbol.lower() == "b":
                    piece_square.piece = Bishop(color_value, self.pieces_images[symbol], piece_square, self.pieces)
                elif symbol.lower() == "n":
                    piece_square.piece = Knight(color_value, self.pieces_images[symbol], piece_square, self.pieces)
                else:
                    piece_square.piece = Pawn(color_value, self.pieces_images[symbol], piece_square, self.pieces)
                file += 1

        # turn
        self.turn = 1 if turn == "w" else -1

        # castle
        self.castle = {
            1: {
                "king_side": True if castle_part[0] == "K" else False,
                "qween_side": True if castle_part[1] == "Q" else False
            },
            -1: {
                "king_side": True if castle_part[2] == "k" else False,
                "qween_side": True if castle_part[3] == "q" else False
            }
        }

        # time
        white_time = time_part.split("-")[0]
        black_time = time_part.split("-")[1]
        self.time = [white_time, black_time]

    def current_fen(self):
        fen = ""
        file, rank = 0, 0
        space = 0
        
        # pieces part
        for square in self.squares:
            if square.piece:
                if square.piece.id < 0:
                    fen += str(space) + Piece.symbol_from_id[abs(square.piece.id)] if space != 0 else Piece.symbol_from_id[abs(square.piece.id)]
                else: fen += str(space) + Piece.symbol_from_id[abs(square.piece.id)].upper() if space != 0 else Piece.symbol_from_id[abs(square.piece.id)].upper()
                file += 1
                space = 0
            else: space += 1

            if square.pos.x >= 7 and square.pos != Vec(7,7):
                fen += "/"
                rank += 1
                file = 0
                space = 0
        
        # turn
        fen += " w" if self.turn == 1 else "b"

        # castle
        fen += " K" if self.castle[1]["king_side"] else " -"
        fen += "Q" if self.castle[1]["qween_side"] else "-"
        fen += "k" if self.castle[-1]["king_side"] else "-"
        fen += "q" if self.castle[-1]["qween_side"] else "-"

        # time
        fen += f" {self.time[0]}-{self.time[1]}"

        return fen


class MainBoard(Board):
    def __init__(self, fen = None):
        super().__init__(fen)
        self.screen = pygame.display.get_surface()
        self.selected_piece = None
        self.selected_square = None
        self.move_logic = Move(Board)
        self.pieces_moves = {}
        self.load_pieces_legal_moves()

    def load_pieces_legal_moves(self):
        for piece in self.pieces:
            self.pieces_moves[piece] = self.move_logic.get_legal_moves(self, piece)
    
    def unhighlight_squares(self):
        for square in self.squares:
            square.highlight("normal")

    def update_selected(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]

        for square in self.squares:
            self.selected_square = square.is_selected()
            if self.selected_square: break

        if not mouse_pressed and self.selected_piece:
            if self.selected_square in self.pieces_moves[self.selected_piece]:
                self.move_logic.move(self.selected_piece, self.selected_square)
                self.load_pieces_legal_moves()
            else:
                self.selected_piece.move_to(self.selected_piece.square)
            
            self.unhighlight_squares()

        for piece in self.pieces:
            selected = piece.is_selected(self.selected_piece)
            if selected: break
            selected = None
        self.selected_piece = selected
        
        if self.selected_piece:
            for piece_moves in self.pieces_moves[self.selected_piece]:
                piece_moves.highlight("red")
            print(self.pieces_moves[self.selected_piece])
        else: self.unhighlight_squares()

    def draw(self):
        self.squares.draw(self.screen)
        self.pieces.draw(self.screen)
    
    def update(self):
        self.update_selected()
        self.draw()
        debug(self.current_fen())
        debug(self.selected_piece,25)
        if self.selected_square:
            debug(self.selected_square.piece,45)