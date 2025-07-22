#22> Ask the user to enter marks and print the grade using if:
#90: A, >75: B, >50: C, else Fail
mark=int(input("Enter your mark"))
if mark>=90:
    print("Your grade is A")
elif mark>=75:
    print("Your grade is B")
elif mark>=50:
    print("Your grade is C")
else:
    print("Fail")