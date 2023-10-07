#print out studnet's name and house using classes and objects

class Student:
    ...
def main():
    student = get_name()
    print(f"{student.name}, {student.house}")

def get_name():
    student=Student() #put the studnet object into the Studnet()calss
    student.name = input("What's the name? ")
    student.house = input("What is the house? ")
    return student

if __name__ == "__main__":
    main()
