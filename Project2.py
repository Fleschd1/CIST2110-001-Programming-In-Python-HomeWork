# Project 2
# Name: Daniel Flesch
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit
# Import the csv module, datetime module
import csv
import datetime as dt
from tabulate import tabulate
# import pandas as pd
# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("Welcome to the Contact List Program \n")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:

# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.
reader = csv.reader(open("contacts.csv"))
contact = {}

def import_csv(file):
    """ Imports contacts from csv file
    
    Args: 
        file: csv file to be imported

    Returns:
        contact: dictionary of contacts
    """
    #This organizes the information into a dictionary for each person's contact information
    global contact
    next(file)
    try:
        for row in reader: 
            contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y' )}

        return contact
    except FileNotFoundError:
        return "File does not exist."


# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]
def add_contact(name, phone, email, birthday):
    """ 
    Adds a contact as a dictionary to the contacts list.
    
    Args: name, phone, email, birthday

    Returns: true (the contact was added)
            false (contact is already in the list)
    """

    birthday = dt.datetime.strptime(str(birthday), '%m/%d/%Y')

    if name in contact:
        print("Contact already exists")
        return False
    else:
        contact[name] = {'Phone': phone, 'Email':email, 'Birthday':birthday}
        print("Contact added successfully.""\n")

        return True
        
    
# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.
def view_contacts():
    """
   Displays all of the contacts in a nice table.

   Args: None

   Return: Cool table
   """
    contacts_list = [{'Name': name, 'Phone': info['Phone'], 'Email': info['Email'], 'Birthday': info['Birthday'].strftime('%m/%d/%Y')} for name, info in contact.items()]
    print(tabulate(contacts_list, headers="keys", tablefmt="fancy_grid"))

    return contacts_list

# delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.
def delete_contact(id):
    """
    Deletes a contact from the contact list.
    Args: id (name of contact to delete)
    Return: true (contact was deleted)
    """
    if id in contact:
        contact.pop(id)
        print("Contact deleted.""\n")
        return True

        
    else:
        print("Contact does not exist")
        return False

# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.
def next_birthday():
    """
    Displays the next birthday in the list.
    Args: None
    Return: None
    """
    today = dt.datetime.today()

    for key, value in contact.items():
        birthday = dt.datetime(today.year, value["Birthday"].month, value["Birthday"].day)
        if 0 <= (birthday - today).days <= 30:
            print(f"{key} has a birthday in the next 30 days.\n")
            break
    else:
        print("No birthdays in the next 30 days.")

    # if there are no contacts in the dictionary, display a message
    # if there are no birthdays in the next 30 days, display a message
    # if there is a birthday in the next 30 days, display the next birthday and name
    # use string formatting to display the next birthday
    # the next birthday should be sorted by the next birthday
    # the next birthday should be formatted as mm/dd/yyyy
# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.
def save_csv(filename):
    """
    Saves the contact to the csv file, 
    Args: filename
    Return: true (contacts were saved)
    """
    try: 
        file = input("Enter a filename to save the contacts to: ")
        with open(file, "w") as file:
            writer = csv.writer(file) #creates the writer object
            writer.writerow(["Name", "Phone", "Email", "Birthday"]) #writes the row
            for key, value in contact.items():
                writer.writerow([key, value["Phone"], value["Email"], value["Birthday"]])
        print("Contacts saved successfully.""\n")
        return True
    
    except FileNotFoundError:
        print("File does not exist.")
        return False
        

    #if the file exists, overwrite the file
    #if the file does not exist, create the file
    #return true if the contacts were saved and false if the contacts were not saved


# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.
def main_menu():
    """Displays the menu and gets the user's choice"""
    print("\n""1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Save contacts to csv file")
    print("5. Next Birthday")
    print("0. Quit""\n")
    global choice
    choice = int(input("Enter your choice: "))
    return choice        # add_contact()

          
def main():
    """
        Calls the functions and runs the program
        """    
    import_csv(reader)
    while True:
       
        main_menu()

        if choice == 1:
            add_contact("Daniel", "123-456-7890", "daniel@gmail", "01/01/2000")
        if choice == 2:
            view_contacts()
        if choice == 3:
            delete_contact("Daniel")
        if choice == 4:
            save_csv("contacts.csv")
        if choice == 5:
            next_birthday()
        if choice == 0:
            break
        elif choice > 5 or choice < 0:
            print("\n""Invalid choice. Try again.""\n")
            continue
    # After you are done with the program, answer the following questions using code (show your code and output):
def last_questions():

    print("\n""How many yahoo emails are there?")
    count_yahoo = 0
    for key, value in contact.items():
        if "yahoo.com" in contact[key]["Email"]:
            count_yahoo += 1
    print(f"{count_yahoo} emails are yahoo emails.\n")

    print("How many .org emails are there?")
    count_org = 0
    for key, value in contact.items():
       if ".org" in contact[key]["Email"]:
        count_org += 1
    print(f"{count_org} .org emails are there.\n")

    print("How many contacts have a birthday in January?")
    count_month = 0
    for key, value in contact.items():
        month = contact[key]["Birthday"].strftime("%m")
        if month == "01":
            count_month += 1
    print(f"{count_month} contacts have a birthday in January.\n")

if __name__ == "__main__":
    main()
    last_questions()