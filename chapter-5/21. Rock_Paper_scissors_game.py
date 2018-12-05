#This program is a Rock, Paper,Scissors Game
import random

#defining some user choice variable
import random
def main():
    repeat = 'y'
    while repeat == 'y' or repeat == 'Y':
        intro()
        random_number = random.randrange(1,4)
        comm_choice = determine_comm_choice(random_number)

        user_choice = input('\nEnter a choice: ')
        while is_invalid(user_choice):  #Validating user_choice
            print('\nWrong input')
            user_choice = input('\nEnter a valid choice: ')
            
        print('\nComputer choice is',comm_choice)  #Displaying computer output
        determine_winner(comm_choice,user_choice)    
        repeat = input('\nEnter y or Y to repeat the game'\
                       ' or enter any key to exit the game: ')
#Defining the intro function
def intro():
    print('\nPick a choice of scissors, rock or paper')

#Defining determine computer choice function
def determine_comm_choice(random_number):
    if random_number == 1:
        comm_choice = 'rock'
    elif random_number == 2:
        comm_choice = 'paper'
    elif random_number == 3:
        comm_choice = 'scissors'
    return comm_choice

#Varifying user validation
def is_invalid(user_number):
    if user_number != 'rock' and user_number != 'paper' and \
       user_number != 'scissors':
        return True
    else:
        return False
    
#Determine a winner
def determine_winner(comm_choice,user_choice):
    while comm_choice == user_choice:
        random_number = random.randrange(1,4)
        comm_choice = determine_comm_choice(random_number)
        print(comm_choice)
        print('\nYou both made the same choice')
        user_choice = input('\nEnter a choice again: ')
        while is_invalid(user_choice):  #Validating user_choice
            print('\nWrong input')
            user_choice = input('\nEnter a valid choice: ')
        print('\nComputer choice is',comm_choice)
    
    if comm_choice == 'rock' and user_choice == 'scissors':
        print('\nComputer wins. The rock smashes scissors')
    elif comm_choice == 'scissors' and user_choice == 'rock':
        print('\nYou win. The rock smashes scissors')
    elif comm_choice == 'scissors' and user_choice == 'paper':
        print('\nComputer wins. Scissors cuts paper')
    elif comm_choice == 'paper' and user_choice == 'scissors':
        print('\nYou win. Scissors cuts paper')
    elif comm_choice == 'paper' and user_choice == 'rock':
        print('\nComputer wins. Paper wraps rock')
    elif comm_choice == 'rock' and user_choice == 'paper':
        print('\nYou win. Paper wraps rock')

main()
