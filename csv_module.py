import csv
students = []
with open("students_adress.csv") as file: #forgot to put the file in quotes"""
    #didn't use the module of the csv called "reader":
    reader = csv.reader(file)# first type funtion after the method, also this line will put all stuff in the file.csv to the "readfer" funtion
    #for row in reader: #it will itterate over whole file, and figure out where are commas how the file structured etc
        #students.append({"name" : row[0], "adress" : row[1]})#forgot to put brakets around the dictionary
#if there will be only two parameters another way to write it:
    for name, adress in reader: 
        students.append({"name":name, "adress":adress})

#use private funcion to print out result:
for student in students:
    sorted(students, key=lambda student: student["name"]) #didn't memorize the lambda syntax

#syntax for csv.DictReader will itterate over the file as dictionary
#the csv file should be updated with name of the coloumns
#new data added to the csv file won't affect the old code although the parameters of this csv file didn't used ig House:Slytherin
import csv
studnets = []
with open('students_adress.csv') as file:
    #first step should be reading the whole file
    reader=csv.DictReader(file) #forgot the name of the funtion DictReader, and pass to it the name of the file
    for row in reader: #than iterating within the file row by row
        students.append(student['name'], student['home']) #

