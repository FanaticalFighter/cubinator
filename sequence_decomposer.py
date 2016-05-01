from cube import *

def decompose_sequence(move_sequence):
    """
    Decomposes a move sequence like "R U R' U R U U R" to something that can be
    executed by our hardware.
    """

    moves = move_sequence.split(' ')

    decomposed_sequence = ''

    for move in moves:
        if move == "U" or move == "U'":
            pass
        else if move == "D" or move == "D'":
            pass
