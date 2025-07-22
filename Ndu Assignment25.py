#25. Check if a given word is a palindrome
word = input("Enter a word: ")

# Convert to lowercase to make the check case-insensitive
word_lower = word.lower()

if word_lower == word_lower[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")