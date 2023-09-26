#how to keep adding to the file:
"""
1) need to import all modules 
2) prompt user with input of name and home
3) open the file for writing in append mode to keep adding in variable 
4) assign to new variable return of the csv writer function that will take as the argument 'file' variabbel | WIRTE  TO THE FILE
5) use function to write a row into the 

writer = csv.writer(file): This line creates a writer object (writer) from the csv module, associated with the file object file. 
The csv.writer function initializes a CSV writer that will write data into the specified file. 
This step is necessary to set up the writer for the subsequent writing operation.
Pass there a list with name and home that i prompted to user
"""

import csv

name = input("What's the name?")
home = input("What's the home?")

with open("write_to.csv", "a") as file: #forgot to quote append
    writer = csv.writer(file) #first wirte function than the method!
    writer.writerow([name, home])
