#This program calculates some stock transaction

shares_purchased = 2000
price_per_buying_share = 40.00
purchasing_amount = shares_purchased * price_per_buying_share
broker_commission = purchasing_amount * 0.03

#Two weeks later
shares_sold = 2000
price_per_selling_share = 42.75
selling_amount = shares_sold * price_per_selling_share
broker_commission_2 = selling_amount * 0.03

#calculating total commission and amount left
total_broker_commission = broker_commission + broker_commission_2
amount_left = selling_amount - (purchasing_amount + total_broker_commission)

#displaying results
print('Money paid for the Stock = $',\
      format(purchasing_amount,',.2f'), sep='')
print('Commission paid for buying shares = $', \
      format(broker_commission,',.2f'),sep='')
print('The selling amount of the stock = $',\
      format(selling_amount,',.2f'),sep='')
print('Commission paid for selling stock = $',\
      format(broker_commission_2,',.2f'),sep='')
print('The amount left = $',format(amount_left,'.2f'),sep='')
