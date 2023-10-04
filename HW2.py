# HW2.py
# Author: Daniel Flesch


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

age_input = int(input("How old are you? "))
if(age_input < 13):
    print("You are a child.")
elif(age_input in range(13, 20)):
    print("You are a teenager.")
else :
    print("You are an adult.")

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."

# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345

for i in range(6):
    if i == 1:
        print("1")
    elif i == 2:
        print("12")
    elif i ==3:
        print("123")
    elif i ==4:
        print("1234")
    elif i ==5:
        print("12345")

    
# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

total = 0
highest_number = 0
lowest_number = 0

for i in range(10):
    number_input = int(input("Enter 10 Numbers: "))
    total += int(number_input)
    if i == 0:
        lowest_number = number_input
    elif number_input < lowest_number:
        lowest_number = number_input
    elif number_input > highest_number:
        highest_number = number_input
    

average_number = (total / 10)

print("Highest Number: ", highest_number)
print("Lowest Number: ", lowest_number)
print("Average:", average_number)

# The highest number.
# The lowest number.
# The average of all the numbers.

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i,  o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

user_input = input("Enter a string: ")
user_input1 = user_input.lower()
vowels = set("aeiou")
vowel_counter = 0

for letter in user_input1:
    if letter in vowels:
        vowel_counter += 1
print(vowel_counter)