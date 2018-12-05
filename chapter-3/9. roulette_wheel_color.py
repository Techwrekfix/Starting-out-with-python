#This program displays roulette wheel Colors.

#Collecting data from the user

pocket_number = int(input('Enter a pocket numbber: '))
print()
#Determine the color
if pocket_number < 0 or pocket_number > 36:
        print('Error: please enter a number from 0 to 36')
elif pocket_number == 0:
        print('The pocket color is green')
elif pocket_number < 11:
    if pocket_number % 2 != 0:
        print('The pocket number is red')
    else:
        print('The pcoket number is black')
elif pocket_number < 19:
    if  pocket_number % 2 != 0:
        print('The pocket number is black')
    else:
        print('The pocket number is red')
elif pocket_number < 29:
    if pocket_number % 2 != 0:
        print('The pocket number is red')
    else:
        print('The pocket number is black')
elif pocket_number < 37:
    if  pocket_number % 2 != 0:
        print('The pocket number is black')
    else:
        print('The pocket number is red')

