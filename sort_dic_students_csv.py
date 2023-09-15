students = []
with open("students.csv") as file:
    for line in file:
        Name, House = line.strip().split(",")
        student = {"Name":Name, "House":House} # i wrote students instead of student: at this line i has to create a dictionary variable and right away assignt to it key - value pair, where "Name" key will be assigned the value of Name variable that i read in the line aobve
        students.append(student) #here is after reading lines in students.csv im adding the every student dictionary to the students list
#add another named parameter"key":

# - def a function that will return the student's name
def get_key(student): #i forgot to write the name of dictionary
    return student['Name']

for student in sorted(students, key=get_key):
    print(f"{student['Name']} is in {student['House']}")

# -than iterate with sorted funciton and pass to it key that is the name of prev funciton