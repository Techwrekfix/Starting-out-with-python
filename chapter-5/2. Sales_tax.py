#This program calculates sales tax
def main():
    
    amount_purchased = float(input('Please enter the amount purchased: '))

    #caculating state tax and county tax
    state_tax = calculate_state_tax(amount_purchased)

    county_tax = calculate_county_tax(amount_purchased)

    #calculating total sales tax
    total_tax = get_total_tax(state_tax, county_tax)

    #calculating total of the sale
    overal_total = calculate_overal_total(amount_purchased, total_tax)

    #displaying results
    print('The amount purchased = $',amount_purchased, sep='')
    print('The state sales tax = $',state_tax, sep='')
    print('The county sales tax = $',county_tax, sep='')
    print('The total sales tax = $',total_tax, sep='')
    print('The total of the sale = $',overal_total, sep='')

#Defining the state tax function
def calculate_state_tax(amount_purchased):
    state_tax = amount_purchased * 0.05
    return state_tax

#Defining the county tax function
def calculate_county_tax(amount_purchased):
    county_tax = amount_purchased * 0.025
    return county_tax

#Defining the total tax function
def get_total_tax(state_tax, county_tax):
    total_tax = state_tax + county_tax
    return total_tax

#Defining the overal total function
def calculate_overal_total(amount_purchased, total_tax):
    overal_total = amount_purchased + total_tax
    return overal_total

main()
