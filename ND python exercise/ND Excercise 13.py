#13> Ask the user to enter a string and count how many times the letter a appears.

name=str(input("Enter a string"))

count_a = name.lower().count('a')

print(count_a)