#7. Write a Python program to check if a character is a vowel or consonant.
char = input("Enter a single alphabet character: ")

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
