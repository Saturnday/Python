
"""
what you can pass to the funciton - parameters
inputs are - arguments

print(*objects, sep=' ', end='\n', file=None, flush=False)

text "python" will enable enteractive mode to execute commands

"""
x = 1
y = 2
z = x + y
print(z)
# plus operator concatenates numbers, not strings


x=int(input("what is x?"))
y=int(input("what is y?"))
z=(x+y)
print (z)
"thismethod will not use z at all:"
print(x+y)

z=round(x+y)
#will be rounded up to neares integer

#positional parameters  - passing parameters to the print, meaning that which parameter goes firs, it'll be passed to print first

#named parameters (sep) - optional, can pass at the end of statement - can pass at the end of the statment
print("hello,",name, sep='???')  #this will print out:hello,???Mike -  

#backslash \ - represents an "escape character" ig:
print("hello, \"friend\"")


#{}
name=("Mike")
print (f"Hello, {name}")#put an f at the begining of the string

#buit into stirngs ability to change string:
name = name.strip() #remove whitespace from str
#if name is a string, we can call a function,

#name = input("what's your name", name = name.strip().title())

name = input("what's your name").strip().title()

#split user name into first and lust name
first, last = name.split(" ")

print(f"Hello, {first}") #notice that print is a function it doesn't need to have the = character to use it;
