name = input("enter your name:  ")

print(name.upper())
print(name.lower())
print(name.title())
print(len(name))
print(name.replace("a", "e"))



sentence = input("enter a sentence:  ")

word_count = len(sentence.split())
clean = sentence.strip()
starts_with = sentence.startswith("I")

print("word count: " + str(word_count))
print("cleaned up: " + clean)

if starts_with:
    print("your sentence starts with 'I'")
else:
    print("your sentence does not start with 'I'")
if "python" in sentence.lower():
    print("your sentence mentions python!")




sentence = input("enter a sentence:  ")

words = sentence.split()
word_count = len(words)
char_count = len(sentence)
upper_count = sum(1 for c in sentence if c.isupper())

print("--- Sentence Analysis ---" )
print("Original:   " + sentence )
print("uppercase:  " + sentence.upper() )
print("lowercase:  " + sentence.lower() )
print("word count: " + str(word_count) )
print("characters: " + str(char_count) )
print("Capital letters: " + str(upper_count) )

if word_count > 10:
    print("Your sentence is quite long!")
elif word_count > 5:
    print("Your sentence is of medium length.")
else:
    print("Your sentence is short!")    