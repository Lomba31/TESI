file = open("calories.txt", "r")

list = []
s = 0
for t in file:
    r = t.strip()
    if r:
        N = int(r)
        s += N
    else:
        print(s)
        list.append(s)
        s=0
print(s)
list.append(s)
list.sort(reverse=True)
print("****", sum(list[:3]))
        