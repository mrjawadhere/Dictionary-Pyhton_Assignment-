# 21.	Use a dictionary to count the occurrences of each word in the string "hello world hello python world".
# Get input from the user
text = input("Enter Any Sentence: ")

# Split the text into words
words = text.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    word = word.lower()  # Convert to lowercase for uniformity
    word_count[word] = word_count.get(word, 0) + 1

# Print the word counts
print("Word occurrences:")
for word, count in word_count.items():
    print(f"\t{word}:\t {count}")
