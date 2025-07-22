#28> Ask user to input two strings and compare if they are equal (case-insensitive).
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1.lower() == string2.lower():
    print("The strings are equal (case-insensitive).")
else:
    print("The strings are not equal.")
