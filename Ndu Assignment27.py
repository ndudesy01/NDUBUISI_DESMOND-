#27. Find the position (index) of a substring in a string
main_string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

index = main_string.find(substring)

if index != -1:
    print(f"Substring '{substring}' found at index {index}.")
else:
    print(f"Substring '{substring}' not found in the string.")