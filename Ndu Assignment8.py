#8. Input a character and check if it’s a vowel or consonant.
character=str(input("please enter your character"))
vowels='a','e','i','o','u'
if   character in vowels:
     print(f"{character} is a vowel")
else :
    print(f"{character} is a consonant")
