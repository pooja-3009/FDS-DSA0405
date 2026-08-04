from collections import Counter
import string

file = open(r"C:\Users\pooja\OneDrive\Desktop\sample_text.txt", "r")

text = file.read().lower()
file.close()

text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()

frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)