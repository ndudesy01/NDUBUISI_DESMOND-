#6. Create a program that takes a sentence and prints the number of vowels in it.
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print("number of vowels:", vowel_count)