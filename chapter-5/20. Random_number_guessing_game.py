#This program is about a random number guessing game

import random

def main():
    print('Guess a number from 1 to 100 to determine if you are correct')
    repeat = 'y'
    while repeat == 'y' or repeat == 'Y':
       
        random_number = random.randrange(1,101)
        user_guess = int(input('\nPlease enter the number you guessed: '))
        determine_user_guess(random_number,user_guess)
        
        repeat = input('\nEnter y or Y to repeat the game, else enter'\
                   ' any key to quit the game: ')
    


#Defining determine user guess
def determine_user_guess(random_number,user_guess):
    guess_count = 1 #This keeps count of the user number of guesses
                    #and the user has alrady entered a number in the
                    #main function hence, guess_count = 1

    while user_guess != random_number:
        if user_guess > random_number:
            print('Too high, try again',end='')
            user_guess = int(input(': '))
        elif user_guess < random_number:
            print('Too low, try again',end='')
            user_guess = int(input(': '))
        guess_count += 1
    print('\nCongratulations, you guessed right')
    print('\nYou guessed',guess_count,'times')
   
main()


    
