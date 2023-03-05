file = open("marker.txt")
letters = file.read().strip()

# for i in range(0, len(letters) - 3):
#     s = letters[i:i+4]
#     if s[0] != s[1] and s[0] != s[2] and s[0] != s[3] and s[1] != s[2] and s[1] != s[3] and s[2] != s[3]:
#         print(i+4)
#         break
    
for i in range(0, len(letters) - 3):
    s = letters[i:i+14]
    if len(set(s)) == 14:
        print(i+14)
        break


