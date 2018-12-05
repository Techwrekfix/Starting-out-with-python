#This program writes each player details
#in a Golf Club tournament

def main():
    try:
        repeat = 'y' #creating a loop to control the file
        #Create the file
        user_file = open('golf.txt', 'a')
        print('Enter the name and scores of all players involved')
        while repeat == 'y' or repeat == 'Y':
            name = input("\nEnter a Player's name: ")
            score = int(input("Enter a Player's score: "))

            #writing details to file
            user_file.write(name + '\n')
            user_file.write(str(score) + '\n')

            print('\nDo you want to add another record?')
            repeat = input('Y or y = yes, anything  else = no: ')

        user_file.close()
        print('The data has been written to golf.txt')
    except Exception as err:
        print(err)
main()
