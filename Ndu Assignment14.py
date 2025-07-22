#14. Calculate the sum of all numbers from 1 to n.
n = int(input("Enter a positive number: "))

if n > 0:
    total = 0
    for i in range(1,n+1):
        total += i
    print(f"The sum of numbers from 1 to {n} is {total}.")
else:
    print("Please enter a number greater than 0.")
