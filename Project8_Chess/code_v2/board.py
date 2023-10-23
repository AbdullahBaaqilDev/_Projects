import pygame
from pygame.math import Vector2 as Vec
from move import Move
from square import Square
from pieces import *
from settings import *
from debug import debug

class Board():
    def __init__(self, fen = None):
        self.pieces = pygame.sprite.Group()
        self.white_pieces = pygame.sprite.Group()
        self.black_pieces = pygame.sprite.Group()
        self.squares = pygame.sprite.Group()
        self.create_squares()
        self.create_images()
        if fen: self.load_fen(fen)

    def create_images(self):
        self.pieces_images = {symbol : pygame.image.load(path) for symbol, path in PIECES_IMAGES.items()}
    
    def create_squares(self):
        for rank in range(8):
            for file in range(8):
                is_light = True if (rank + file) % 2 != 0 else False
                Square(is_light, Vec(file, rank), self, self.squares)

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
                groups = [self.pieces, self.white_pieces] if color_value == 1 else [self.pieces, self.black_pieces]

                if symbol.lower() == "k":
                    piece_square.piece = King(color_value, self.pieces_images[symbol], piece_square, groups)
                elif symbol.lower() == "q":
                    piece_square.piece = Qween(color_value, self.pieces_images[symbol], piece_square, groups)
                elif symbol.lower() == "r":
                    piece_square.piece = Rook(color_value, self.pieces_images[symbol], piece_square, groups)
                elif symbol.lower() == "b":
                    piece_square.piece = Bishop(color_value, self.pieces_images[symbol], piece_square, groups)
                elif symbol.lower() == "n":
                    piece_square.piece = Knight(color_value, self.pieces_images[symbol], piece_square, groups)
                else:
                    piece_square.piece = Pawn(color_value, self.pieces_images[symbol], piece_square, groups)
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
                    fen += str(space) + Piece.symbol_from_id[square.piece.id] if space != 0 else Piece.symbol_from_id[square.piece.id]
                else: fen += str(space) + Piece.symbol_from_id[square.piece.id].upper() if space != 0 else Piece.symbol_from_id[square.piece.id].upper()
                file += 1
                space = 0
            else: space += 1

            if square.pos.x >= 7 and square.pos != Vec(7,7):
                fen += str(space) + "/" if space > 0 else "/"
                rank += 1
                file = 0
                space = 0
        
        # turn
        fen += " w" if self.turn == 1 else " b"

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
        self.move_logic = Move(self.squares, Board)
        self.moves_played = {}
        self.pieces_legal_moves = {}
        self.load_pieces_legal_moves()

    def load_pieces_legal_moves(self):
        for piece in self.pieces:
            self.pieces_legal_moves[piece] = self.move_logic.get_legal_moves(self, piece)
    
    def unhighlight_squares(self):
        for square in self.squares:
            square.highlight("normal")

    def update_selected(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]

        for square in self.squares:
            self.selected_square = square.is_selected()
            if self.selected_square: break

        if not mouse_pressed and self.selected_piece:
            self.unhighlight_squares()
            if self.selected_square in self.pieces_legal_moves[self.selected_piece]:
                self.selected_piece.square.highlight("yellow")
                self.selected_square.highlight("yellow")

                new_en_passanted_piece = self.move_logic.move(self.selected_piece, self.selected_square)
                self.turn *= -1
                for piece in self.pieces:
                    if abs(piece.id) == 6 :
                        if piece != new_en_passanted_piece:
                            piece.en_passant = False
                self.load_pieces_legal_moves()
                if self.selected_piece.image != self.pieces_images[Piece.symbol_from_id[self.selected_piece.id]]:
                    self.selected_piece.image = self.pieces_images[Piece.symbol_from_id[self.selected_piece.id]]
            else: self.selected_piece.move_to(self.selected_piece.square)
            
        for piece in self.pieces:
            selected = piece.is_selected(self.selected_piece)
            if selected: break
            selected = None
        self.selected_piece = selected
        
        if self.selected_piece:
            for piece_moves in self.pieces_legal_moves[self.selected_piece]:
                piece_moves.highlight("red")

    def draw(self):
        self.squares.draw(self.screen)
        self.pieces.draw(self.screen)
    
    def update(self):
        self.update_selected()
        self.draw()
        
        debug(self.current_fen())
        debug(self.selected_piece,25)
        if self.selected_piece:
            debug(self.selected_piece.square.pos,25,250)
        if self.selected_square:
            debug(self.selected_square.piece,45)
            debug(self.selected_square.pos,65)
            if self.selected_square.piece:
                if abs(self.selected_square.piece.id) == 6:
                    if self.selected_square.piece.en_passant:
                        debug(self.selected_square.piece.en_passant,70)
                debug(self.selected_square.piece.id,25,305)
                debug(self.selected_square.piece.moved,70,100)