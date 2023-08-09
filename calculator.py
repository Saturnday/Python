#
def main():
    x=int(input("enter a number: "))
    print("the square is: ",square(x))

def square(n):
    return n*n

if __name__ == "__main__":#this allows safe import the funciton into another file
    main()