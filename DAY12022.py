file = open("day12022.txt", "r")

# s_max = 0
# s = 0
# for riga in file:
#     r = riga.strip()
#     if r :
#         N = int(r)
#         s += N
#     else:
#         print(s)
#         if s > s_max:
#             s_max = s
#         s = 0
# print(s)
# if s > s_max:
#     s_max = s
# print("****", s_max)

list = []
s = 0
for riga in file:
    r = riga.strip()
    if r :
        N = int(r)
        s += N
    else :
        print(s)
        list.append(s)
        s = 0
print(s)
list.append(s)
list.sort(reverse=True)
print("****", sum(list[:3]))


