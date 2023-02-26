with open("rock.txt") as f:
    data = [i for i in f.read().split("\n") if i!= ""]
    

print(data)

count = 0

for i in data:
    if i[0]== "A":
        count = count + 1
        if i[2]== "X":
            count += 3
        elif i[2]== "Y":
            count += 6
        elif i[2] == "Z":
            count += 0
    elif i[0] == "B":
        count = count + 2
        if i[2]== "X":
            count += 0
        elif i[2] == "Y":
            count += 3
        else:
            count += 6
    elif i[0] == "C":
        count = count + 2
        if i[2] == "X":
            count += 6
        elif i[2] == "Y":
            count += 0
        else:
            count += 3

print(count)