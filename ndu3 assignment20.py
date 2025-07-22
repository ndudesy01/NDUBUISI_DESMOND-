#20. Write a function that accepts a name and a greeting message as keyword arguments and
#prints them.
def greet_user(name="Okoye", greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user(name="Desmond", greeting="Welcome")
greet_user(greeting="Hi", name="Ndubuisi")

greet_user()