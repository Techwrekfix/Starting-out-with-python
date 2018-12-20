#This program keeps names and email addresses
#as key-value pairs

#Note: The program initially starts with an empty dictionary,
#      so you have to choose option 2 from the menu to add new
#      email addresses before you perform other options

import pickle

#Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Global constant for the filename
FILENAME = 'email.dat'

#Main function
def main():
    #Load the existing email dictionary and
    #assign it to mycontacts
    my_emails = load_emails()

    #Initialize a variable for the user's choice.
    choice = 0

    #Process menu selections until the user
    #wants to quit the program
    while choice != QUIT:
        #Get the user's menu choice
        choice = get_menu_choice()

        #Process user choice
        if choice == LOOK_UP:
            look_up(my_emails)
        elif choice == ADD:
            add(my_emails)
        elif choice == CHANGE:
            change(my_emails)
        elif choice == DELETE:
            delete(my_emails)
        else:
            print('Program quitting.....')
            print('Program quitted.')

        #Save the mycontacts dictionary to a file
        save_contacts(my_emails)

def load_emails():
    try:
        #open the condacts.dad file
        input_file = open(FILENAME, 'rb')

        #Unpickle the dictionary
        email_dict = pickle.load(input_file)
        
        #Close the phone_inventory.dat file
        input_file.close()

    #Handling the most likely exceptions to
    #be raised
    except FileNotFoundError:
        #Could not find the file, so create
        #an empty dictionary
        email_dict = {}
    except EOFError:
        #Could not open the file, so create
        #an empty dictionary
        email_dict = {}
    except IOError:
        #input or open error, so create
        #an empty dictionary
        email_dict = {}

    #Return the dictionary
    return email_dict

def get_menu_choice():
    print()
    print('Menu')
    print('-----------------------------')
    print('1. Look up email address')
    print('2. Add a new email address')
    print('3. Change an existing email address')
    print('4. Delete email address')
    print('5. quit the program')
    print()

    #Get the user's choice
    choice = int(input('Enter your choice: '))

    #Validate user choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    #return the user's choice
    return choice

def look_up(my_emails):
    #Get a name to look up:
    name = input('Enter a name: ').lower()

    #Look it up in the dictionary
    print(my_emails.get(name, 'Not found.'))
    
def add(my_emails):
    #Get a name and email address.
    name = input('Enter a name: ').lower()
    email = input('Enter email address: ')

    #If the name does not exist, add it.
    if name not in my_emails:
        my_emails[name] = email
        print('Name and email address added.')
    else:
        print('That entry already exists.')

def change(my_emails):
    #Get a name to look up
    name = input('Enter a name: ').lower()

    if name in my_emails:
        #Get a new email address
        email = input('Enter the new email address: ')

        #Update the entry
        my_emails[name] = email
        print('Email address change implemented')

    else:
        print('That name is not found')

def delete(my_emails):
    #Get name
    name = input('Enter a name: ').lower()

    #If the name is found, delete the entry
    if name in my_emails:
        del my_emails[name]
        print('Email address deleted')
    else:
        print('That name is not found')

#The save_contacts function pickles the specified
#object and saves it to the my_emails file.
def save_contacts(my_emails):
    #Open the file for writing
    output_file = open(FILENAME,'wb')

    #Pickle the dictonary and save it
    pickle.dump(my_emails, output_file)

    #close the file
    output_file.close()
    
main()
