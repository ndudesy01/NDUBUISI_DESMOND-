#1. Write a Python program to take a number from user and print whether it is even or odd.
num1=int(input("please enter your number"))
if num1 % 2 == 0:
    print(f"{num1} is Even.")
else:
    print(f"{num1} is Odd.")