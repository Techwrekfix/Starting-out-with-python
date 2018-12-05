#This program calculates total sales of some items

#Collecting the price of each item
item1 = float(input('Please enter the price of Item 1: '))
item2 = float(input('Please enter the price of Item 2: '))
item3 = float(input('Please enter the price of Item 3: '))
item4 = float(input('Please enter the price of Item 4: '))
item5 = float(input('Please enter the price of Item 5: '))

#Calculating subtotal of the sale
subtotal = item1 + item2 + item3 + item4 + item5

#Calculating the amount of sales tax
sales_tax = subtotal * 0.07

#Calculating the total of the entire sale
total = subtotal + sales_tax

#Now displaying the results of the sales
print('The subtotal = $',subtotal, sep='')
print('The sales_tax = $',format(sales_tax,'.2f'), sep='')
print('The total of the sales = $',format(total,'.2f'),sep='')
