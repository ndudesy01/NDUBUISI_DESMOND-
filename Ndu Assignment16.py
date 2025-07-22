#16. Print all prime numbers between 1 and 50.
for num in range(2, 51):  # Start from 2, since 1 is not a prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check up to the square root of num
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(num)