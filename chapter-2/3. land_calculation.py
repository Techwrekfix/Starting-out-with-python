#This program calculates the number of acres in a tract

total_square_feet = float(input('Please enter the total ' \
                                'square feet of the tract' \
                                'of land: '))

number_of_acres = total_square_feet / 43560

#Displaying results

print('The number of acres in the tract of land is:' \
      ,format(number_of_acres, '.1f'))
