"""
#@property of funtion and decorators to decorate functions - these are funcitons that modify behabior of another funcitons
class Student:
    def __init__(self, name, house): 
        if not name: 
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        
        if house not in ["Gryffindor","Hufflepuff","Slytherin", "Ravenclaw"]:
            self.name = name
            self.house = house
           
    def __str__(self):
        return f"{self.name} is in {self.house}"
    
    @property
    # Getter
    def house(self):
        return self.house
    
    @house.setter #we can ceep all error chekcing in the setter, every time we access.house the setter method will be called 
    # Setter #the setter also protects data from changing it later in the code, 
    #if ill try to assign some other value to the variable house it will rise the Value Error from the setter ig line 31
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid house")
    
        self.house = house
 
def main():
    student=get_student()
    #print(student)
    #ig ill set here new vaule line below: 
    #student.house= "Number four, Privet Drive"  - this won't work cos data protected by the setter
    print(student)



def get_student():
    name = input("What's the name?  ")
    house = input("What's the house?  ")

    try:
        return Student(name, house) #,patronus)
    except Value:
        ...

if __name__ == "__main__":
    main()

"""
class Student:
    def __init__(self, name, house): 
        if not name: 
            raise ValueError("Missing name")
        self.name = name
        self.house = house
       
           
    def __str__(self):
        return f"{self.name} is in {self._house}" #now instance variable called _house, but property caled house, to avoid coliding
    
    @property
    def house(self):
        return self._house
    
    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house
 
def main():
    student = get_student()
    print(student)



def get_student():
    name = input("What's the name?  ")
    house = input("What's the house?  ")

    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()
