"""
name = input("what's your name?")
print (f"Hello, {name}")


#add support for multiple names:
names = []
for _ in range(3):
    name = input("What's your name")
    names.append(name)
"""
#first method more direct
"""
name=input("what's your name?")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close() #don't realy need to call close on the file, but:

"""
#we can use WITH:


name=input("what's your name?")
with open("names.txt", "a") as file: #file here is still a varriable that is assigned
    file.write(f"{name}\n")