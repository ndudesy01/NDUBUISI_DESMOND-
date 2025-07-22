#5.Write a program to find the greatest among three numbers.

num1=int(input("please enter your first number"))
num2=int(input("please enter your second number"))
num3=int(input("please enter your third number"))
if num1>num2 and num1>num3:
    print(num1,"is greatest number")
if num2>num3 and num2>num1:
    print(num2,"is greatest number")
if num3>num2 and num3>num1:
    print(num3,"is greatest number")