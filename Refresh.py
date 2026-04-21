print("Welcome to the temperature converter!")

celcius = int(input("Enter a temperature in celcius: "))
farhenheit = (celcius * 9/5) + 32
print(str(celcius) + " degrees celcius is equal to " + str(farhenheit) + " degrees farhenheit.")

print("part 2")


for i in range(1, 11):
   is_even = (i % 2 == 0)
   if is_even:
       print(str(i) + " is even.")
   else:
       print(str(i) + " is odd.")   


print("part 3")

while True:
    password = input("Enter Password:   ")
    if password == "supersecret":
        print("Access Granted!")
        break
    else:
        print("Access Denied! Try again.")
    