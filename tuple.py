

#tuple - returning two values in one:
def main():
    name, house = get_name()
    print(f"The {name} is in the {house}")

def get_name():
    name = input("what's the name? ")
    house = input("what's the house? ")
    return name, house #tuple

if __name__== "__main__":
    main()

#index into the tuple:

def main():
    i = get_name()
    print(f"The {i[0]} is in the {i[1]}") #indexing here 

def get_name():
    name = input("what's the name? ")
    house = input("what's the house? ")
    return name, house

if __name__== "__main__":
    main()
#''tuple' object does not support item assignment
#to assign some values to the object create a list: return[name, house]; and then assign new values to it