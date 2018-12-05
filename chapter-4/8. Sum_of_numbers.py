#This program displays the sum of positive numbers
user_number = float(input('Enter any positve number or ' \
                          'negative number to quit: '))
total = 0.0 
while user_number >= 0:
    total += user_number
    user_number = float(input('\nEnter any positve number or ' \
                              'negative number to quit: '))
print('The sum =',total)
    
