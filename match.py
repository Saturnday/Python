"""
x=input("What is your name?")
match x:
    case "Mike":
        print("Shmike")
    case "Alex":
        print("Shmalex")
    case _:
        print("alright")
"""
x=input("What is your name?")
match x:
    case "Mike"|"Alex":
        print("Shmalex")
    case _:
        print("alright")