import chess
import chess.svg as chess_gui
import os
import constants 

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from piece import Piece
from states import *


def prepare_folders():
    for folder_name in constants.all_folders:
        try:
            os.makedirs(folder_name)
            print('[{} created]'.format(folder_name))
        except FileExistsError:
            print('[{} already exists]'.format(folder_name))


def get_png_path(filename):
    return os.path.join(constants.PNG_FOLDER, filename)


def get_working_path(filename):
    return os.path.join(constants.WORKING_FOLDER, filename)



class Board():
    def __init__(self, state = []):
        self.pieces = state
        self.white_turn = False


    def generate_string(self):
        result = ('8/' * 8)[:-1]
        for piece in self.pieces:
            result = piece.update_str(result)
        return result


    def get_chess_obj(self):
        return chess.Board(self.generate_string())


    def save_state_as_png(self):
        board = self.get_chess_obj()
    
        prepare_folders()
        boardsvg = chess_gui.board(board)
        open(get_working_path('file.svg'), 'w').write(boardsvg)
        drawing = svg2rlg(get_working_path('file.svg'))
        renderPM.drawToFile(drawing, get_png_path("file.png"), fmt="PNG")


    def __str__(self):
        return str(self.get_chess_obj())
    
    
    def __repr__(self):
        return str(self)


b = Board(bishop_end_game)
b.save_state_as_png()
print(str(b)) 
