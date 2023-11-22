# HW8.py
# Author: Daniel Flesch

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)
import datetime as dt
import streamlit as st

# # Streamlit title, subtitle, date, and button
st.title("Day Calculator")

st.subheader("Displays the amount of days until the date entered.")

user_input = st.date_input("Enter a date:", format='MM/DD/YYYY')

button = st.button("Calculate ")


# The calculate_days function from Lab9.py

def calculate_days(date) -> int:

    today = dt.datetime.now().date()
    days = (date - today).days
    if days < 0:
        raise ValueError("Invalid date, date is in the past.")
    return days



# # START OF HOMEWORK Questions

# # 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.
def calculate_days_until_birthday():
    daysbirthday = calculate_days(user_input)
    return daysbirthday

# # 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# # Hint: You can use the date object to create a date for the end of the semester. IE.
def days_until_semester_ends(date):
    end_of_semester = dt.date(2023, 12, 8)
    semester_days = (end_of_semester - date).days
    return semester_days
semester_button = st.button("Calculate Days of Semester Left")
# # 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# # of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# # an emoji of a party popper in the Streamlit app.
# # Hint: You can use the date object to create a date for New Years. IE. 
# # Hint: To add an emoji, use the st.write() function. IE. st.write("🎊🗿🎉")

def days_until_new_years(date):
    new_years = dt.date(2024, 1, 1)
    new_years_days = (new_years - date).days
    return new_years_days


new_years_button = st.button("Calculate 🎊🗿")

# # 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# # days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.

current_date = dt.datetime.now().date()
# # Hint: You can use the st.button() function. IE. button = st.button("Click me")
# # Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# # IE. current_date = dt.datetime.now().date()
# # Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# # app function from Lab9.py
def app():
    if button:
        try:
            result = calculate_days_until_birthday()

        except ValueError:
            st.write("Please enter a valid date.")
            return

        st.write(f"There are {result} days until your birthday 🎊🎉")

    if semester_button:
        try:
            semester_results = days_until_semester_ends(current_date)
        except ValueError:
            st.write("Please enter a valid date.")
            return
        st.write(f"There are {semester_results} until the semester ends.")

    if new_years_button:
        try:
            new_year_result = days_until_new_years(user_input)
        except ValueError:
            st.write("Please enter a valid date.")
            return

        st.write(f"There are {new_year_result} days until the new year 🎉")


if __name__ == '__main__':
    app()