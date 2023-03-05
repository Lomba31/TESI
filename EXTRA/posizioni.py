file = open("posizioni.txt")

s = set()
s.add((0, 0))
file = file.read().strip()

# pos = (0, 0)
# for c in file:
#     if c == "^":
#         pos = (pos[0], pos[1] + 1)
#         s.add(pos)
#     elif c == ">":
#         pos = (pos[0] + 1, pos[1])
#         s.add(pos)
#     elif c == "<":
#         pos = (pos[0] - 1, pos[1])
#         s.add(pos)
#     else:
#         pos = (pos[0], pos[1] -1)
#         s.add(pos)
# print(len(s))

pos = (0, 0)
pos1 = (0, 0)
for i in range(len(file)): #se uso range itero sugli indici
    if i % 2 == 0:
        if file[i] == "^":
            pos = (pos[0], pos[1] + 1)
            s.add(pos)
        elif file[i] == ">":
            pos = (pos[0] + 1, pos[1])
            s.add(pos)
        elif file[i] == "<":
            pos = (pos[0] - 1, pos[1])
            s.add(pos)
        else:
            pos = (pos[0], pos[1] -1)
            s.add(pos)
    else:
        if file[i] == "^":
            pos1 = (pos1[0], pos1[1] + 1)
            s.add(pos1)
        elif file[i] == ">":
            pos1 = (pos1[0] + 1, pos1[1])
            s.add(pos1)
        elif file[i] == "<":
            pos1 = (pos1[0] - 1, pos1[1])
            s.add(pos1)
        else:
            pos1 = (pos1[0], pos1[1] -1)
            s.add(pos1)        
        
print(len(s))

