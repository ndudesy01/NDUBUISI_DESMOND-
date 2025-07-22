#20. Use a loop to print only vowels in a given string.
word = input("Enter a string: ")

vowels = "aeiouAEIOU"

print("Vowels in the string:")
for char in word:
    if char in vowels:
        print(char)
