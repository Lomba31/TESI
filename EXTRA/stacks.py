f=open("stacks.txt")
testo=f.read()
parti=testo.split("\n\n")

stacks=parti[0]
moves=parti[1].split("\n")

stacks=stacks.split("\n")
indici_stacks=stacks[-1].strip().split() #store a list of indices corresponding to each stack
del stacks[-1]
#print(stacks)

for i in range(len(stacks)):
    l=[]
    for j in range(0,len(stacks[i]),4):
        l.append(stacks[i][j:j+3]) #append from the element i of the list 3 elements riga e colonna
    stacks[i]=l
# print(stacks)

diz_stacks={} #creo dizionario con come chiavi gli indici degli stacks e come valore la lista degli elementi di ciascuno stack
for indice in indici_stacks:
    indice=int(indice)
    diz_stacks[indice]=[] #aggiungo al dizionario chiavi come indice e ad ogni valore aggiungo le stack degli elementi di quell'indice
    for r in stacks:
        x=r[indice-1].strip()
        if len(x)>0:
            diz_stacks[indice].append(x)
# print(diz_stacks)


# for move in moves:
#     print(move)
#     move=move.strip()
#     if move:
#         move=move.split()
#         quanti=int(move[1])
#         da=int(move[3])
#         a = int(move[5])
#         for n in range(quanti):
#             x=diz_stacks[da].pop(0)
#             diz_stacks[a].insert(0,x)

for move in moves:
    move = move.strip()
    if move:
        #Split the move into its components
        move = move.split()

        #Extract the number of crates to move, the source stack, and the destination stack
        quanti = int(move[1])
        da = int(move[3])
        a = int(move[5])

        #Move the crates from the source stack to the destination stack
        crates = diz_stacks[da][:quanti]
        del diz_stacks[da][:quanti]
        diz_stacks[a] = crates + diz_stacks[a]

# print(diz_stacks)

# indici=sorted(list(diz_stacks.keys()))

# l=[]
# for indice in indici:
#     l.append(diz_stacks[indice][0])

# for i in range(len(l)):
#     l[i]=l[i][1:-1]
# print(l)
# result="".join(l)
# print(result)

# Sort the stacks by their indices
indici = sorted(list(diz_stacks.keys()))

# Print the top element of each stack
for indice in indici:
    print(diz_stacks[indice][0])