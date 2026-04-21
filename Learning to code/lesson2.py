name = input("What's your name?")
age = input("How old are you?")
age = int(age)

print("Hey" + name + "!")
print("you are " + str(age) + " years old!")
print("next year you will be " + str(age + 1) + " years old! "  )

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")

if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager!")
else:
    print("You're a child!")

name = input("What's your name?")
Score = input("what did you get on the test?")
Score = int(Score)

if Score >= 90:
    print("Great job " + name + "! You got an A!")
elif Score >= 80:
    print("Good job " + name + "! You got a B!")
elif Score >= 70:
    print("Not bad " + name + "! You got a C!")
elif Score >= 60:
    print("You passed " + name + "! You need to do more studyin'!")
