file = open("frequenze.txt")
"""
frequenza = 0
for riga in file:
    n = int(riga)
    frequenza += n
print(frequenza)
"""
freq = [0]
frequenza = 0
for riga in file:
    n = int(riga)
    if n >= 0: 
        for f in range(frequenza + 1, frequenza + n + 1):
            freq.append(f)
    else:
        for f in range(frequenza - 1, frequenza + n - 1, -1):
            freq.append(f)

for c in freq:
    if freq.count(c) > 1:
        print(c)
        break
  