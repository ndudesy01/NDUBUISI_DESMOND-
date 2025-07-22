#16. Write a function that takes a string and returns True if it is a palindrome, else False.
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word = "information"
result = is_palindrome(word)
print(f"Is '{word}' a palindrome? {result}")
