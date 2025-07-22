#11. Create a function that takes a string and returns the reverse of that string.
def reverse_string(s):
    return s[::-1]
name = "desmond"
reversed_name = reverse_string(name)
print("Reversed string:", reversed_name)