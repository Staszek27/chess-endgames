from board import *
from states import all_states
from constants import *

import imageio
import os





def get_boards_chain(initial_board):
    return [Board(bishop_end_game if i % 2 == 0 else rook_end_game)
                for i in range(10)]


def get_images_chain(name, initial_board):
    boards_chain = get_boards_chain(initial_board)
    images_names = []

    cnt = 0
    for board in boards_chain:
        png_name = f'{name}{cnt}'
        board.save_state_as_png(png_name)
        images_names.append(os.path.join(
            PNG_FOLDER,
            f'{png_name}.png'
        ))
        cnt += 1
    return images_names



def generate_gif(name, initial_board):
    images_names = get_images_chain(name, initial_board)
    imageio.mimsave(
        os.path.join(GIF_FOLDER, f'{name}.gif'),
        [imageio.imread(e) for e in images_names]
    )


if __name__ == '__main__':
    prepare_folders()
    for state_name, state_pieces in all_states.items():
        generate_gif(state_name, Board(state_pieces))    

