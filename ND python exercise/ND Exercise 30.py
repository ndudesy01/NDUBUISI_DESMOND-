#30> Use input() to get a number and check if it's a 3-digit number.
num1=input("Enter a number")
if num1.isdigit() and len(num1.lstrip('-')) == 3:
    print("It is a 3-digit number.")
else:
    print("It is NOT a 3-digit number.")
