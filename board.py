import chess
import chess.svg as chess_gui
import os
import constants 

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from piece import Piece, get_fixed_s
from states import *


def prepare_folders():
    for folder_name in constants.all_folders:
        try:
            os.makedirs(folder_name)
            print('[{} created]'.format(folder_name))
        except FileExistsError:
            pass


def get_png_path(filename):
    return os.path.join(constants.PNG_FOLDER, filename)


def get_working_path(filename):
    return os.path.join(constants.WORKING_FOLDER, filename)


def get_board_from_matrix(matrix, turn):
    pieces = []
    matrix = [e.replace(' ', '') for e in matrix.split('\n')]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '.':
                continue
            pieces.append(Piece(
                i, j, matrix[i][j]
            ))
    return Board(pieces, turn)


class Board():
    def __init__(self, state = [], turn = False):
        self.pieces = state
        self.white_turn = turn


    def generate_string(self):
        result = ('8/' * 8)[:-1]
        for piece in self.pieces:
            result = piece.update_str(result)
        return result


    def get_neibhour_states(self):
        moves = self.get_chess_obj().legal_moves
        result = []
        for move in moves:
            cand = self.get_chess_obj()
            cand.push(move)
            result.append(get_board_from_matrix(str(cand), not self.white_turn))
        return result


    def get_chess_obj(self):
        result = chess.Board(self.generate_string())
        result.turn = self.white_turn

        return result


    def save_state_as_png(self, filename = 'file'):
        board = self.get_chess_obj()
    
        prepare_folders()
        boardsvg = chess_gui.board(board)
        open(get_working_path(f'{filename}.svg'), 'w').write(boardsvg)
        drawing = svg2rlg(get_working_path(f'{filename}.svg'))
        renderPM.drawToFile(drawing, get_png_path(f"{filename}.png"), fmt="PNG")


    def __str__(self):
        return str(self.get_chess_obj())
    
    
    def __repr__(self):
        return str(self)


    def __eq__(self, other):
        return (
            sorted(self.pieces) ==
            sorted(other.pieces)
        ) and self.white_turn == other.white_turn


if __name__ == '__main__':
    b = Board(bishop_end_game).get_neibhour_states()[0]
    it = 1
    for state in b.get_neibhour_states():
        state.save_state_as_png(f'{it}')
        it += 1


