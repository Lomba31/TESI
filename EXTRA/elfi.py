with open('calories.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

elf_sum = 0
elfi = []
for entry in calories:
    if entry != "":
        elf_sum += int(entry)
    elif entry == "":
        elfi.append(elf_sum)
        elf_sum = 0

print(max(elfi))

elfi = elfi.sort(reverse = True)
print("****", sum(elfi[:3]))
