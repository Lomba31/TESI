#Getting Data
with open("day1.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

#Traversing every string in our Data
count = 0
max = 0
max2 = 0
max3 = 0

for item in data:
    if item == "":
        count = 0
    else:
        num = int(item)
        count += num

    if count > max:
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count
    
print(max)
print(max + max2 + max3)

