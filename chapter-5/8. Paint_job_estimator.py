#This program estimates a painting job
cost_per_hour = 35.00
base_hours = 8
def main():
    square_feet = float(input('Enter the number of square feet to be painted: '))
    price_per_gallon = float(input('Enter the price of a paint per a gallon: '))
    number_of_gallons = calculates_number_of_gallons(square_feet)
    hours_required = calculates_hours_required(square_feet)
    paint_cost = calculate_paint_cost(price_per_gallon,number_of_gallons)
    labor_charges = calculate_labor_charge(hours_required)
    grand_total = calculate_overal_total_cost(paint_cost,labor_charges)

    #Displaying the above data
    print('\nThe number of gallons of paint required = '\
          ,format(number_of_gallons,'.2f'),\
          ' gallons\nThe hours of labor required = '\
          ,format(hours_required,'.2f'),' hours'\
          '\nThe total cost of the paint = $',format(paint_cost,',.2f'),\
          '\nThe labor charges = $',format(labor_charges,',.2f'),\
          '\nThe total cost of the paint job = $',format(grand_total,',.2f')\
          ,sep='')

def calculates_number_of_gallons(square_feet):
    total_gallons = square_feet / 112
    return total_gallons

def calculates_hours_required(square_feet):
    hours = (square_feet * base_hours)/ 112                             
    return hours

def calculate_paint_cost(price_per_gallon,number_of_gallons):
    paint_cost = price_per_gallon * number_of_gallons
    return paint_cost

def calculate_labor_charge(hours):
    labor_charges = hours * cost_per_hour
    return labor_charges

def calculate_overal_total_cost(paint_cost,labour_charges):
    total_cost = paint_cost + labour_charges
    return total_cost

main()
