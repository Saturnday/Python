#way to sort by sentence:

students = []

with open("students.csv") as file:
    for line in file:
        Name, House = line.strip().split(',')
        students.append(f"{Name} is in{House}")
for student in sorted(students):
    print(student)
#another way of sorting by just the Name

