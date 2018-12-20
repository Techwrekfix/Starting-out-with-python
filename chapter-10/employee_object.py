#This program creates objects from the Employee class

import employee_class

def main():

    employees_details = create_object_list()
    display_employees_details(employees_details)

def create_object_list():
    #Create an empty list to hold the ojbects
    employee_list = []
    #Enter the particulars of the employees
    for count in range(3):
        print('Provide particulars for Employee #',count + 1,sep='')
        name = input('Enter Name: ')
        number = input("Enter ID Number: ")
        department = input('Enter Department: ')
        title = input('Enter Job Title: ')
        print()

        #creating three objects of the class
        employees = employee_class.Employee(name,number,department,title)

        #append the objects to the list
        employee_list.append(employees)

    #return employee_list
    return employee_list

def display_employees_details(details):
    #Iterating over details to display employees details
    print('Here are the Employees details.')
    for items in details:
        print('Name:',items.get_name())
        print('ID Number:',items.get_ID_number())
        print('Departmen:',items.get_department())
        print('Job Title:',items.get_job_title())
        print()
    
main()
