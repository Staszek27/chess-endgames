from piece import Piece

# bishop_end_game = [
#     Piece(7, 0, 'B'),
#     Piece(7, 1, 'B'),
#     Piece(7, 7, 'K'),
#     Piece(3, 3, 'k'),
# ]

rook_end_game = [
    Piece(7, 0, 'R'),
    Piece(7, 7, 'K'),
    Piece(3, 3, 'k'),
]

queen_end_game = [
    Piece(7, 0, 'Q'),
    Piece(7, 7, 'K'),
    Piece(3, 3, 'k'),
]

all_states = dict([
    (key, val) for key, val in locals().items()
        if type(val) == list
])
