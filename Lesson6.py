scores = [95, 82, 74, 61, 88]
print(scores)
print(scores[0])
print(scores[1])
print(scores[-1])
print(len(scores))

scores.append(99)
print(scores)

scores.remove(61)
print(scores)
scores.sort()
print(scores)

scores.reverse()
print(scores)

print(max(scores))
print(min(scores))

names= ["Ethan", "Jordan", "Maya", "Chris"]

for name in names:
    print("Hello, " + name + "!")

grades = []

for i in range(1, 6):
    score =int(input("Entter score " + str(i) + ": "))
    grades.append(score)
print("")
print("Your Scores: " + str(grades))
print("highest score: " + str(max(grades)))
print("lowest score: " + str(min(grades)))
print("average score: " + str(sum(grades) / len(grades)))

grades.sort()
print("sorted scores: " + str(grades))