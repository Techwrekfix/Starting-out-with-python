#This program is a money counting game
#Collecting data from userz
number_of_pennies = int(input('Enter the number of pennies: '))
number_of_nickles = int(input('Enter the number of nickles: '))
number_of_dimes = int(input('Enter the number of dimes: '))
number_of_quaters = int(input('Enter the number of quaters: '))
print()
#creating Variables
one_penny = 0.01
one_nickel = 0.05
one_dime = 0.1
one_quarter = 0.25

#Making calculations
penny_value = number_of_pennies *one_penny
nickle_value = number_of_nickles * one_nickel
dime_value = number_of_dimes *  one_dime
quarter_value = number_of_quaters * one_quarter

total_value = penny_value + nickle_value + \
              dime_value + quarter_value

#Determining the value
if total_value == 1.00:
    print('Congratulatons! you won the game because your money ' \
          'value of $',format(total_value,'.2f'), \
          ' is equal to $1',sep='')
elif total_value < 1.00:
    print('You loss the game because your money value of $' \
          ,format(total_value,'.2f'), ' is less than $1',sep='')
else:
    print('You loss the game because your money value of $' \
          ,format(total_value,'.2f'), ' is more than $1',sep='')
