file = open("calories.txt")

elfs = [
]
elfi = 0

for i in file:
    i = i.strip()
    if i == "":
        pass
    else:
        i = str(i)
        elfi += i
        elfs.append(elfi)
print(max(elfs))