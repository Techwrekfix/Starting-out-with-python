#This program displays the total
#cost of a meal purchased at a restaurant

meal_charge = float(input('Enter the cost of the meal: '))

tip = 0.18 * meal_charge	#calculating 18% tip of the meal

sales_tax = 0.07 * meal_charge	 #calculating 7% sales tax of the meal

total = meal_charge + tip+sales_tax	#calculating total cost of the meal

#Displaying results
print('The 18% tip = $',format(tip, '.2f'),sep='')
print('The 7% sales tax = $',format(sales_tax, '.2f'),sep='')
print('The total cost of the meal = $',format(total,'.2f'),sep='')


