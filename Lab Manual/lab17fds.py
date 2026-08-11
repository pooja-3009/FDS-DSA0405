from collections import Counter
import matplotlib.pyplot as plt

# Input feedback
text = """
The product is good and the service is good.
The service is fast and the product is useful.
Good product with excellent service.
The product is useful and easy to use.
"""

# Convert to lowercase
text = text.lower()

# Remove punctuation
import string
text = text.translate(str.maketrans('', '', string.punctuation))

# Stop words
stop_words = {
    "the", "is", "and", "a", "an", "to", "of", "for",
    "with", "in", "on", "at", "this", "that", "it"
}

# Remove stop words
words = [word for word in text.split() if word not in stop_words]

# Frequency distribution
frequency = Counter(words)

# User input
N = int(input("Enter Top N words: "))

# Display Top N words
top_words = frequency.most_common(N)

print("\nTop", N, "Most Frequent Words\n")

for word, count in top_words:
    print(word, ":", count)

# Bar graph
words = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.bar(words, counts)
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()