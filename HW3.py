# HW3.py
# Author: Daniel Flesch

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9

def squared(number_input) -> int:
    return number_input ** 2
   

def squared_number():
    user_input = int(input("Enter a number: "))
    answer1 = squared(user_input)
    print("Your number squared: ", answer1, "\n")

squared_number()

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"

#TODO HELP!!!!
# def question2(string, char, number_shift):
#    for i in string:
#         word_index = len(string)
#         if word_index == number_shift:
#             return char == i



# def question2_inputs():
#     word1 = input("Enter a string: ")
#     letter = input("Enter a letter: ")
#     numbered_shift = int(input("Enter a number: "))
    
#     result = question2(word1, letter, numbered_shift)
#     print(result)

# question2_inputs()

# Question 3:
# Write a function that takes in a number, a lower bound, and an upper bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True

def number_bounds(number, lower_bound, upper_bound):
    if number >= lower_bound and number <= upper_bound:
        return True
   
    else:
        return False
    
def bound_test():
    number1 = int(input("Enter a number: "))
    low_bound = int(input("Enter a lower bound: "))
    high_bound = int(input("Enter a higher bound: "))
    bounds = number_bounds(number1, low_bound, high_bound)
    print(bounds)

bound_test()

# Question 4:
# Write a function that asks the user for their name, age, and favorite color. Then write a function that accepts those three parameters and prints them out in a sentence
# IE. If the user inputs "John", 20, and "blue", the function should print "Hello, my name is John. I am 20 years old. My favorite color is blue."
# Hints: You will need to use the input() function to get the user's input. You will also need to use the str() function to convert the age to a string
# This is a two part question. You will need to write two functions
# remember in class we learned you can return miltiple values from a function
# also remember in class you can pass in pultiple variables into a function


def user_info(name, age, fav_color) -> str:
    print("Hello, my name is " + name + "." + " I am " + age + " years old." + " My favorite color is " + fav_color + ".")

def display_user_info():
    user_name = input("Enter a name: ")
    user_age = str(input("Enter a age: "))
    user_color = input("Enter a color: ")
    user_info(user_name, user_age, user_color)

display_user_info()

# Question 5:
# import the random module and use it to generate a random number between 1 and 100

import random
random_number = random.randint(1, 100)
print(random_number)

# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)

import math
sqrt_function =  math.sqrt(16)
print(sqrt_function)

# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)

import sys as python_version
print(python_version.version)


# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function

import os as os_info
print(os_info.getcwd())