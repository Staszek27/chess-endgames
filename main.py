from board import *
from states import all_states
from constants import *
from random import shuffle

import imageio
import os


def get_neib_states(chains):
    result = []
    for chain in chains:
        if not chain[-1].its_a_win():
            if chain[-1].white_turn:
                cands = chain[-1].get_neibhour_states()
                shuffle(cands)
                cands = cands[:NUMBER_OF_NEIBS]
                for neib in cands:
                    result.append(chain + [neib])
            else:
                try:
                    worst_state = min(chain[-1].get_neibhour_states())
                    result.append(chain + [worst_state])
                except ValueError:
                    pass
        else:
            result.append(chain)
        
    return result


def get_best_segments(chains):
    for i in range(MOVES_IN_SEGMENT):
        chains = get_neib_states(chains)
    return chains


def get_filtred_by_number_of_pieces(chains):
    return [chain for chain in chains 
            if len(chain[0].pieces) == len(chain[-1].pieces)]


def get_boards_chain(initial_board):
    chains = [[initial_board]]
    cnt = 0
    while True:
        chains = get_best_segments(chains)
        chains = get_filtred_by_number_of_pieces(chains)
        chains = sorted(chains)[:NUMBER_OF_SEGMENTS]
        cnt += 1
        print('step = {}, chains = {}'.format(cnt, len(chains)))
        for chain in chains:
            if chain[-1].its_a_win():
                return chain
        
        if cnt == 10:
            print('something went wrong..')
            return chains[0]


def get_images_chain(name, boards_chain):
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



def generate_gif(name, images_names):
    imageio.mimsave(
        os.path.join(GIF_FOLDER, f'{name}.gif'),
        [imageio.imread(e) for e in images_names]
    )


if __name__ == '__main__':

    prepare_folders()
    for state_name, state_pieces in all_states.items():
        generate_gif(
            state_name, 
            get_images_chain(
                state_name, 
                get_boards_chain(Board(state_pieces))
        ))    
        

