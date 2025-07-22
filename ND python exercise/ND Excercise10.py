#Ask the user for two numbers and a choice (add, subtract, multiply, divide), then perform the chosen operation.
num1=(input("Enter the first number:"))
num2=(input("Enter the second number:"))
operation = input("choose an operation(+,-,*,/ ")
if operation =="+":
   result = num1+num2
   print(f"The result of adding {num1} and {num2} is result")
elif operation == "-":
   result = num1-num2
   print(f"The result of - {num1} from {num2} is {result}")
elif operation == "*":
   result = num1*num2
   print(f"The result of * {num1} and {num2} is {result}")
elif operation == "/":
   result = num1/num2
   print(f"The result of / {num1} by {num2} is {result}")
   if num2==0:
   else:
 print("Error: / by zero is not allowed.")
else:
print("invalid operation. please choose from '+', '-', '*', '/'. ")
