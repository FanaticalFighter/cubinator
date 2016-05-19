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
            current_move = "z "
            if move == "U":
                current_move += "R "
            elif move == "U'":
                current_move += "R' "
            elif move == "D":
                current_move += "L' "
            elif move == "D'":
                current_move += "L "
            current_move += "z'"

        decomposed_sequence += current_move + ' '

    return decomposed_sequence

print decompose_sequence("R U R' U R U U R")
