#This program converts a user string into morse code

#ALGORITHM in pseudocode

#The main function:
#   1.get a string from the user
#   2.morse code converter function accepts
#     string an argurment
#The morse code converter function(string):
#   1.converts all alphabetic letters in string
#     to uppercase
#   2. set an empty string variable to concatenate the morse code
#   3.a loop steps through the string concatenating each
#     character's morse code to the variable above(using += operator)
#           4.for every character in string:
#               5.if character equals each of the characters in
#               in the question(see question for the characters:
#                    add the character's morse code to the variable
#               6. repeat number 5 using elif to run each character
#                   in the string against each character in the question
#                   and adding its morse code to the variable


#CODE

def main():
     user_string = input('Enter a statement to convert to morse code: ')

     morse_code_converter(user_string)

def morse_code_converter(user_string):
    string = user_string.upper()
    morse = ''

    for char in string:
        if char == ' ':
            morse += ' '
        elif char == ',':
            morse += '--..--'
        elif char == '.':
            morse += '.-.-.-'
        elif char == '?':
            morse += '..--..'
        elif char == '0':
            morse += '-----'
        elif char == '1':
            morse += '.----'
        elif char == '2':
            morse += '..---'
        elif char == '3':
            morse += '...--'
        elif char == '4':
            morse += '....-'
        elif char == '5':
            morse += '.....'
        elif char == '6':
            morse += '-....'
        elif char == '7':
            morse += '--...'
        elif char == '8':
            morse += '---..'
        elif char == '9':
            morse += '----.'
        elif char == 'A':
            morse += '.-'
        elif char == 'B':
            morse += '-...'
        elif char == 'C':
            morse += '-.-.'
        elif char == 'D':
            morse += '-..'
        elif char == 'E':
            morse += '.'
        elif char == 'F':
            morse += '..-.'
        elif char == 'G':
            morse += '--.'
        elif char == 'H':
            morse += '....'
        elif char == 'I':
            morse += '..'
        elif char == 'J':
            morse += '.---'
        elif char == 'K':
            morse += '-.-'
        elif char == 'L':
            morse += '.-..'
        elif char == 'M':
            morse += '--'
        elif char == 'N':
            morse += '-.'
        elif char == 'O':
            morse += '---'
        elif char == 'P':
            morse += '.--.'
        elif char == 'Q':
            morse += '--.-'
        elif char == 'R':
            morse += '.-.'
        elif char == 'S':
            morse += '...'
        elif char == 'T':
            morse += '-'
        elif char == 'U':
            morse += '..-'
        elif char == 'V':
            morse += '...-'
        elif char == 'W':
            morse += '.--'
        elif char == 'X':
            morse += '-..-'
        elif char == 'Y':
            morse += '-.-'
        elif char == 'Z':
            morse += '--..'
    print('The morse code equivalent of your input is:',morse)
main()
