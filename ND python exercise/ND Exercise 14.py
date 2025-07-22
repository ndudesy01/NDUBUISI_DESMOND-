#14> Take a full name and print the first name and last name separately
full_name = input("Enter your full name: ")

name_parts = full_name.strip().split()

if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
else:
    print("Please enter both your first and last name.")

