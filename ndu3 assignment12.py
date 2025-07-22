#12. Write a function that accepts a list and returns the maximum element from the list.
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

my_list = [3, 7, 2, 9, 5]
max_value = find_max(my_list)
print("Maximum element:", max_value)
