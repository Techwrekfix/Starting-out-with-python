#This program writes a series of random numbers to a file
import random

def main():
    user_number = int(input('Specify how many random numbers the'\
                            ' the file should hold: '))
    #creating an output file
    user_file = open('random_numbers.txt', 'w')

    #using a loop to write user_number to file

    for count in range(user_number):
        random_number = random.randint(1,501)
        user_file.write(str(random_number) + '\n')
    user_file.close()
    print('The data has been written to random_numbers.txt')
main()
