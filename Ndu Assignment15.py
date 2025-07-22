#15. Write a program to count digits in an integer using a while loop
num = int(input("Enter an integer: "))
original_num = num
num = abs(num)
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1
print(f"The number of digits in {original_num} is {count}.")
