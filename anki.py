#some excersises to learn syntax
"""
import sys
def main():
    if len(sys.argv)<2:
        sys.exit("no arguments passed")
    
for arg in sys.argv[1:]
    print("Hello, ", arg)
main()

def main():
    try:
        x=int(input("x=?"))
        print("x=", x)
    except:
        print("the x is not int")
main()

def main():
    square(3)

def square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()
main()
assertx
__init__.py

def test_sayhello():
    assert the_fucntion(argument)=="output"

    for x in range(2):
        print("")
        print("x\n"*3, end="")

x=input("what's x? ")        
match x:
    case "1":
        print("")
    case _:
        print("all other ")

"""
"""

from calculator import square
def main():
    x=input(print("Name?"))    


def test_square():
    try:
        assert square(3)==9
    except:
        print("square of 3 is not 9")

if __name__ == "__main__":
    main()
import sys
sys.argv

name_of_dic={
    "key": "value",
}
print(name_of_dic['Key'])


name = input("what's your name?")
print(f"Hello, {name}")

"""

#create a file to soter the list in


name=input("what's your name?")
file = open("names.txt", "w")
file.write(name)
file.close()
