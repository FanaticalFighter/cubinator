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

    print decomposed_sequence

    ds = decomposed_sequence.split(' ')
    new_ds = ''
    skipping = False

    for i in range(1, len(ds) + 1):
        if i < len(ds) and (ds[i - 1] == ds[i] + "'" or ds[i - 1] + "''" == ds[i]):
            skipping = True
            continue
        elif skipping:
            skipping = False
            continue
        else:
            new_ds += ds[i - 1] + ' '

    decomposed_sequence = new_ds

    print decomposed_sequence
    return decomposed_sequence

decompose_sequence("R U R' U R U U R'")
