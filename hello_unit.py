def main():
    name = input("what's your name?")
    print(say_hello(name))
#the world is a defout value, if there are no parameters passed to the function
def say_hello(to="world"): 
    return f"Hello, {to}"

if __name__ == "__main__":
    main()