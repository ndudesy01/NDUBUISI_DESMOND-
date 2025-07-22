#4. Take two numbers from user and print the greater one using if-else.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")