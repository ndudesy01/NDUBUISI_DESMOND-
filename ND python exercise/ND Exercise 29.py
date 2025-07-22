#29> Write a program that asks for username and password and validates them
correct_username = "ndubuisi"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
