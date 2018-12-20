#This program imports Personal class module to create an object

import personal_information_class

def main():
    
    for count in range(3):
        print('Please enter your deatails.')
        name = input('\nPlease enter your name: ')
        address = input('Please enter your address: ')
        age = int(input('Please enter your age: '))
        number = int(input('Enter your phone number: '))
        print()
        #creating object
        entry = personal_information_class.Personal(name,address,age,number)

main()
