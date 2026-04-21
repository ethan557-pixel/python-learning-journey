questions = [
    {"question": "what is the capital of tennesee?", "answer": "Nashville"},
    {"question": "what language are we learning?", "answer": "Python"},
    {"question": " what do you use to store key-value pairs?", "answer": "Dictionary"},
    {"question": "what is the keyword to define a function?", "answer": "def"},
    {"question": "what keyword exits a loop early?", "answer": "break"}
]

def run_quiz(questions):
    score = 0
    results = []

    print("")
    print("=" * 30)
    print("Welcome to the quiz!")
    print("=" * 30)
    print("")

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == q['answer'].lower():
            print("Correct!")
            score += 1
            results.append((q['question'], user_answer, True))
        else:
            print(f"Wrong! The correct answer is: {q['answer']}")
            results.append((q['question'], user_answer, False))

        print("")
    return score, results

def show_results(name, score, total, results):
    print("=" * 30)
    print("Results for " + name + "!")
    print("=" * 30)
    print("")

    for r in results:
        status = "Correct" if r[2] else "Wrong"
        print(status + ": " + r[0])

    print("")
    print("Final Score: " + str(score) + "/" + str(total))
    print("Percentage: " + str((score / total) * 100) + "%")

    if score == total:
        print("Excellent work! You got a perfect score!")
    elif score >= total * 0.8:
        print("Great job! You scored above 80%!")
    elif score >= total * 0.5:
        print("Not bad! You scored above 50%!")
    else:
        print("Better luck next time! Keep practicing!")

def save_results(name, score, total):
    try:
        with open("quiz_results.txt", "a") as file:
            file.write(f"Name: {name}, Score: {score}/{total}, Percentage: {(score / total) * 100}%\n")
        print("Results saved to quiz_results.txt")
    except Exception as e:
        print("An error occurred while saving results: " + str(e))

name = input("Enter your name: ").strip().title()
score, results = run_quiz(questions)
show_results(name, score, len(questions), results)
save_results(name, score, len(questions))