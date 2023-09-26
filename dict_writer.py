import csv
name = input("what's the name? ")
home = input("what's the home? ")
with open('dict_writer.csv' , 'a') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})