#2. Write a program to check whether a number is positive, negative or zero.
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is Positive.")
elif num < 0:
    print(f"{num} is Negative.")
else:
    print("The number is Zero.")