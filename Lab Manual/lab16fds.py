from collections import Counter

# Sample customer reviews
reviews = [
    "This product is excellent and easy to use",
    "Excellent quality and good performance",
    "Good product with excellent features",
    "Easy to use and good value for money"
]

# Convert all reviews into one string
text = " ".join(reviews).lower()

# Remove punctuation
for ch in ".,!?;:'\"()":
    text = text.replace(ch, "")

# Split into words
words = text.split()

# Calculate frequency
frequency = Counter(words)

# Display frequency distribution
print("Frequency Distribution of Words:\n")
for word, count in frequency.items():
    print(word, ":", count)