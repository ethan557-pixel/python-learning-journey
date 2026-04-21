def get_student_name():
    name = input("enter your name?")
    return name.strip().title()

def show_welcome(name):
    print("")
    print("="*30)
    print(" Welcome, " + name + "!")
    print(". Your personal score tracker")
    print("="*30)
    print("")

name = get_student_name()
show_welcome(name)

def get_score():
    subjects =[]
    scores = []

    print ("Enter you subjects and scores.")
    print("Type 'done' when finished.")
    print("")

    while True:
        subject = input("Subject name ( or 'done'): ").strip().title()

        if subject.lower() == "done":
            break
        score = int(input("Score for " + subject + ": "))

        subjects.append(subject)
        scores.append(score)
        print("Added!")
        print("")
    return subjects, scores

name = get_student_name()
show_welcome(name)
subjects, scores = get_score()
print(subjects)
print(scores)

def analyze_scores(subjects, scores):
    total = 0
    high_score = 0
    low_score = 100
    best_subject = ""
    worst_subject = ""

    for i in range(len(scores)):
        total = total + scores[i]

        if scores[i] > high_score:
            high_score = scores[i]
            best_subject = subjects[i]

        if scores[i] < low_score:
            low_score = scores[i]
            worst_subject = subjects[i]

    average = total / len(scores)
    grade = get_grade(average)

    return average, high_score, low_score, best_subject, worst_subject, grade
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
    
name = get_student_name()
show_welcome(name)
subjects, scores = get_score()
average, high_score, low_score, best_subject, worst_subject, grade = analyze_scores(subjects, scores)
print("Average: " + str(average)) 
print("Grade: " + grade)


def show_report(name, subjects, scores, average, high_score,low_score, best_subject, worst_subject, grade):
    print("")
    print("==="*10)
    print("Report Card for " + name.upper())
    print("==="*10)
    print("")

    for i in range(len(subjects)):
        subject = subjects[i]
        score = scores[i]

        if score >= 90:
            tag = "Excellent"
        elif score >= 80:
            tag = "Good"
        elif score >= 70:   
            tag = "Average"
        elif score >= 60:
            tag = "Needs Improvement"
        else:
            tag = "Failing" 
        print(subject + ": " + str(score) + " - " + tag)

    print("")
    print("-"*30)
    print("Average Score: " + str(round(average, 1)))
    print("final grade: " + grade )
    print("Best Subject: " + best_subject + " (" + str(high_score) + ")")
    print("Worst Subject: " + worst_subject + " (" + str(low_score) + ")")
    print("==="*10) 
    print("")

    if grade == "A":
        print("Amazing job, " + name + "!")
    elif grade == "B":
        print("Good job, " + name + "!")
    elif grade == "C":
        print("Do better, " + name + "!")
    else:
        print("Keep trying, " + name + "!") 
    
def get_student_name():
    name = input("Enter your name: ")
    return name.strip().title()

def show_welcome(name):
    print("")
    print("=" * 30)
    print("  Welcome, " + name + "!")
    print("  Your Personal Score Tracker")
    print("=" * 30)
    print("")

def get_score():
    subjects = []
    scores = []

    print("Enter your subjects and scores.")
    print("Type 'done' when finished.")
    print("")

    while True:
        subject = input("Subject name (or 'done'): ").strip().title()

        if subject.lower() == "done":
            break

        while True:
            score_input = input("Score for " + subject + ": ")
            if score_input.isdigit():
                score = int(score_input)
                break
            else:
                print("Please enter a number!")

        subjects.append(subject)
        scores.append(score)
        print("Added!")
        print("")

    return subjects, scores

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

def analyze_scores(subjects, scores):
    if len(scores) == 0:
        print("No scores entered!")
        return None, None, None, None, None, None

    total = 0
    high_score = 0
    low_score = 100
    best_subject = ""
    worst_subject = ""

    for i in range(len(scores)):
        total = total + scores[i]

        if scores[i] > high_score:
            high_score = scores[i]
            best_subject = subjects[i]

        if scores[i] < low_score:
            low_score = scores[i]
            worst_subject = subjects[i]

    average = total / len(scores)
    grade = get_grade(average)

    return average, high_score, low_score, best_subject, worst_subject, grade

def show_report(name, subjects, scores, average, high_score, low_score, best_subject, worst_subject, grade):
    print("")
    print("=" * 30)
    print("  REPORT CARD FOR " + name.upper())
    print("=" * 30)
    print("")

    for i in range(len(subjects)):
        subject = subjects[i]
        score = scores[i]

        if score >= 90:
            tag = "Excellent"
        elif score >= 80:
            tag = "Good"
        elif score >= 70:
            tag = "Average"
        elif score >= 60:
            tag = "Needs Improvement"
        else:
            tag = "Failing"

        print(subject + ": " + str(score) + " - " + tag)

    print("")
    print("-" * 30)
    print("Average Score:   " + str(round(average, 1)))
    print("Final Grade:     " + grade)
    print("Best Subject:    " + best_subject + " (" + str(high_score) + ")")
    print("Worst Subject:   " + worst_subject + " (" + str(low_score) + ")")
    print("-" * 30)
    print("")

    if grade == "A":
        print("Amazing job, " + name + "!")
    elif grade == "B":
        print("Good job, " + name + "!")
    elif grade == "C":
        print("Do better, " + name + "!")
    else:
        print("Keep trying, " + name + "!")
    print("")

name = get_student_name()
show_welcome(name)
subjects, scores = get_score()
average, high_score, low_score, best_subject, worst_subject, grade = analyze_scores(subjects, scores)

if average is not None:
    show_report(name, subjects, scores, average, high_score, low_score, best_subject, worst_subject, grade)