#the funcction open files comes with a special method readelines() - read of the lines in file
#docs.python.org/3/library/functions.html#sorted
"""
with open("names.txt", "r") as file: #actually don't need to specify "r"  - it is impicit deoult
    lines = file.readlines()
for line in lines:
    print("Hello, ", line.rstrip()) #rstrip - strip of the end of the line, technically it'll be more "clean" execution
"""
#create a list to store the data and sort in this list using append

list_names=[]
with open("names.txt") as file:
    for line in file:
        list_names.append(line.rstrip())

for name in sorted(list_names):
    print(f"Hello,  {name}")
#it is more common to use csv files inside the file we can seporate values with commas as like columns