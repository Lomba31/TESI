blocchi = open("blocchi.txt").readline().strip()

lista = blocchi.split(", ")

dir = "N"
pos = [0, 0]
""""
posizioni = []

for c in lista:
    n = int(c[1:])
    d = c[0]
    if d == "L":
        if dir == "N":
            pos = [pos[0] - n, pos[1]]
            dir = "W"
        elif dir == "W":
            pos = [pos[0], pos[1] - n]
            dir = "S"
        elif dir == "S":
            pos = [pos[0] + n, pos[1]]
            dir = "E"
        elif dir == "E":
            pos = [pos[0], pos[1] + n]
            dir = "N"
    elif d == "R":
        if dir == "N":
            pos = [pos[0] + n, pos[1]]
            dir = "E"
        elif dir == "W":
            pos = [pos[0], pos[1] + n]
            dir = "N"
        elif dir == "S":
            pos = [pos[0] - n, pos[1]]
            dir = "W"
        elif dir == "E":
            pos = [pos[0], pos[1] - n]
            dir = "S"

print(pos)
d = abs(pos[0]) + abs(pos[1])
print(d)
"""

posizioni = [[0, 0]]

for c in lista:
    n = int(c[1:])
    d = c[0]
    if d == "L":
        if dir == "N":
            for h in range(pos[0] - 1, pos[0] - n - 1, -1):
                posizioni.append([h, pos[1]])
            pos = [pos[0] - n, pos[1]]
            dir = "W"
        elif dir == "W":
            for h in range(pos[1] - 1, pos[1] - n - 1, -1):
                posizioni.append([pos[0], h])
            pos = [pos[0], pos[1] - n]
            dir = "S"
        elif dir == "S":
            for h in range(pos[0] + 1, pos[0] + n + 1):
                posizioni.append([h, pos[1]])
            pos = [pos[0] + n, pos[1]]
            dir = "E"
        elif dir == "E":
            for h in range(pos[1] + 1, pos[1] + n + 1):
                posizioni.append([pos[0], h])
            pos = [pos[0], pos[1] + n]
            dir = "N"
    elif d == "R":
        if dir == "N":
            for h in range(pos[0] + 1, pos[0] + n + 1):
                posizioni.append([h, pos[1]])
            pos = [pos[0] + n, pos[1]]
            dir = "E"
        elif dir == "W":
            for h in range(pos[1] + 1, pos[1] + n + 1):
                posizioni.append([pos[0], h])
            pos = [pos[0], pos[1] + n]
            dir = "N"
        elif dir == "S":
            for h in range(pos[0] - 1, pos[0] - n - 1, -1):
                posizioni.append([h, pos[1]])
            pos = [pos[0] - n, pos[1]]
            dir = "W"
        elif dir == "E":
            for h in range(pos[1] - 1, pos[1] - n - 1, -1):
                posizioni.append([pos[0], h])
            pos = [pos[0], pos[1] - n]
            dir = "S"   

for p in posizioni:
    if posizioni.count(p) > 1:
        print(p)
        break
print(posizioni)


