try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("100 divided by " + str(number) + " is " + str(result))
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")





try:
    with open("nonexistentfile.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("The file you are trying to read does not exist!")

try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("That index is out of range!")

try:
    result = int("hello") + 5
except ValueError as e:
    print("Something went wrong: " + str(e))


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None
    finally:
        print(" division attempted. ")

print(safe_divide(10, 2))
print(safe_divide(10, 0))