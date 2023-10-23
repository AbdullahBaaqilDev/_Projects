import pygame
from pygame.math import Vector2 as Vec
from pieces import Piece
from settings import *

class Move():
    def __init__(self, squares, Board):
        # sounds
        self.moves_sound = {sounds_name : pygame.mixer.Sound(sounds) for sounds_name, sounds in {"normal": MOVE_SOUND, "capture": CAPTURE_SOUND, "check": CHECK_SOUND, "castle": CASTLE_SOUND, "promote": PROMOTE_SOUND}.items()}

        self.squares = squares
        # board class
        self.Board = Board

    def get_castle(self, board):
        castle = {
            1: {
                "king_side": False,
                "qween_side": False
            },
            -1: {
                "king_side": False,
                "qween_side": False
            }
        }

        for piece_id in range(1, -2, -2):
            king = [piece for piece in board.pieces if piece.id == piece_id][0]
            king_right_pos = Vec(4, 7) if piece_id == 1 else Vec(4, 0)
            # king side
            if not king.moved and king.square.pos == king_right_pos:
                rook_king_square = self.get_target_square(king.square.pos + Vec(3, 0))
                if rook_king_square:
                    if rook_king_square.piece:
                        if rook_king_square.piece.id == 3 * piece_id and not rook_king_square.piece.moved:
                            if not self.get_target_square(king.square.pos + Vec(1, 0)).piece and not self.get_target_square(king.square.pos + Vec(2, 0)).piece:
                                castle[piece_id]["king_side"] = True
            # qween side
            if not king.moved and king.square.pos == king_right_pos:
                rook_qween_square = self.get_target_square(king.square.pos - Vec(4, 0))
                if rook_qween_square:
                    if rook_qween_square.piece:
                        if rook_qween_square.piece.id == 3 * piece_id and not rook_qween_square.piece.moved:
                            if not self.get_target_square(king.square.pos - Vec(1, 0)).piece and not self.get_target_square(king.square.pos - Vec(2, 0)).piece and not self.get_target_square(king.square.pos - Vec(3, 0)).piece:
                                castle[piece_id]["qween_side"] = True
        return castle

    def get_target_square(self, target_pos):
        for square in self.squares:
            if square.pos == target_pos:
                return square

    def get_legal_moves(self, board, piece):
        legal_moves = []

        if piece.id / abs(piece.id) == board.turn:
            if abs(piece.id) in [1,5,6]:
                moves = [Vec(move) for move in SHORT_PIECES_MOVES[Piece.symbol_from_id[abs(piece.id) * -1]]]
                is_long_range = False
            else:
                directions = [Vec(direction) for direction in LONG_PIECES_DIRECTIONS[Piece.symbol_from_id[abs(piece.id) * -1]]]
                is_long_range = True

            if is_long_range:
                for piece_square in board.squares:
                    if piece_square.piece == piece:
                        for direction in directions:
                            for index in range(8):
                                # we add 1 to the index so it doesn't count the square that the piece stand on
                                square = self.get_target_square(piece_square.pos + direction * (index + 1))
                                if square:
                                    if square.piece:
                                        # checking if the piece is enemy or friendly
                                        if square.piece.id < 0 and piece.id > 0 or square.piece.id > 0 and piece.id < 0:
                                            legal_moves.append(square)
                                        break
                                    else: legal_moves.append(square)
            else:
                if piece.id == -6:
                    for index,move in enumerate(moves):
                        moves[index] = move * -1
                castle = self.get_castle(board)

                for piece_square in board.squares:
                    if piece_square.piece == piece:
                        for move in moves:
                            square = self.get_target_square(piece.square.pos + move)
                            if square:
                                if square.piece:
                                    if square.piece.id < 0 and piece.id > 0 or square.piece.id > 0 and piece.id < 0:
                                        if abs(piece.id) == 6:
                                            if move in moves[2:]:
                                                legal_moves.append(square)
                                        else: legal_moves.append(square)
                                else:
                                    if abs(piece.id) == 6:
                                        if move == moves[1]:
                                            if moves[0] + piece.square.pos in [square.pos for square in legal_moves]:
                                                if (piece.square.pos.y == 6 and piece.id > 0 or piece.square.pos.y == 1 and piece.id < 0) and not piece.moved:
                                                    legal_moves.append(square)
                                        elif not move in moves[2:]:
                                            legal_moves.append(square)
                                        
                                        # en passant
                                        if piece.id < 0:
                                            if move == moves[3]:
                                                king_side_square = self.get_target_square(piece.square.pos + Vec(1, 0))
                                                if king_side_square:
                                                    if king_side_square.piece:
                                                        if abs(king_side_square.piece.id) == 6:
                                                            if king_side_square.piece.en_passant:
                                                                legal_moves.append(square)
                                            elif move == moves[2]:
                                                qween_side_square = self.get_target_square(piece.square.pos + Vec(-1, 0))
                                                if qween_side_square:
                                                    if qween_side_square.piece:
                                                        if abs(qween_side_square.piece.id) == 6:
                                                            if qween_side_square.piece.en_passant:
                                                                legal_moves.append(square)
                                        else:
                                            if move == moves[2]:
                                                king_side_square = self.get_target_square(piece.square.pos + Vec(1, 0))
                                                if king_side_square:
                                                    if king_side_square.piece:
                                                        if abs(king_side_square.piece.id) == 6:
                                                            if king_side_square.piece.en_passant:
                                                                legal_moves.append(square)
                                            elif move == moves[3]:
                                                qween_side_square = self.get_target_square(piece.square.pos + Vec(-1, 0))
                                                if qween_side_square:
                                                    if qween_side_square.piece:
                                                        if abs(qween_side_square.piece.id) == 6:
                                                            if qween_side_square.piece.en_passant:
                                                                legal_moves.append(square)
                                    elif abs(piece.id) == 1 and move in [Vec(2, 0), Vec(-2, 0)]:
                                        if castle[piece.id]["king_side"]:
                                            legal_moves.append(square)
                                        if castle[piece.id]["qween_side"]:
                                            legal_moves.append(square)
                                    else: legal_moves.append(square)
        return legal_moves
    
    def filter_legal_moves(self, piece, board):
        # filtering the legal moves like if there was a check or a pin
        legal_moves = []
        pieces_legal_moves = {}
        opponent_legal_moves = {}
        if piece.id < 0:
            for white_piece in board.white_pieces: opponent_legal_moves[white_piece] = self.get_legal_moves(board, white_piece)
        else:
            for black_piece in board.black_pieces: opponent_legal_moves[black_piece] = self.get_legal_moves(board, black_piece)
        

        return legal_moves

    def move(self, piece, target_square):
        if piece.square.pos != target_square.pos:
            move_sound = "normal"
            # en passant rule and promote to a qween
            if abs(piece.id) == 6:
                # checking if the pawn moved 2 steps and there is an oopponent piece next to it
                duoble_square = Vec(0, -2) if piece.id > 0 else Vec(0, 2)
                king_side_en_passant = self.get_target_square(target_square.pos + Vec(1, 0))
                qween_side_en_passant = self.get_target_square(target_square.pos + Vec(-1, 0))
                if king_side_en_passant:
                    if piece.square.pos + duoble_square == target_square.pos and \
                        king_side_en_passant.piece: piece.en_passant = True
                if qween_side_en_passant:
                    if piece.square.pos + duoble_square == target_square.pos and \
                        qween_side_en_passant.piece: piece.en_passant = True
                
                # checking if the move was en passant
                behind_piece = Vec(0, 1) if piece.id > 0 else Vec(0, -1)
                square_behind_piece = self.get_target_square(target_square.pos + behind_piece)
                if square_behind_piece.piece:
                    if abs(square_behind_piece.piece.id) == 6:
                        if square_behind_piece.piece != piece and square_behind_piece.piece.en_passant:
                            square_behind_piece.piece.kill()
                            square_behind_piece.piece = None
                            move_sound = "capture"
                
                # promote
                if target_square.pos.y == 0 and piece.id > 0 or target_square.pos.y == 7 and piece.id < 0:
                    # if the piece is black then piece.id = -1 * 2 wich is -2 black qweens id and same for white
                    piece.id = int((piece.id / abs(piece.id)) * 2)
                    move_sound = "promote"
            
            elif abs(piece.id) == 1:
                # castling the king
                if target_square.pos - piece.square.pos == Vec(2, 0):
                    self.move(self.get_target_square(target_square.pos + Vec(1, 0)).piece, self.get_target_square(target_square.pos - Vec(1, 0)))
                    move_sound = "castle"
                elif target_square.pos - piece.square.pos == Vec(-2, 0):
                    self.move(self.get_target_square(target_square.pos - Vec(2, 0)).piece, self.get_target_square(target_square.pos + Vec(1, 0)))
                    move_sound = "castle"
                
            if target_square.piece:
                target_square.piece.kill()
                if move_sound not in ["promote", "castle", "check"]: move_sound = "capture"
            piece.square.piece = None
            target_square.piece = piece
            piece.move_to(target_square)
            piece.moved = True
            if move_sound: self.moves_sound.get(move_sound).play()
            
            # checking if there is a new pawn can be en passant
            if abs(piece.id) == 6:
                if piece.en_passant: return piece