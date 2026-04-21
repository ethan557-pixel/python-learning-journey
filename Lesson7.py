person ={
    "name": "Ethan Harmon",
    "age": 32,
    "city": "Nashville"

}
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

person["email"] = "ethan.harmon@Belmoooont.edu"
person["age"] = 32
del person["city"]
print(person)

students = {
    "ethan": 95,
    "jordan": 82,
    "maya": 74,
    "chris": 88
}

for name, score in students.items():
    print(name + " scored: " + str(score))

print("")
print("Highest score: " + str(max(students.values())))
print("Lowest score: " + str(min(students.values())))
print("Class Average: " + str(sum(students.values()) / len(students)))




students = [
    {"name": "Ethan", "score": 95, "city": "Nashville"},
    {"name": "Jordan", "score": 82, "city": "Chattanooga"},
    {"name": "Maya", "score": 74, "city": "Knoxville"},
    {"name": "Chris", "score": 88, "city": "Memphis"}
]

for student in students:
    print(student["name"] + " from " + student["city"] + " scored: " + str(student["score"]))

print("")
print(" Total students: " + str(len(students)))