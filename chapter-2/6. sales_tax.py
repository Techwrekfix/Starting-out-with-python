#This program calculates sales tax

amount_purchased = float(input('Please enter the amount purchased: '))

#caculating sales tax
state_tax = amount_purchased * 0.05

county_tax = amount_purchased * 0.025

#calculating total sales tax
total_sales_tax = state_tax + county_tax

#calculating total of the sale
total = amount_purchased + total_sales_tax

#displaying results
print('The amount purchased = $',amount_purchased, sep='')
print('The state sales tax = $',state_tax, sep='')
print('The county sales tax = $',county_tax, sep='')
print('The total sales tax = $',total_sales_tax, sep='')
print('The total of the sale = $',total, sep='')
