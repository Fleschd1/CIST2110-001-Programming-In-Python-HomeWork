# Project1.py
# Author: Daniel Flesch


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.
SCORE = 0
START="y"

# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome_msg():
    print("Welcome to the Trivia Game" + "\n")

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
def ask_question(question, correct_answer, option1, option2, option3, option4):
    
    print(question)
    print("a. "+ option1)
    print("b. "+ option2)
    print("c. "+ option3)
    print("d. "+ option4)
    answer_choice = input("Your answer? ").strip()
    options = "a", "b", "c", "d"
    if answer_choice in options:
        if answer_choice == correct_answer:
            global SCORE 
            SCORE += 1
            return True

    
        elif answer_choice in options: 
         print("\n" + "Incorrect answer. The correct answer is : " + correct_answer + "\n")
        return False
    
    else:
        print("Invalid answer. Try again." + "\n")
        exit()


def question1():
    question = "What is Stockton's mascot?"
    correct_answer = "c"
    answer1 = ask_question(question, correct_answer, "Eagle", "Crow", "Osprey", "Ostrich")

    if answer1 == True:
        print("\n" + "Correct!!")
        print("+1 Point, good job!" + "\n")
        
    else:
        return False
        


def question2():
    question = "What is Mr. Walsh's first name?"
    correct_answer = "a"
    answer1 = ask_question(question, correct_answer, "Greg", "Geff", "Grog", "Jonathan")

    if answer1 == True:
        print("\n" + "Correct!!")
        print("+1 Point, good job!" + "\n")

    else:
        return False
        

def question3():
    question = "Which of the following are CPU brands?"
    correct_answer = "b"
    answer1 = ask_question(question, correct_answer, "Nvidia", "Intel", "Windows", "HP")

    if answer1 == True:
        print("\n" + "Correct!!")
        print("+1 Point, good job!" + "\n")

    else:
        return False
    

def question4():
    question = "Which of the following are search engines?"
    correct_answer = "d"
    answer1 = ask_question(question, correct_answer, "Microsoft", "Chrome", "Apple", "Google")

    if answer1 == True:
        print("\n" + "Correct!!")
        print("+1 Point, good job!" + "\n")

    else:
        return False
    

def question5():
    question = "What color is the planet Mars?"
    correct_answer = "a"
    answer1 = ask_question(question, correct_answer, "Orange", "Purple", "Blue", "Grey")

    if answer1 == True:
        print("\n" + "Correct!!")
        print("+1 Point, good job!" + "\n")

    else:
        return False
    

def total_score():
    global SCORE
    
    print("Thanks for playing.")
    print("Your score: " + str(SCORE) + "/5")

    
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:        

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).

def main_menu() -> str:
    menu_choice = input("Are you ready to start? y / n: ")
    if menu_choice == START:
            question1()
            question2()
            question3()
            question4()
            question5()
            total_score()
            
    elif menu_choice == "n":
            print("Goodbye")
            exit()
    elif menu_choice != "y" or "n":
            print("Invalid Input")
            main_menu()


def main():
    welcome_msg()
    main_menu()

if __name__ == "__main__":
    main()