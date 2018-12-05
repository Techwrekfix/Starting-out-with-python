#This prgram writes a series of numbers to a file

def main():
    repeat = 'y'
    user_file = open('numbers.txt', 'w')
    print('Enter a series  of integers as many as you can.')
    while repeat == 'y' or repeat == 'Y':
        number = int(input('\nEnter an integer: '))

        user_file.write(str(number) + '\n')
        
        print('\nDo you want to add another integer?')
        repeat = input('Y or y = yes, anything  else = no: ')
    user_file.close()
    print('Data has been written to numbers.txt')
main()
