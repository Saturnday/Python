"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
main()


students = ["Hermione","Harry","Ron"]
for student in students:
    print (len(students), student)

x=input("what's x?")
try:
    x= int(x)
except ValueError:
    print("x is not an int ")
print(x)


i = input("?")
for x in range(i):
    print("hi")
    
j = int(input("?"))
for i in range(j):
    print("hi")


a = input("?")
match a:
    case "1"|"3"|"5":
        print("odd")
    case "2"|"4":
        print("not odd")

def main():
    square(3)

def square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
main()

def main():
    get_int()
    print_int()

def get_int():
    while True:
        try:
            return int(input("x=?"))
        except ValueError:
            print("x is not int")
def print_int():
    print(f"x = {get_int()}")
main()

somedict = {"key":"value",
         "key2":"value2"
         }
otherdict = [
    {"key1":"value1"},
    {"key2":"value2"}
]

try:
    x=int(input("what's x?"))
except ValueError:
    print("nope")

def main():
    print("x is", get_int())
def get_int():
    while True:
        try:
            return int(input("x=? "))
        except ValueError:
            print("x is not int")
        

main()

x = input("??")

match x:
    case "1":
        print('x=1')
    case _:
        print("blabla")

def main():
    square(3)

def square(size):
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
main()


x=input("what is x")
match x:
    case "2":
        print("x=2")
    case _:
        print

"""
x=list(range(1,6))
print(x[1:-1])
