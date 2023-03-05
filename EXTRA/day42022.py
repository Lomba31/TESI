file = open("coppie.txt")
coppie = file.readlines()

assignment = 0
for coppia in coppie:
    coppia = coppia.strip().split(",")
    coppia0 = coppia[0].split("-")
    coppia1 = coppia[1].split("-")
    if int(coppia0[0]) >= int(coppia1[0]) and int(coppia0[1]) <= int(coppia1[1]) or int(coppia1[0]) >= int(coppia0[0]) and int(coppia1[1]) <= int(coppia0[1]):
        assignment += 1
        
print(assignment)

assignment1 = 0
for coppia in coppie:
    coppia = coppia.strip().split(",")
    coppia0 = coppia[0].split("-")
    coppia1 = coppia[1].split("-")
    if int(coppia0[0]) >= int(coppia1[0]) and int(coppia0[0]) <= int(coppia1[1]) \
    or int(coppia0[1]) >= int(coppia1[0]) and int(coppia0[1]) <= int(coppia1[1]) \
    or int(coppia1[0]) >= int(coppia0[0]) and int(coppia1[0]) <= int(coppia0[1]) \
    and int(coppia1[1]) >= int(coppia0[0]) and int(coppia1[1]) <= int(coppia0[1]):
        assignment1 += 1
print(assignment1)