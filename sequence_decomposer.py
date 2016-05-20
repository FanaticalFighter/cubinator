def decompose_sequence(move_sequence):
    """
    Decomposes a move sequence like "R U R' U R U U R" to something that can be
    executed by our hardware. Returns decomposed sequence as a string.
    """

    moves = move_sequence.split(' ')

    decomposed_sequence = ''
    for move in moves:
        if len(move) > 1 and move[1] == '2':
            decomposed_sequence += move[0] + ' ' + move[0] + ' '
            print decomposed_sequence, '***'
        else:
            decomposed_sequence += move + ' '

    moves = decomposed_sequence.split(' ')

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

    ds = decomposed_sequence[:-1].split(' ')  # remove the trailing whitespace
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

    decomposed_sequence = new_ds[:-1]  # removing the trailing whitespace

    print decomposed_sequence

    lastTurn = ''
    ds = decomposed_sequence.split(' ')

    ds.remove('')
    i = 0
    while i < len(ds):
        print ds
        if (ds[i] == 'z' or ds[i] == "z'" and lastTurn == ''):
            lastTurn = ds[i]
        elif (i < len(ds) - 1 and ((lastTurn == "z" and ds[i] == "z'") or (lastTurn == "z'" and ds[i] == "z")) and ds[i + 1][0] not in "RLzxy"):
            ds[i + 1], ds[i] = ds[i], ds[i + 1]  # swap 'z' with next move
        elif (ds[i] == lastTurn + "'" or ds[i] + "'" == lastTurn):
            lastTurn = ''

        print ds

        new_ds = ''
        for j in range(1, len(ds) + 1):
            if j < len(ds) and (ds[j - 1] == ds[j] + "'" or ds[j - 1] + "''" == ds[j]):
                skipping = True
                continue
            elif skipping:
                skipping = False
                continue
            else:
                new_ds += ds[j - 1] + ' '

        ds = new_ds[:-1].split(' ')

        i += 1



    decomposed_sequence = ' '.join(ds)

    print decomposed_sequence
    return decomposed_sequence

decompose_sequence("R U2 F U2")
