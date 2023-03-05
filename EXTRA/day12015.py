with open("scale.txt") as f:
    floor = f.readline().strip()
    
    scale = floor.count("(")
    scale1 = floor.count(")")
    
    print(scale - scale1)
    
testo = open("scale.txt").readline().strip()

floor = 0
i = -1

while i < len(testo) and floor != -1:
    i += 1
    if testo[i] == "(":
        floor += 1
    else:
        floor -= 1
if floor == -1:
    print(i)
else:
    print("NO")
    
