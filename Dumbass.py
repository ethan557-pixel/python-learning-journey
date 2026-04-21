print("Hello, World!" )
name = input("What's your name? ")

def greet(name):
    print(f"Hello, {name}! Welcome to python coding!")  

    if name == "Ethan":
        print("You are the best, " + name + "!")
    elif name == "Claude":
        print("You are the best, " + name + "!")
    else:
        print("Nice to meet you, " + name + "!")


def get_age():
    age = input("How old are you? ")
    return int(age)