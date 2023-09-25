# HW1.py
# Author: Daniel Flesch

# Question 1:
# Print Hello World like we did in class
print("Hello World")
# Question 2:
# Print the following:
# Your name
print("Daniel Flesch")

# Your age
print(18)

# Your favorite color
print("Blue")

# Your favorite animal
print("Dog")

# Question 3:
# Create a variable called "myName" and set it equal to your name
myName = "Daniel Flesch"
# Create a variable called "myAge" and set it equal to your age
myAge = 18
# Create a variable called "myColor" and set it equal to your favorite color
myColor = "Blue"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "Dog"
# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>
print("Hello my name is " + myName, end="\n")
print("I am ", myAge, end=" years old \n")
print("My favorite color is", myColor, end="\n")
print("My favorite animal is", myAnimal, end="\n")

# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2+2)
# 3 * 4
print(3*4)
# 5 - 6
print(5-6)
# 8 / 2
print(8/2)
# Question 5:
# Create a variable called "num1" and set it equal to 2
num1 = 2
# Create a variable called "num2" and set it equal to 3
num2 = 3
# Create a variable called "num3" and set it equal to 4
num3 = 4
# Create a variable called "num4" and set it equal to 5
num4= 5
# Calculate the following and print the result:
# num1 + num2
print( num1 + num2)
# num3 * num4
print(num3 * num4)
# num4 - num1
print(num4 - num1)
# num2 / num1
print(num2 / num1)
# Question 6: Write a program that asks the user for their name and then prints the following:
print("Hello,", input("What is your name? "))

# Hello, <name>. Please enter three numbers.

threeNumbers1 = float(input("Please enter three numbers(1/3): "))
threeNumbers2 = float(input("Please enter three numbers(2/3): "))
threeNumbers3 = float(input("Please enter three numbers(3/3): "))
# The program should then ask the user for three numbers (floats) and print the following:


# 1. The sum of the three numbers is <sum>
print("The sum of the three numbers is ", threeNumbers1+threeNumbers2+threeNumbers3)
# 2. The product of the three numbers is <product>
print("The product of the three numbers is ", threeNumbers1 * threeNumbers2 * threeNumbers3)
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
rounded1 = round(threeNumbers1)
rounded2 = round(threeNumbers2)
rounded3 = round(threeNumbers3)

three_average = int(rounded1 + rounded2 + rounded3) / 3
# 4. The average of the three numbers is <average>
print("The average of the three numbers is ", three_average)

# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
symbol = input("Enter a symbol: ")
print("\t", symbol, "\t /")
print("       ", (symbol *3), "\t /")
print("      ", (symbol *5), "\t /")
print("     ", (symbol *7), "\t /")
print("      ", (symbol *5), "\t /")
print("       ", (symbol *3), "\t /")
print("\t", symbol, "\t /")

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
