#This program imports the Employee module class
#for employee management system

import employee_class
import pickle

#Naming global constants for menu choice
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Constant for file name
FILENAME = 'employee.dat'

def main():
    #Load the existing employees details dictionary
    #assign it to emp_details
    emp_details = load_employee_details()   #emp = employees

    choice = 0      #variable to control the loop

    #Process menu selections until the user
    #wants to quit the program
    while choice != QUIT:
        choice = menu_choice()

        #process the choice
        if choice == LOOK_UP:
            look_up(emp_details)
        elif choice == ADD:
            add(emp_details)
        elif choice == CHANGE:
            change(emp_details)
        elif choice == DELETE:

            delete(emp_details)
        else:
            print('Program quitted')

    #saving the program to a file
    save_program(emp_details)

def load_employee_details():
    #open employees file
    try:
        input_file = open(FILENAME,'rb')

        #unpickle the dictionary
        emp_file = pickle.load(input_file)

        #close the employee file
        input_file.close()

    except IOError:
        #could not open the file, so create
        #an empty dictionary
        emp_file = {}

    #return dictionary
    return emp_file

def menu_choice():
    print()
    print('\tMENU CHOICE')
    print('----------------------------')
    print('1. Look up employee')
    print('2. Add employee')
    print('3. Change existing employee')
    print('4. Delete existing employee')
    print('5. Quit program')
    print()

    #make a selection
    user_choice = int(input('Enter choice: '))

    #validate user choice
    while user_choice < LOOK_UP or user_choice > QUIT:
        user_choice = int(input('Invalid choie,Enter a valid choice: '))

    #return user choice
    return user_choice

def look_up(details):
    #since we are using employee ID as the key,
    #get employee's id_number to look it up
    id_number = input('Enter ID Number: ')

    #look it up in the dictionary
    print(details.get(id_number, 'That ID Number is not found.'))

def add(details):
    #get employee's info
    name = input('Name: ')
    id_number = input('ID Number: ')
    department = input('Department: ')
    title = input('Job Title: ')

    #create employee object named entry
    entry = employee_class.Employee(name,id_number,department,title)

    #If the ID Number does not exist in the dictionary,
    #add it as key with the entry objects as the value
    if id_number not in details:
        details[id_number] = entry

        print('The entry has been added.')
    else:
        print('That ID Number already exists.')

def change(details):
    #get id numbe
    id_number = input('Enter ID Number: ')

    #if id number is in dictionary,
    #provide new details
    if id_number in details:
        name = input('Enter the new name: ')
        department = input('Enter new department: ')
        title = input('Enter new title: ')

        #create employee object
        entry = employee_class.Employee(name,id_number,department,title)

        #updating the entry
        details[id_number] = entry
        print('information updated.')

    else:
        print('ID Number not found')

def delete(details):
    #get id number
    id_number = input('Enter ID Number: ')

    #if id number is in dictionary, delete it
    if id_number in details:
        del details[id_number]
        print('Entry deleted.')
    else:
        print('ID Number not found.')

def save_program(details):
    #open the file for writing
    output_file = open(FILENAME,'wb')

    #pickle the dictionary and save it
    pickle.dump(details, output_file)

    #close the file
    output_file.close()

main()
