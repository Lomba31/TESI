file = open("fuel2019.txt")

counter = 0
""""
for c in file:
    c = int(c)
    f = c // 3 - 2
    counter += f
print(counter)
"""

for c in file:
    c = int(c)
    c = c // 3 - 2
    while c > 0:
        counter += c
        c = c // 3 - 2
print(counter)
         
