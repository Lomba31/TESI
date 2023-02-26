# Getting Data
with open("day1.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

# Traversing every string in our Data
count = 0
elves = []

for item in data:
    if item == "":
        elves.append(count)
        count = 0
    else:
        num = int(item)
        count += num

# Append the final count to the list of Elves
elves.append(count)

# Sort the list of Elves in descending order
elves.sort(reverse=True)

# Take the sum of the first three Elves
result = sum(elves[:3])

print(result)
