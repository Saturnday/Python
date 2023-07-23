"""
    #first attemnt

    main():
    age=get_student_age()
    print_age(age)

def get_student_age():
    if True:
        try:
            return int(input("Whta's your age?"))
        except ValueError:
            print("Age is not int")
            
def print_age(age):
    while True:
        if 30>age>5:
            print("Age must be between 5 and 30")
        else:
            print(f"The student's age is {age}")
            break
main()
"""

main():
age=get_student_age()
print_age(age)

def get_student_age():
    while True:
        try:
            age = return int(input("Whta's your age?"))
            if age<5 or age>30:
                print("The age sould be between 5 and 30")
            else:
                return age
        except ValueError:
            print("Age is not int")
            
def print_age(age):
    print(f"sutdent's age is {age}")
main()
