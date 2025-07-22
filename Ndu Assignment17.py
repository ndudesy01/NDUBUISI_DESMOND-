#17. Reverse a number using a while loop (e.g., 123 → 321).
num = int(input("Enter an integer: "))
original_num = num

is_negative = num < 0
num = abs(num)

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
    print(num)
