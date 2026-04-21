def greet(name):
    print(f"Hello, {name}! Welcome to python coding!")
greet("Ethan")
greet("claude ")
greet("world")

def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print("5 + 3 = " + str(answer))
print("10 + 20 = " + str(add(10, 20)))
print("100 + 200 = " + str(add(100, 200)))


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def analyze_scores(name):
    total = 0
    high_score = 0

    for round in range(1, 4):
        score = int(input("enter score for round " + str(round) + ": "))
        total = total + score
        if score > high_score:
            high_score = score
        
    average = total / 3
    grade = get_grade(average)

    print("--- Score Analysis for " + name + " ---")
    print("average score: " + str(average))
    print("highest score: " + str(high_score))
    print("final grade: " + grade)
    return grade

name = input("What's your name?")
grade = analyze_scores(name)
if grade == "A":
    print("Amazing job, " + name + "!")
elif grade == "B":
    print("Good job, " + name + "!")
elif grade == "C":
    print("Do better, " + name + "!")
else:
    print("Keep trying, " + name + "!")