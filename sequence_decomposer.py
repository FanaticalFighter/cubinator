from cube import *

def decompose_sequence(move_sequence):
    """
    Decomposes a move sequence like "R U R' U R U U R" to something that can be
    executed by our hardware. Returns decomposed sequence as a string.
    """

    moves = move_sequence.split(' ')

    decomposed_sequence = ''

    for move in moves:
        current_move = move
        if move in ["U", "U'", "D", "D'"]:
            if move == "U" or move == "U'":
                pass
            else if move == "D" or move == "D'":
                pass

        decompose_sequence += current_move + ' '
