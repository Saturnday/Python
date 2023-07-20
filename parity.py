"""
x=int(input("What is x? "))
if x>=90:
    print("A")
elif x>=80:
    print("B")
else:
    print ("C or D")


def main():
    x=int(input("What is x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("odd")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False


main()

def main():
    x=int(input("What is x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("odd")
def is_even(n):
    return True if n%2==0 else False
main()
"""

def main():
    x=int(input("What is x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("odd")
def is_even(n):
    return n%2==0 #just return the quastion, due to the this operations is already true or false
main()