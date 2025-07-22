#9. Input username and password; validate if they match the stored ones.

username = "ndubuisi"
password = "1234567"
inputed_username = input("Enter username: ")
inputed_password = input("Enter password: ")

if inputed_username == username and inputed_password == password:
    print("Login successful.")
else:
    print("Invalid username or password.")