def analyze_text(text):
   return {
      "word_count": len(text.split()),
      "char_count": len(text),
      "uppercase": text.upper(),
      "is_question": text.strip().endswith("?")
    }

result = analyze_text("Hello, how are you?")
for key, value in result.items():
   print(key+": " + str(value))

def filter_scores(scores, passing):
    return [score for score in scores if score >= passing]

scores = [45, 82, 91, 67, 55, 78, 95, 33, 88]
passing = filter_scores(scores, 70)
print(passing)






def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        word = word.strip(".,!?:;")
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

sentence = input("Enter a sentence: ")
frequencies = word_frequency(sentence)
for word, freq in frequencies.items():
    print(f"{word}: {freq}")