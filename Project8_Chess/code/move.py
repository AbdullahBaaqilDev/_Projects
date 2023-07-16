import pygame
from pygame import Vector2 as Vec
from settings import *

class Move():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.turn = 0
        self.pieces_directions = PIECES_DIRETIONS
        # sounds
        move_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\move.wav")
        capture_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\capture.wav")
        check_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\check.wav")
        castle_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\castle.wav")
        promote_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\promote.wav")
        self.sounds_list = {
            "normal" : move_sound,
            "capture": capture_sound,
            "check"  : check_sound,
            "castle" : castle_sound,
            "promote": promote_sound
        }

    def update_attributes(self,squares=None,pieces=None,piece=None,square=None):
        self.squares = squares
        self.pieces = pieces
        self.piece = piece
        self.square = square
        self.current_pos = Vec(self.piece.square.pos) if piece else None

    def get_square_by_pos(self,square_pos):
        target = None
        for square in self.squares:
            if square.pos == square_pos:
                target = square
                return target
        return target
    
    def get_castle_pieces(self):
        pass

    def get_castle(self):
        pass
    
    def is_check(self,piece):
        for opponent_piece in self.pieces.sprites():
            if opponent_piece.value == piece.value:
                moves = self.get_piece_moves(
                    current_pos = opponent_piece.square.pos,
                    piece = opponent_piece,
                    turn = opponent_piece.value)
                for opponent_piece_move in moves.keys():
                    if opponent_piece_move.piece and \
                       opponent_piece_move.piece.id == opponent_piece.value * -1 and \
                       moves[opponent_piece_move] == "":
                        return True
        return False
    
    def get_piece_moves(self,current_pos = None,piece = None,turn = None):
        if not current_pos: current_pos = self.current_pos
        if not piece: piece = self.piece
        if not turn: turn = self.turn
        moves = {}
        direction_range = range(1,9) if piece.is_long_range else range(1,2)
        if piece.id in self.pieces_directions.keys():
            directions = self.pieces_directions[piece.id]
        else: directions = self.pieces_directions[abs(piece.id)]

        if abs(piece.id) != 6:
            for direction in directions:
                for index in direction_range:
                    square = self.get_square_by_pos(current_pos + direction * index)
                    if square:
                        if square.piece == None:
                            moves[square] = "normal"
                        else:
                            if square.piece.value != piece.value:
                                moves[square] = "capture"
                            break
        else:
            if piece.id > 0:
                if not piece.moved: directions.append(Vec(0,-2))
            else:
                if not piece.moved: directions.append(Vec(0,2))

            for direction in directions:
                square = self.get_square_by_pos(current_pos + direction)
                if square:
                    if square.piece == None:
                        if direction == directions[0]:
                            moves[square] = "normal"
                        if not self.piece.moved:
                            if direction == directions[3]:
                                one_square_before = self.get_square_by_pos(current_pos+directions[0])
                                if one_square_before in moves:
                                    moves[square] = "normal"
                    else:
                        if direction in [directions[1],directions[2]]:
                            if square.piece.value != piece.value:
                                moves[square] = "capture"
        return moves
    
    def move_piece(self,piece,square):
        piece.moved = True
        piece.square.piece = None
        piece.rect.topleft = square.rect.topleft
        square.piece = piece
        piece.square = square
        self.update_attributes(self.squares,self.pieces,piece,square)

    def set_move(self,turn = None,piece = None,square = None):
        if not turn: turn = self.turn
        if not piece: piece = self.piece
        if not square: square = self.square

        if square in list(self.get_piece_moves().keys()) and piece.square != square:
            # set move sound
            move_type = self.get_piece_moves()[square]
            if move_type == "capture":
                square.piece.kill()


            for square_ in self.squares:
                square_.highlighted = 0
            piece.square.highlighted = 2
            square.highlighted = 2

            self.move_piece(piece,square)
            self.turn *= -1

            if self.is_check(piece):
                move_type = "check"
            self.sounds_list[move_type].play()
        else:
            self.piece.rect.topleft = self.piece.square.rect.topleft
        return self.turn