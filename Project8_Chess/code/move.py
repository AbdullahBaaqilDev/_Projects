import pygame
from pygame import Vector2 as Vec
from piece import *
from square import *
from settings import *

class Move():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.move_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\move.wav")
        self.capture_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\capture.wav")
        self.check_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\check.wav")
        self.castle_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\castle.wav")
        self.promote_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\promote.wav")
        self.pieces_directions = {
            1:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
            2:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
            3:[Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
            4:[Vec(-2,1),Vec(-2,-1),Vec(2,1),Vec(2,-1),Vec(1,2),Vec(-1,2),Vec(1,-2),Vec(-1,-2),],
            5:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),],
            6:[Vec(0,-1),Vec(1,-1),Vec(-1,-1)],
            -6:[Vec(0,1),Vec(-1,1),Vec(1,1)],
        }

    def __attributes__(self,squares=None,pieces=None,piece=None,square=None,turn=None):
        self.squares = squares
        self.pieces = pieces
        self.piece = piece
        self.square = square
        self.turn = turn
        self.current_pos = Vec(self.piece.square.pos)

    def get_target_square(self,target_pos):
        target = None
        for square in self.squares:
            if square.pos == target_pos:
                target = square
                return target
        return target
    
    def get_castle(self,white,black):
        white_castle = []
        black_castle = []
        if white[0].moved:
            white_castle = ["-","-"]
        if black[0].moved:
            black_castle = ["-","-"]
        return white_castle,black_castle
    
    def get_piece_moves(self,current_pos = None,piece = None):
        if current_pos == None:
            current_pos = self.current_pos
        if piece == None:
            piece = self.piece
        moves = []
        direction_range = range(1,9) if piece.is_long_range else range(1,2)
        if piece.id in list(self.pieces_directions.keys()): directions = self.pieces_directions[piece.id]
        else: directions = self.pieces_directions[abs(piece.id)]
        if abs(piece.id) != 6:
            for direction in directions:
                for index in direction_range:
                    square = self.get_target_square(current_pos+direction*index)
                    if square != None:
                        if square.piece == None:
                            moves.append(square)
                        else:
                            if square.piece.value != piece.value:
                                moves.append(square)
                            break
        else:
            if piece.id > 0:
                if not piece.moved: directions.append(Vec(0,-2))
            else:
                if not piece.moved: directions.append(Vec(0,2))

            for direction in directions:
                square = self.get_target_square(current_pos+direction)
                if square != None:
                    if square.piece == None:
                        if direction == directions[0]:
                            moves.append(square)
                        if not self.piece.moved:
                            if direction == directions[3]:
                                one_square_before = self.get_target_square(current_pos+directions[0])
                                if one_square_before in moves:
                                    moves.append(square)
                    else:
                        if direction in [directions[1],directions[2]]:
                            if square.piece.value != piece.value:
                                moves.append(square)
        return moves

    def set_move(self):
        if self.piece != None and self.square != None and self.square in self.get_piece_moves():
            if self.piece.square != self.square:
                sounds_list = [
                    self.move_sound,
                    self.capture_sound,
                    self.check_sound,
                    self.castle_sound,
                    self.promote_sound
                ]
                if self.square.piece != None:
                    self.square.piece.kill()
                    sound_index = 1
                elif self.square.piece == None:
                    sound_index = 0


                for square in self.squares:
                    square.highlighted = 0
                self.piece.moved = True
                self.piece.square.highlighted = 2
                self.square.highlighted = 2
                self.piece.square.piece = None
                self.piece.rect.topleft = self.square.rect.topleft
                self.square.piece = self.piece
                self.piece.square = self.square
                self.piece = self.piece
                self.id = self.piece.id
                self.__attributes__(self.squares,self.pieces,self.piece,self.square,self.turn)
                for square_ in self.get_piece_moves():
                    if square_.piece != None:
                        if square_.piece.value != self.piece.value and abs(square_.piece.id) == 1:
                            sound_index = 2
                sounds_list[sound_index].play()
                return 1 if self.turn == -1 else -1
        else:
            self.piece.rect.topleft = self.piece.square.rect.topleft
        return self.turn