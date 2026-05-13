def shout(func):
    def wrapper():
        print("ABOUT TO RUN DIS FUNCTION BOIIIII")
        func()
        print("WE OUT HERE, FUNCTION DONE")
    return wrapper

@shout
def greet():
    print("Hello, Ethan!")

greet()


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to run.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done")

@timer
def fast_function():
    total = sum(range(1000000))
    print(f"Sum: {total}")

slow_function()
fast_function()


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} ")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def multiply(a, b):
    return a * b

add(5, 3)
multiply(10, 4)