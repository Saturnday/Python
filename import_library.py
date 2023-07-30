
some built-in libraries in the python

import random
coin = random.choice(["heads","tails"])
print(coin)

from random import choice
coin=choice(["heads","tails"])
print(coin)

print (random.randint(1,10))

cards=["jack","king","queen"]
random.shuffle(cards)#shuffles the list was given itself
for card in cards:
    print(card)
import sys
try:
    print("Hello, my name is", sys.argv[1])
#sys.argv is a list, the square bracket notation used to at the vairous elements insied of the list
#Terminal: python import_library.py Mike
#sys.argv[1] - stores the name, but in sys.argv[0] - is the name of the programm(name of the file that is executed)
#and error indexerror - try to acces of an element that is doesn't exist
except IndexError:
    print("too few arguments")
if len(sys.argv)<2:
    print("too few args")
elif len(sys.argv)>2:
    print("to many args")
else:
    print("Hello, ", sys.argv[1])

#the way to exit if we don't pass any parameters to avoid error message:
import sys
if len(sys.argv)<2:
    sys.exit("too few args")
elif len(sys.argv)>2:
    sys.exit("to many args")
print("Hello, ", sys.argv[1])

#sys.exit used ot exit the programm

#using a for loop to eterate over a list, arg is a variable created on fly

import sys
if len(sys.argv)<2:
    sys.exit("too few args")
for arg in sys.argv:
    print("Hello, ", arg)
#take a slice of a list - take a subset of it
#to take a slice: 
    #sys.argv[1:] - this will take a slice from 1, start at element 1, and go do the end, the second number is not nescessary
import sys
if len(sys.argv)<2:
    sys.exit("too few args")
for arg in sys.argv[1:]:#sliced
    print("Hello, ", arg)