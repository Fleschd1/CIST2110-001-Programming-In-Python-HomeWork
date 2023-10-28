# HW5.py
# Author: Daniel FLesch

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
print("___Question 1___" + "\n")
foods_list = ["grilled chicken", "rice", "tacos", "quesadilla", "potatoes"]
print(foods_list)
print("\n")

# Question 2: Using the list from question 1, print the first and last element of the list
print("___Question 2___" + "\n")
print(foods_list[0],"and", foods_list[-1])
print("\n")

# Question 3: Using the list from question 1, print the 3rd element of the list
print("___Question 3___" + "\n")
print(foods_list[2])
print("\n")

# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print("___Question 4___" + "\n")
print(foods_list[0:3])
print("\n")

# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print("___Question 5___" + "\n")
print(foods_list[3:5])
print("\n")

# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
print("___Question 6___" + "\n")
for i in foods_list:
    print(i)
print("\n")

# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
print("___Question 7___" + "\n")
foods_list.reverse()
for i in foods_list:
    print(i)
print("\n")

# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
print("___Question 8___" + "\n")
for i in enumerate(foods_list):
    print(i)
print("\n")

# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
print("___Question 9___" + "\n")
list = [[1,2,3],[4,5,6],[7,8,9]]
print(list[1][0])
print("\n")

# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
print("___Question 10___" + "\n")
the_list = [1, 2, 3, 4, 5]

def user_list(list_input):
    list_input.reverse()
    print(list_input)

user_list(the_list)
print("\n")