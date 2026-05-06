def count_down(number):
    for i in range(number, 0, -1):
        print(i)
    print("Blast off!")
count_down(10)


def profile (name, age, city):
    profile = {
        "name": name,
        "age": age,
        "city": city
    }
    codename = input(" Enter Codename: ")

    if codename == "Jefe":
        print("Welcome back, Jefe!")
        for key, value in profile.items():
            print(key + ": " + str(value))
    else:
        print("Access denied. GO AWAY!")
profile("Ethan", 30, "Nashville")

def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

save_note("Today i learned about dictionaries")
save_note(" functions are reusable blocks of code")
save_note(" Jefe is the best codename ever")