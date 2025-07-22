#16> Write a program that checks whether a given word is a palindrome

word=str(input("Enter a word"))
normalized_word = word.lower()
if normalized_word == normalized_word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

