file = open("directory.txt")
s = file.readlines()

directory_curr = ""
tree = {}

for commando in s:
    if commando.startswith("$"):
        commando = commando.split()
        if commando[1] == "cd":
            if commando[2] == "/":
                directory_curr = "/"
            elif commando[2] == "..":
                
