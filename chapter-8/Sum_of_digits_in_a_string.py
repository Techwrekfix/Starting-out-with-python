#This program displays the sum of digits in a string

#ALGORITHM in pseudocode

#1. get a series of single-digit number from the user
#   set total accumulator to zero
#2. for every digit in user input:
#       convert digit to integer
#       add the digit to the accumulator
#3. Display total

#CODE

def main():
    user_input = input('Enter a series of single-digit number: ')
    total = 0   #accumulator
    for digits in user_input:
        digits = int(digits)
        total += digits

    print('The total of',user_input,'is:',total)

main()
        
