#This program displays a software
#its discounts

#Asking the enter the number of packages purchased
quantity_purchased = float(input('Enter the number of packages ' \
                                  'purchased: '))
package_price = 99.0
sub_total = quantity_purchased * package_price

if quantity_purchased < 10:
    discount = 0
elif quantity_purchased < 20:
    discount = 0.1
elif quantity_purchased < 50:
    discount = 0.2
elif quantity_purchased < 100:
    discount = 0.3
else:
    discount = 0.4


#Calculating discount amount and total
discount_amount = sub_total * discount
total = sub_total - discount_amount

#Displaying results
print('\nYour discount amount = $',format \
      (discount_amount,',.2f'),'\nYour total amount after discount = $',\
      format(total,',.2f'),sep='')

