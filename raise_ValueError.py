#create a class with an objects name and house that will be printed out in main function 

#how to initialize a class
class Student:
    def __init__(self, name, house): #patronus #pass parameters to this method init, first variable should be self(the container itself)
    #assign values to the variables from the class 
        if not name: #if name==""  
            raise ValueError("Missing name")#you can treat exception like funciton and pass arguments
        if house not in ["Gryffindor","Hufflepuff","Slytherin", "Ravenclaw"]:
            self.name = name
            self.house = house
            """self.patronus = patronus"""
    def __str__(self):
        return f"{self.name} is in {self.house}"
    """
    def charm(self): #funcion inside of the calss, in has to take at least on arguemnt by convintion it called self
        match self.patronus:
            case "Stag":
                return "🐴"
            case _:
                return"🪄"
    """
def main():
    student=get_student()
    #print(student)
    student.house= "Number four, Privet Drive" #change the atribute in the class Student
    print(student)
    """
    print("expecto patronum")
    print(student.charm())
    """


def get_student():
    name = input("What's the name?  ")
    house = input("What's the house?  ")
    """patronus = input("What's the patronus?  ")"""
    try:
        return Student(name, house) #,patronus)
    except Value:
        ...

if __name__ == "__main__":
    main()

#exceptions that we can craete to exit a program, and send info back that it is
