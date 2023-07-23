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

#a tighter version + use it as a funcion


def main():
    x=what_is_x(x)

    def what_is_x(x):
        while True:
            try:
                print(int(input(f"x={x}")))
            except ValueError: #Other syntax NameError
                print("x is not int")
            else:
                return x
main()

