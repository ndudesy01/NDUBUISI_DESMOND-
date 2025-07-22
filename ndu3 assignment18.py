#18. Take a sentence input and count how many times a word appears using count() function.

sentence = input("Enter a sentence: ")

word = input("Enter the word to count: ")

count = sentence.count(word)

print(f"The word '{word}' appears {count} times in the sentence.")
