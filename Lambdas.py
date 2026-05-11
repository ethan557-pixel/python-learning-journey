# Regular function

def double(x):
    return x * 2

# Same thing as a lambda
double_lambda = lambda x: x * 2

print(double(5))          
print(double_lambda(5))



students = [
    {"name": "Ethan", "grade": 95},
    {"name": "Zuko", "grade": 88},
    {"name": "Kya", "grade": 92},
    {"name": "Mako", "grade": 78}       

]


# Sort by grade using lambda
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
for s in sorted_students:
    print(f"{s['name']}: {s['grade']}")
print("")

# Map - apply a function to every item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)

#Filter - Keep only items that match
passing = list(filter(lambda x: x >= 90, [95,82,91,67,55,78]))
print("Passing scores:", passing)