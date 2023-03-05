file = open("captcha.txt").readline().strip()

somma = 0
"""
for i in range(len(file) - 1):
    if file[i] == file[i + 1]:
        somma += int(file[i])

if file[0] == file[len(file) - 1]:
    somma += int(file[0])
print(somma)
"""
lunghezza = len(file)//2
for i in range(len(file)):
    if file[i] == file[(i + lunghezza) % len(file)]:
        somma += int(file[i])
print(somma)