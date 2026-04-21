for i in range(5):
    print(i)
for i in range(5, 6):
    print(i)
for i in range(1, 11):
    print(str(i) +"x5 = " + str(i*5))
count = 1
while count <= 5:
    print("count is: " + str(count))
    count = count + 1

print("done!")

name = input("What's your name?")
high_score = 0

for round in range(1, 4):
    print("--- Round " + str(round) + " ---")
    score = int(input("What is your score?"))

    if score > high_score:
        high_score = score
        print( "New HIGH SCORE!!")
    else:
        print(" do better next time!") 

print ("Game Over, " + name + " !")
print("Your high score was: " + str(high_score))   
if high_score >= 90:
    print("Amazing game, " + name + "!")
elif high_score >= 80:
    print("Good game, " + name + "!")
else:
    print("do better next time, " + name + "!")