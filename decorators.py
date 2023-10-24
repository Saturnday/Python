class Studnent:
    def __init__(self, name, house):
        if not name:
            raise ValueError("No name")
        if house not in ["a", "b", "c"]:
            raise ValueError("House is not a,b,c")
        self.name = name # object self initialized in the class Student that contains variables name and house
        self.house = house
    def __str__(self): #anytime a function Student called with the print function this method will be called automatically
        return(f"{self.name} is in {self.house}")



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Studnent(name, house)

def main():
    student = get_student()
    print(student)

if __name__ == "__main__":
    main()
