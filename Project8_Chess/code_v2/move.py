import pygame
from pygame.math import Vector2 as Vec
from pieces import Piece
from settings import *

class Move():
    def __init__(self, Board):
        # sounds
        self.move_sound = pygame.mixer.Sound(MOVE_SOUND)
        self.capture_sound = pygame.mixer.Sound(CAPTURE_SOUND)
        self.check_sound = pygame.mixer.Sound(CHECK_SOUND)
        self.castle_sound = pygame.mixer.Sound(CASTLE_SOUND)
        self.promote_sound = pygame.mixer.Sound(PROMOTE_SOUND)

        # board class
        self.Board = Board

    def get_castle(self, board):
        pass
    
    def get_target_square(self, squares, target_pos):
        for square in squares:
            if square.pos == target_pos:
                return square

    def get_legal_moves(self, board, piece):
        legal_moves = []

        if abs(piece.id) in [1,5,6]:
            moves = [Vec(move) for move in SHORT_PIECES_MOVES[Piece.symbol_from_id[abs(piece.id)]]]
            is_long_range = False
        else:
            directions = [Vec(direction) for direction in LONG_PIECES_DIRECTIONS[Piece.symbol_from_id[abs(piece.id)]]]
            is_long_range = True

        if is_long_range:
            for piece_square in board.squares:
                if piece_square.piece == piece:
                    for direction in directions:
                        for index in range(8):
                            # we add 1 to the index so it doesn't count the square that the piece stand on
                            square = self.get_target_square(board.squares, piece_square.pos + Vec(direction) * (index + 1))
                            if square:
                                if square.piece:
                                    # checking if the piece is enemy or friendly
                                    if square.piece.id < 0 and piece.id > 0 or square.piece.id > 0 and piece.id < 0:
                                        legal_moves.append(square)
                                    break
                                else: legal_moves.append(square)
        else:
            if piece.id == -6:
                pass

            for piece_square in board.squares:
                if piece_square.piece == piece:
                    for move in moves:
                        square = self.get_target_square(board.squares, piece.square.pos + move)
                        if square:
                            if square.piece:
                                if square.piece.id < 0 and piece.id > 0 or square.piece.id > 0 and piece.id < 0:
                                    if abs(piece.id) == 6:
                                        if move == moves[1]:
                                            if moves[0] in legal_moves:
                                                legal_moves.append(move)
                                        if move in moves[2:] and square.piece:
                                            legal_moves.append(square)
                                    else: legal_moves.append(square)
                            else: legal_moves.append(square)
        return legal_moves

    def move(self, piece, target_square):
        if target_square.piece:
            target_square.piece.kill()
        piece.square.piece = None
        target_square.piece = piece
        piece.move_to(target_square)