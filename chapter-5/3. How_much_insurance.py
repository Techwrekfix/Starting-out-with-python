#This program calculates minimum amount of insurance
#a user needs to buy for a property

def main():
    replacement_cost = get_replacement_cost()
    minimum_amount = calculate_minimum_amount(replacement_cost)
    #Displaying the minimum amount of insurance
    print('The minimum amount of insurance to be paid = $',\
          format(minimum_amount,',.2f'),sep='')

#Defining the replacement cost
def get_replacement_cost():
    cost = float(input('Enter the replacement cost of the property: '))
    return cost
#Defining  the minimum amount
def calculate_minimum_amount(replacement_cost):
    minimum = 0.8 * replacement_cost
    return minimum
main()
