def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(name + ": " + str(score) + "\n")
    print(name + "'s score saved!")

def read_scores():
    with open("scores.txt", "r") as file:
        lines = file.readlines()
    
    print("")
    print("=== All Scores ===")
    for line in lines:
        print(line.strip())
    print("")

with open("scores.txt", "w") as file:
    file.write("")

save_score("Ethan", 95)
save_score("Jordan", 82)
save_score("Maya", 74)
save_score("Chris", 88)

read_scores()
