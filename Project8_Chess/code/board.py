import pygame
import sys
from move import Move
from square import Square
from piece import Piece
from settings import *
from debug import debug

class Board():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = pygame.sprite.Group()
        self.squares_group = pygame.sprite.Group()
        self.pieces_group = pygame.sprite.Group()

        self.selected_piece = None
        self.selected_square = None
        self.castle = [False] * 4
        self.move_ = Move()

        # make the squares
        for rank in range(8):
            for file in range(8):
                # square color
                is_dark = True
                if (rank+file) % 2 == 0:
                    is_dark = False
                square_name = list("abcdefgh")[file]+list("87654321")[rank]
                square = Square(file*SQUARE_SIZE,rank*SQUARE_SIZE,square_name,(file,rank),is_dark)
                self.visible_sprites.add(square)
                self.squares_group.add(square)

    def get_fen(self):
        rank = 0
        file = 0
        fen = ""
        piece_symbol_from_id_dect = {
            1:"K",
            2:"Q",
            3:"B",
            4:"N",
            5:"R",
            6:"P",
            -1:"k",
            -2:"q",
            -3:"b",
            -4:"n",
            -5:"r",
            -6:"p",
            }
        for square in self.squares_group.sprites():
            if square.piece == None:
                file += 1
            elif square.piece != None:
                if file > 0:
                    fen += str(file)
                file += 1

                fen += str(piece_symbol_from_id_dect[square.piece.id])
                file = 0
            if file-1 in list(range(7,63,8)):
                fen += "/"
                file = 0
                rank += 1

        if self.move_.turn == 1:
            tomove = "w"
        else:
            tomove = "b"
        fen += f" {tomove}"

        self.castle = self.move_.get_castle(False)
        fen += " {}{}{}{}".format(self.castle["white_ck"],self.castle["white_cq"],self.castle["black_ck"],self.castle["black_cq"])

        return fen

    def load_fen(self,fen):
        rank = 0
        file = 0
        part = 0

        piece_id_from_symbol_dect = {
            "k":1,
            "q":2,
            "b":3,
            "n":4,
            "r":5,
            "p":6,
            }
        
        for letter in fen:
            if letter == " ":
                part += 1
            elif part == 0:
                if letter == "/":
                    rank += 1
                    file = 0
                elif letter.isdigit():
                    file += int(letter)
                else:
                    square_pos = pygame.math.Vector2(file,rank)
                    for square in self.squares_group:
                        if square.pos == square_pos:
                            piece = Piece(piece_id_from_symbol_dect[letter.lower()],
                                          1 if letter.isupper() else -1,
                                          letter.lower() in ["q","b","r"],
                                          square,
                                          (file*SQUARE_SIZE,rank*SQUARE_SIZE))
                            self.visible_sprites.add(piece)
                            self.pieces_group.add(piece)
                            square.piece = piece
                            break
                    file += 1
            elif part == 1:
                if letter == "w":
                    self.move_.turn = 1
                else:
                    self.move_.turn = -1
            elif part == 2:
                self.castle.append(letter)

    def reset_board(self):
        for piece in self.pieces_group.sprites():
            piece.kill()
        for square in self.squares_group.sprites():
            square.piece = None
        self.load_fen(START_FEN)

    def update_selected(self):
        mouse = pygame.mouse.get_pressed()
        if not mouse[0] and self.selected_piece != None:
            if self.selected_square != None:
                self.move_.update_attributes(self.squares_group,self.pieces_group,self.selected_piece,self.selected_square)
                self.move_.set_move()
                self.selected_piece = None
                self.selected_square = None

        for piece in self.pieces_group.sprites():
            if piece.is_selected(self.selected_piece) != None:
                select = piece.is_selected(self.selected_piece)
                break
            else:
                select = None
        self.selected_piece = select

        temp_square = None
        for square in self.squares_group.sprites():
            if square.is_selected() != None:
                self.selected_square = square.is_selected()
                temp_square = self.selected_square
                break
        if temp_square == None:
            self.selected_square = None

    def highlight_squares(self):
        mouse = pygame.mouse.get_pressed()
        if self.selected_piece != None:
            self.move_.update_attributes(self.squares_group,self.pieces_group,self.selected_piece,self.selected_square)
            moves = self.move_.get_piece_moves()
            for square in self.squares_group.sprites():
                square.highlighted = 0
                if square in moves:
                    square.highlighted = 1
            self.selected_piece.square.highlighted = 2
        elif self.selected_piece == None or mouse[0]:
            for square in self.squares_group.sprites():
                if square.highlighted != 2:
                    square.highlighted = 0

    def keys_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_r]:
            self.reset_board()

    def draw(self):
        for sprite in self.visible_sprites.sprites():
            self.display_surface.blit(sprite.image,sprite.rect)

    def update(self):
        self.draw()
        self.keys_inputs()
        self.highlight_squares()
        self.update_selected()
        self.visible_sprites.update()
        self.move_.update_attributes(self.squares_group,self.pieces_group,self.selected_piece,self.selected_square)
        debug(self.move_.turn)
        debug(self.get_fen(),25)
        if self.selected_piece != None:
            debug(self.selected_piece.moved,50)
        if self.selected_square != None:
            debug(self.selected_square.piece,75)
