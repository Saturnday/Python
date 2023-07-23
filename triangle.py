"""
the code that didn't work first attemnt:
def main():
    triangle(5)

def triangle(side):
    for k in range(side):
        for i in range(side):
            j = int((len(range(side))))
            print("#"*j,end="")
            i=i-1
        print()
main()
"""
#why is it prints from 1 to 3 but not to 4? - the first number in range is 0
#issue fixed with passing the the side parameters 
def main():
   # triangle(5)
    revtriangle(5)
"""
def triangle(side):
    for i in range(1,side+1):
        print("#"*(i-1))
"""
def revtriangle(side):
    for i in range(1,side-1):
        print("#"*i)
        
            

main()

