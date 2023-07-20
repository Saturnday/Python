    #call a function hello
"""
name = input("what's your name? ")
hello() #trying to make a funciton hello - it'll give an error that there are no such funciton
print (name)

    #def to define a funnction
def hello(): 
    print("Hello")
name = input("What's your name? ")
hello()
print(name)
    #the : means that wait for indantation, that there will be some input to this funciton
    #the () means that there could be some arguments


def hello(to): #parameter called to
    print("Hello,", to)#all indented code should line up to make python understand that this is one function
name = input("What's your name? ")
hello(name)

# default value of the parameter = "World":
def hello(to="world"): #parameter called to
    print("Hello,", to)#all indented code should line up to make python understand that this is one function

hello()
name = input("What's your name? ")
hello(name)

#function has to be defined at the top:
def main():
    name = input("What's your name? ")
    hello(name)
def hello(to="world"): 
    print("Hello,", to)
main()
#scope - referes to veriable existing only in context in whicn we defind it
"""

#return square x
def main():
   x=int(input("waht is x? "))
   print("Square x =", square(x))
def square(n):
   return n*n # other variations: pow (n,2) / n**2
main()