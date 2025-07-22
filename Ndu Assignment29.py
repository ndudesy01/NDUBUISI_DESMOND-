#29. Remove all digits from a string.
word = input("Enter a string: ")

result = ""
for char in word:
    if not char.isdigit():
          result +=char

print("String after removing digits:", result)
