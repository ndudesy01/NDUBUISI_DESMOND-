#23. Count the number of vowels in a given string.
word = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print(f"Number of vowels in the string: {count}")