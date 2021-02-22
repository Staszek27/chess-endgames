from piece import Piece

bishop_end_game = [
    Piece(7, 0, 'B'),
    Piece(7, 1, 'B'),
    Piece(7, 7, 'K'),
    Piece(0, 7, 'k')
]

all_states = dict([
    (key, val) for key, val in locals().items()
        if type(val) == list
])
