file = open("score.txt", "w")
file.write("Ethan: 95\n")
file.write("Jordan: 82\n")
file.write("Maya: 74\n")
file.close()

print(" FILE SAAAAVED!")

file = open("score.txt", "r")
content = file.read()
file.close()

print("here is what's in the file: ")
print(content)

file = open("score.txt", "a")
file.write("Chris: 88\n")
file.close()

file = open("score.txt", "r")
lines = file.readlines()
file.close()

print(" All Scores: ")
for line in lines:
    print(line.strip())



def save_score(name, score):
    with open("score.txt", "a") as file:
        file.write(f"{name}: {score}\n")
    print( name + "Score saved!")

def read_scores():
    with open("score.txt", "r") as file:
        lines = file.readlines()
        print("")
        print("=== All Scores ===")
        for line in lines:
            print(line.strip())
        print("")

with open("score.txt", "r") as file:
    file.write("")

save_score("Ethan", 95)
save_score("Jordan", 82)
save_score("Maya", 74)
save_score("Chris", 88)

read_scores()
