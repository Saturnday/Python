# the csv file is a format practice
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]}is in{row[1]}")
#other way to do it assigning tow variables at the same time:
with open("students.csv") as file:
    for line in file:
        Name, House = line.rstrip().split(',')
        print(f"{Name} is in {House}")