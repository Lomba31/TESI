with open("stacks.txt") as file:
    stacks = []
    moves = []
    primaparte = True
    for riga in file:
        if len(riga) == 0:
            primaparte = False
        if primaparte:
            stacks.append(riga)
        else:
            if len(riga) > 0:
                moves.append(riga)
print(stacks)
print(moves)