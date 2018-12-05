#This program is an Alphabetic Telephone Number Transaltor

#ALGORITHM in pseudocode

#1. An alpha_translator function accepts a phone number
#   as an argument
#   create an empty string variable to accumulate any character
#   that appears in phone number and is equal to question characters
#   for every character in phone number:
#       if phone character equals any of the question characters:
#           phone character equals question character
#        repeat the if process till every question character equals
#         phone number
#   display results
#2.the main fucntion:
#   prompt user to enter a telephone number in the format
#   555-xxx-xxx
# alpha_translator receives user_input as an argument

#CODE

def alpha_translator(phone_number):
    phone_number = phone_number.upper()
    phone_translate = ''
    for char in phone_number:
        if char == 'A' or char == 'B' or char =='C':
            char = '2'
        elif char == 'D' or char == 'E' or char == 'F':
            char = '3'
        elif char == 'G' or char == 'H' or char == 'I':
            char = '4'
        elif char == 'J' or char == 'K' or char == 'L':
            char = '5'
        elif char == 'M' or char == 'N' or char == 'O':
            char = '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            char = '7'
        elif char == 'T' or char == 'U' or char == 'V':
            char = '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            char = '9'
        phone_translate += char
    print('Here is the full telephone number:',phone_translate)

def main():
    user_input = input('Enter a 10-character telephone number'\
                       'in the format 555-xxx-xxxx: ')
    alpha_translator(user_input)

main()
            
 
