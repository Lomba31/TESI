file = open("rettangoli.txt")

dimensioni = file.readlines()
# dimensioni = ("2x3x4", "1x1x10")

# formula = 2*l*w + 2*w*h + 2*h*l
sup = 0
for d in dimensioni:
    d = d.split("x")
    l = int(d[0])
    w = int(d[1])
    h = int(d[2])
    print(l, w, h)  
    sup += 2*l*w + 2*w*h + 2*h*l
    g = [l, w, h]
    g.sort()
    p = g[0]*g[1]
    sup += p
print(sup)


for d in dimensioni:
    d = d.split("x")
    l = int(d[0])
    w = int(d[1])
    h = int(d[2])
    g = [l, w, h]
    g.sort()
    p = 2*(g[0] + g[1])
    sup += l * w * h
    sup += p
print(sup)

