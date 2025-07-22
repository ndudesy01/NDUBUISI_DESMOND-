
#1Write a program which tell number of vowels in each


# a_list = ["chinaza","vivian","goodness","osinafa","ofoma"]
# vowels=("a","e","i","o","u")
# for names in a_list:
#     count=0
#     for i in names:
#         if i in vowels:
#            count+= 1
#     print(f"{names}={count}vowels")

#2.Take 5 names from the user create a list
# step 1, count the number of vowels in each of the names and print the output

a_list=[]
# for i in range(5):
#  name=(input("Please enter your name"))
#  a_list.append(name)
#  vowels=["a","e","i","o","u"]
# for name in a_list:
#     count=0
#     for i in name:
#         if i in vowels:
#             count+=1
#     print(f"{name}={count}vowels")


#27/05/25
#write a function which will tst if a number is even or not
# def evenodd():
#     num=int(input("please enter number"))
#     if num%2==0:
#         print(num,"ia an even number")
#     else:
#         print(num,"is an odd number")
# evenodd()


# def even(num):
#     if num%2==0:
#         print(num,"ia an even number")
#     else:
#         print(num,"is an odd number")
# even(10)
#
#
# def sumnumber(num1,num2):
#     sum=num1+num2
#     print(sum)
# sumnuber(num1:10,num2:20)
#

#write a function which will tell if a person
# is eligible to vote in Nigeria
#function is going to accept the age.

# def check_vote():
#     if num>=18:
#         print("you are eligible to vote")
#     else:
#         print("you are not eligible to vote")

#write a function which will accept two numbers
# and tell which is greater.

# defgreater(num1,num2):
#     if num1>num2:
#         print(num1,"is greater than",num2)
#     elif:
#         print(num2,"is a greater than",num1)
#     else
#        print(num_greater)
#  num_greater(num1,num2):
#     if num1>num2:
#         print(num1,"is greater than",num2)
#     elif:
#         print(num2,"is a greater than",num1)
#     else
#        print(num_greater)
#

#write a program to create a functionality
# which will accept aname and return Hello name.

# def hello(name):
#     x="hello"+
#     print(x)
#     y=hello("vivian")
#     print(y)



#accept two numbers from a user and
# find the product of there sum and difference.


#write a program to create a function which accepts
# a string from the user
#and return the capital form of it.

# df x(word):
#     x=word.upper()
#   print(word)
#   name=estr(input("please enter name"))


# write a progarm which accept birth from user
# # and returns the age.
# def  age(year):
#      x=2025
#      age=x-year
#      return age
#     year=(input("please enter your year")




# def sum1(*args):
#     return sum(args)
#
# total = sum1(10, 20, 10, 4)
# print(total)

# def hello(**kwargs):
#     hello(name="anish",salary=10000,address="nigeria",profession="software engr")
#     print(kwargs)

#Given a list of number,use a far loop
# and a function to return a list of even number{10,2,4,5,6,42,8,6,25,4,30,20}

def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
num_list=[10,2,4,5,6,42,8,6,25,4,30,20]
even_list = get_even_numbers(num_list)
print(even_list)

