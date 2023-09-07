#
#print is always giving a new line, and in the file the names are also wirttent on the new line

with open("names.txt", "r") as file:
    lines=file.readlines()
    for line in lines:
        #print (f"Hello, {line}", end="") #or a little better is strip off the line:
        print(f"Hello, {line.strip()}")

#another more ellegant way:

with open("names.txt", "r") as file:
    for line in file:
        print(f"Hello, {line.strip()}")


#how to sort names before printing it:

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())
for name in sorted(names):
    print(f"Hello,{name}")

#a lot more compact way:
        
with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.strip()}")


