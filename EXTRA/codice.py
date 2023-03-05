file = open("codice.txt")

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# s = ""

# pos = (1, 1)
# for riga in file:
#     print(riga)
#     riga = riga.strip()
#     for c in riga:
#         if c == "U":
#             if pos[0] == 0:
#                 print(pos)
#                 continue
#             else:
#                 pos = (pos[0] - 1, pos[1])
#         elif c == "R":
#             if pos[1] == 2:
#                 print(pos)
#                 continue
#             else:
#                 pos = (pos[0], pos[1] + 1)            
#         elif c == "D":
#             if pos[0] == 2:
#                 print(pos)
#                 continue
#             else:
#                 pos = (pos[0] + 1, pos[1])
#         else:
#             if pos[1] == 0:
#                 print(pos)
#                 continue
#             else:
#                 pos = (pos[0], pos[1] - 1)
#     s += str(l[pos[0]][pos[1]])
# print(s)

l = [[1], [2, 3, 4], [5, 6, 7, 8], ["A", "B", "C"]]
s = ""

pos = (1, 1)
for riga in file:
    print(riga)
    riga = riga.strip()
    for c in riga:
        if c == "U":
            if pos[0] == 0:
                print(pos)
                continue
            else:
                pos = (pos[0] - 1, pos[1])
        elif c == "R":
            if pos[1] == 2:
                print(pos)
                continue
            else:
                pos = (pos[0], pos[1] + 1)            
        elif c == "D":
            if pos[0] == 2:
                print(pos)
                continue
            else:
                pos = (pos[0] + 1, pos[1])
        else:
            if pos[1] == 0:
                print(pos)
                continue
            else:
                pos = (pos[0], pos[1] - 1)
    s += str(l[pos[0]][pos[1]])
print(s)
