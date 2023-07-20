def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("what is n? "))
        if n>0:
            return n 

def meow(x):
    for _ in range(x):
        print("meow")
main()

"""
i=0
while i<3:
    print("meow")
    i+=1

while True:
    n=int(input("what's n?"))
    if n>0:
        break
for _ in range(n):
    print("meow")

#print mew n times, where n is an input of a function, and mew is a function that returns n

#two functions
    #1)definding a number
        #argument n that will be passed to range
    #2)printing the word meow this number of times
        #using range()
"""