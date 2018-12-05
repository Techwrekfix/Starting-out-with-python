#This program displays the total number of bugs
#of a bug collector during five days
total = 0
for counter in range(5):
    print('Enter number of bugs for day',counter+1,end='')
    number_of_bugs = int(input(': '))
    total += number_of_bugs
#Display results
print('\nThe total number of bugs collected during five days =',total)
