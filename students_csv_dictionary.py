#-create a list to store values in it and make operations on them such as:
# -read the file every line of it and put it in to the list
# - use the 
#  -sorted()
#  -use list.append() to add to the list
#-create a dictionary where i cant store value and name of the pairs from the csv file
#-
"""
Students = []  # Create an empty list called 'Students' to store student data.

with open("students.csv") as file:  # Open the file named "students.csv" for reading.
    for line in file:  # Start iterating over each line in the file.

        # Split the current line into two parts at the comma (',') and remove any leading/trailing whitespace.
        Name, House = line.strip().split(",")

        # Create an empty dictionary called 'Student' to store the student's data.
        Student = {}

        # Assign the 'Name' and 'House' values to the 'Student' dictionary.
        Student['Name'] = Name
        Student['House'] = House

        # Append the 'Student' dictionary to the 'Students' list.
        Students.append(Student)

# Now that we've processed all lines in the file and populated the 'Students' list with dictionaries,
# we'll iterate over each dictionary in the 'Students' list and print out the student's name and house.
for Student in Students:
    print(f"{Student['Name']} is in {Student['House']}")
"""
#using lambda function (anonimus function)

Students = []  
with open("students.csv") as file:  
    for line in file:  
        Name, House = line.strip().split(",")
        Student = {"name" : Name, 'house' : House}
        Students.append(Student)

for Student in sorted(Students, key=lambda student: student['name']):
    print(f"{Student['name']} is in {Student['house']}")



