"""
how to handle runtime errors
https://youtu.be/nLRL_NcnK-4


#example: input the value and if it is a string handle it

#syntax for error handling:
try:
    x=int(input("what's x?"))
except ValueError: #Other syntax NameError
    print("x is not int")
else:
    print(f"x={x}")


#Using loop to constantly prompt user with the input quastion

while True:
    try:
        x=int(input("what's x?"))
    except ValueError: #Other syntax NameError
        print("x is not int")
    else:
        print(f"x={x}")
        break
"""

#Pack it in to a function


def main():
    x=what_is_x()
    print(f"x={x}")

def what_is_x():
    while True:
        try:
            return int(input("what is x?"))
        except ValueError: 
            print("x is not int")
main()

