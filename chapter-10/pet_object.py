#This program imports the Pet class for use

import pet_class

def main():
    #Asking user for pet's details
    name = input('Enter the name of the Pet: ')
    pet_type = input('Enter the type of animal Pet: ')
    age = int(input('Enter the age of the Pet: '))

    #Creating an object of the Pet class
    pet_details = pet_class.Pet(name,pet_type,age)

    #displaying user's entries
    print('Pet Name:',pet_details.get_name())
    print('Pet Type:',pet_details.get_animal_type())
    print('Pet Age: ',pet_details.get_age(),'year(s)',sep='')
    
main()
    
