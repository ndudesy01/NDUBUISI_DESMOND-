#19. Write a program that uses both if-else and for loop to print whether numbers from 1 to 10
#are odd or even
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
