file = open("parole.txt")

#ab, cd, pq, or xy
counter = 0
vocali = "aeiou"
no = ["ab", "cd", "pq", "xy"]


for c in file:
    vowels = 0
    for i in c:
        if i in vocali:
            vowels += 1
    if vowels >= 3:
        doppie = False
        for i in range(len(c) - 1):
            if c[i] == c[i + 1]:
                doppie = True
                break
        if doppie == True:
            if "ab" not in c and "cd" not in c and "pq" not in c and "xy" not in c:
                counter += 1
print(counter)            
                
            
        
    