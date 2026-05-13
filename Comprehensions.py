# Basic list Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squared = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]

print("Squared:", squared)
print("Evens:", evens)
print("Doubled Evens:", doubled_evens)


# Dictionary Comprehension
names = ["Ethan", "Zuko", "Kya", "Mako"]
grades = [95, 88, 92, 78]


# Zip two lists into a dictionary

grade_book = { name: score for name, score in zip(names, grades) }
print("Grade Book:", grade_book)

# Only Passing Grades

passsing = { name: score for name, score in grade_book.items() if score >= 90 }
print("Passing Students:", passsing)

# Transform Values
letter_grades = { name: ("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F") for name, score in grade_book.items() }
print("Letter Grades:", letter_grades)

# Nested List Comprehension -multiplication table

table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for row in table:
    print(row)

    # Remove duplicates automatically
words = ["the", "cat", "sat", "on", "the", "mat", "and", "the", "cat"]

unique_words = {word for word in words}
print("Unique words:", unique_words)

word_lengths = {word: len(word) for word in unique_words}
print("Word lengths:", word_lengths)

long_words = {word for word in unique_words if len(word) > 2}
print("Long words:", long_words)