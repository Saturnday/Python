#create a function that'll print # 3 times in a row:

"""
def main():
    print_coloumn(3)

def print_coloumn(hight):
    for _ in range(hight):
        print("#")
        
main()
"""

def main():
    print_coloumn(3)

def print_coloumn(hight):
    for _ in range(hight):
        print("#\n"*3, end="")
        
main()
