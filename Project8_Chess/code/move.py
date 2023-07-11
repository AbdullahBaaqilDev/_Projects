import pygame
from pygame import Vector2 as Vec
from settings import *

class Move():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.turn = 0
        self.move_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\move.wav")
        self.capture_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\capture.wav")
        self.check_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\check.wav")
        self.castle_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\castle.wav")
        self.promote_sound = pygame.mixer.Sound(f"{ASSETS_FOLDER}\\sounds\\promote.wav")
        self.sounds_list = {
            "normal":self.move_sound,
            "capture":self.capture_sound,
            "check":self.check_sound,
            "castle":self.castle_sound,
            "promote":self.promote_sound
        }
        self.pieces_directions = {
            1:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
            2:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
            3:[Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
            4:[Vec(-2,1),Vec(-2,-1),Vec(2,1),Vec(2,-1),Vec(1,2),Vec(-1,2),Vec(1,-2),Vec(-1,-2),],
            5:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),],
            6:[Vec(0,-1),Vec(1,-1),Vec(-1,-1)],
            -6:[Vec(0,1),Vec(-1,1),Vec(1,1)],
        }

    def update_attributes(self,squares=None,pieces=None,piece=None,square=None):
        self.squares = squares
        self.pieces = pieces
        self.piece = piece
        self.square = square
        self.current_pos = Vec(self.piece.square.pos) if piece != None else None

    def get_target_square(self,target_pos):
        target = None
        for square in self.squares:
            if square.pos == target_pos:
                target = square
                return target
        return target
    
    def get_castle_pieces(self):
        for piece_ in self.pieces.sprites():
            if piece_.id == 1:
                white_king = piece_
            elif piece_.id == 5:
                if piece_.square.pos == Vec(7,7):
                    white_rookK = piece_
                elif piece_.square.pos == Vec(0,7):
                    white_rookQ = piece_
            if piece_.id == -1:
                black_king = piece_
            elif piece_.id == -5:
                if piece_.square.pos == Vec(7,0):
                    black_rookK = piece_
                elif piece_.square.pos == Vec(0,0):
                    black_rookQ = piece_

        return {"king":white_king,"rookK":white_rookK,"rookQ":white_rookQ},{"king":black_king,"rookK":black_rookK,"rookQ":black_rookQ}

    def get_castle(self,return_bool=False):
        castle = {"white_ck":"-","white_cq":"-","black_ck":"-","black_cq":"-"}
        white,black = self.get_castle_pieces()
        white_ck = True
        white_cq = True
        
        if white["king"].moved:
            white_ck = False
            white_cq = False
        if white["rookK"].moved:
            white_ck = False
        if white["rookQ"].moved:
            white_cq = False

        black_ck = True
        black_cq = True
        if black["king"].moved:
            black_ck = False
            black_cq = False
        if black["rookK"].moved:
            black_ck = False
        if black["rookQ"].moved:
            black_cq = False

        if not return_bool:
            if white_ck: castle["white_ck"] = "K"
            if white_cq: castle["white_cq"] = "Q"
            if black_ck: castle["black_ck"] = "k"
            if black_cq: castle["black_cq"] = "q"
        else:
            castle["white_ck"] = white_ck
            castle["white_cq"] = white_cq
            castle["black_ck"] = black_ck
            castle["black_cq"] = black_cq
        
        return castle
    
    def is_check(self,piece):
        for piece_ in self.pieces.sprites():
            if piece_.value == piece.value:
                for square_ in list(self.get_piece_moves(piece_.square.pos,piece_,piece_.value).keys()):
                    if square_.piece != None and square_.piece.id == piece.value * -1:
                        return True
        return False
    
    def get_piece_moves(self,current_pos = None,piece = None,turn = None):
        if current_pos == None:
            current_pos = self.current_pos
        if piece == None:
            piece = self.piece
        if turn == None:
            turn = self.turn
        
        moves = {}
        direction_range = range(1,9) if piece.is_long_range else range(1,2)
        if piece.id in list(self.pieces_directions.keys()): directions = self.pieces_directions[piece.id]
        else: directions = self.pieces_directions[abs(piece.id)]

        if abs(piece.id) != 6:
            castle = self.get_castle(True)
            if piece.id == 1:
                if castle["white_ck"] and self.get_target_square(Vec(6,7)).piece == None and self.get_target_square(Vec(5,7)).piece == None:
                    directions.append(Vec(2,0))
                if castle["white_cq"] and self.get_target_square(Vec(4,7)).piece == None and self.get_target_square(Vec(3,7)).piece == None and self.get_target_square(Vec(2,7)).piece == None and self.get_target_square(Vec(1,7)).piece == None:
                    directions.append(Vec(-2,0))
            elif piece.id == -1:
                if castle["black_ck"] and self.get_target_square(Vec(6,0)).piece == None and self.get_target_square(Vec(5,0)).piece == None:
                    directions.append(Vec(2,0))
                if castle["black_cq"] and self.get_target_square(Vec(4,0)).piece == None and self.get_target_square(Vec(3,0)).piece == None and self.get_target_square(Vec(2,0)).piece == None and self.get_target_square(Vec(1,0)).piece == None:
                    directions.append(Vec(-2,0))
            for direction in directions:
                for index in direction_range:
                    square = self.get_target_square(current_pos+direction*index)
                    if square != None:
                        if square.piece == None:
                            moves[square] = "normal"
                            if piece.id == piece.value and direction in [Vec(2,0),Vec(-2,0)]:
                                moves[square] = "castle"
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
                square = self.get_target_square(current_pos+direction)
                if square != None:
                    if square.piece == None:
                        if direction == directions[0]:
                            moves[square] = "normal"
                        if not self.piece.moved:
                            if direction == directions[3]:
                                one_square_before = self.get_target_square(current_pos+directions[0])
                                if one_square_before in moves:
                                    moves[square] = "normal"
                    else:
                        if direction in [directions[1],directions[2]]:
                            if square.piece.value != piece.value:
                                moves[square] = "capture"
        return moves

    def set_move(self,turn = None,piece = None,square = None):
        if turn == None:
            turn = self.turn
        if piece == None:
            piece = self.piece
        if square == None:
            square = self.square
        if square in list(self.get_piece_moves().keys()) and piece.square != square:
            # set move sound
            move_type = self.get_piece_moves()[square]
            if move_type == "capture":
                square.piece.kill()

            for square_ in self.squares:
                square_.highlighted = 0
            piece.square.highlighted = 2
            square.highlighted = 2

            piece.moved = True
            piece.square.piece = None
            piece.rect.topleft = square.rect.topleft
            square.piece = piece
            piece.square = square
            self.turn *= -1
            self.update_attributes(self.squares,self.pieces,piece,square)

            if self.is_check(piece):
                move_type = "check"
            self.sounds_list[move_type].play()
        else:
            self.piece.rect.topleft = self.piece.square.rect.topleft
        return self.turn