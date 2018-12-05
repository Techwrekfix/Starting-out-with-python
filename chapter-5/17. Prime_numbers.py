#This program determines wether a number is prime or not

#Checking if the integer entered is prime
def is_prime(integer):
    prime_division = 0
    if integer <= 1:
        return False
    for current_integer in range(1,integer + 1):
        if integer % current_integer == 0:
            prime_division += 1
            if prime_division > 2:
                return False
    else:
         return True

#Defining the main function to call other functions
def main():
    repeat = 'y'
    while repeat == 'y' or repeat == 'Y':
        number = int(input('Enter a possitive integer: '))

        if is_prime(number):
            print('\n',number,'is a prime number')
        else:
            print('\nSorry!',number,'is not a prime number')
            
        repeat = input('\nEnter y or Y to repeat the program, else press'\
                       ' any key to exit the program: ')

main()
