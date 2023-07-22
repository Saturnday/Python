#create a function that'll print # 3 times in a row:

"""
def main():
    print_coloumn(3)

def print_coloumn(hight):
    for _ in range(hight):
        print("#")
        
main()


def main():
    print_coloumn(3)

def print_coloumn(hight):
    for _ in range(hight):
        print("#\n"*3, end="")
        
main()
"""

#print square with hashes 3x3:

# commence or sudo code 

def main():
    square(3)

def square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()#every time the line finished will be a backslash line ending 
main()