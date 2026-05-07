class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"{self.name} is a {self.breed} and is {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old!!")
    def describe(self):
        return (f"{self.name} ({self.breed}) ({self.age} years old)")

dog1 = Dog("Zuko", "Husky", 5)
dog2 = Dog("Kya", "Husky", 2)
dog3 = Dog("Mako", "PitBull", 1)

dogs = [dog1, dog2, dog3]
for dog in dogs:
    dog.info()
    dog.bark()

print(dog1.describe())
dog1.birthday()
print(dog1.describe())




class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)
        print(f"Score {score} added for {self.name}.")

    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)
    def report(self):
        avg = self.average()
        if avg >= 90:
            letter_grade = "A"
        elif avg >= 80:
            letter_grade = "B"
        elif avg >= 70:
            letter_grade = "C"
        elif avg >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
        print(f"\n{self.name} - Grade {self.grade}")
        print(f"Scores: {self.scores}")
        print(f"Average: {avg: .1f}")
        print(f"Grade: {letter_grade}")

student1 = Student("Ethan", 12)
student1.add_score(95)
student1.add_score(88)
student1.add_score(92)
student1.report()