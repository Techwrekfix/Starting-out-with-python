#This program displays monthly sales tax

state_tax = 0.05
county_tax = 0.025

def main():
    total_sales = float(input('Enter the total sales for the month: '))
    county_sales_tax = calculate_county_sales_tax(total_sales)
    state_sales_tax = calculate_state_sales_tax(total_sales)
    total_sales_tax = calculate_total_sales_tax\
                      (county_sales_tax,state_sales_tax)

    #Displaying results
    print('\nCounty sales tax = $',format(county_sales_tax,',.2f'),\
          '\nState sales tax = $',format(state_sales_tax,',.2f'),\
          '\nTotal sales tax = $',format(total_sales_tax,',.2f'),sep='')

def calculate_county_sales_tax(total_sales):
    county_sales_tax = total_sales * county_tax
    return county_sales_tax

def calculate_state_sales_tax(total_sales):
    state_sales_tax = total_sales * state_tax
    return state_sales_tax

def calculate_total_sales_tax(county_sales_tax,state_sales_tax):
    total_sales_tax = county_sales_tax + state_sales_tax
    return total_sales_tax

main()
