file = open("numeri.txt")

file = file.readline().split(",")

for i in range(len(file)):
    file[i] = int(file[i])

file[1] = 12
file[2] = 2

i = 0 
while i < len(file) and file[i] != 99:
    opcode = file[i]
    op1 = file[file[i + 1]]
    op2 = file[file[i + 2]]
    if opcode == 1:
        file[file[i + 3]] = op1 + op2
    elif opcode == 2:
        file[file[i + 3]] = op1 * op2
    i += 4
    
print(file[0])
    
