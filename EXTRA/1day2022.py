with open("calories.txt") as f:
    data = f.read().splitlines()
  
s_max = 0 
s = 0
for t in data:
    r = t.strip()
    if r:
        N = int(r)
        s += N 
    else:
        print(s)
        if s > s_max:
            s_max = s
        s = 0
print(s)

if s > s_max:
    s_max = s
print("****", s_max)

