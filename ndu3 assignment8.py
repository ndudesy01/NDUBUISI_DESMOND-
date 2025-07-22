#8. Take a list of numbers and print only the even numbers using a for loop.
num1 = [10, 21, 32, 43, 54, 65, 76, 87, 98]
print("Even numbers in the list:")
for num in num1:
    if num % 2 == 0:
        print(num)
