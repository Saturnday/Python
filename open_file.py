#opent(names.txt) open returnes a "file handle"(дескриптор файла) special variable that allowes to access the data subsequently
#appending - добавление 
"""
name = input('What is the name')
file=open("names.txt", "w") # w - used for writing, it opens a filed an recrates it.
file.write(name)
file.close()

#this version will add the names one after another without spaces
name = input('What is the name? ')
file=open("names.txt", "a") # a - used to append to the file, to add to the bottom
file.write(name)
file.close()


#so here we have to add a new line to the file manually:

name = input('What is the name? ')
file=open("names.txt", "a") 
file.write(f"{name}\n") # each of the name will be on the own line
file.close() #we don't need to close file, coz wehn wirting code it is easy to forget to close file, because the file could be corrupted or summat

"""
#more pythonik way is to use "with":

name = input('What is the name? ')
with open("names.txt", "a") as file:
    file.write(f"{name}\n") # the file will be automaticly closed
