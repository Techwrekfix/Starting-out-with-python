#This program calculates monthly and yearly automobile cost
def main():
    loan_payment,insurance,gas,oil,tires,maintenance = get_expenses()
    
    monthly_cost = calculate_monthly_cost(loan_payment\
                   ,insurance,gas,oil,tires,maintenance)
    
    yearly_cost = calculate_yearly_cost(monthly_cost)
    
    print('\nThe monthly automobile cost = $',format(monthly_cost,',.2f'),\
          '\nThe yearly automobile cost = $'\
          ,format(yearly_cost,',.2f'),sep='')

def get_expenses():
    loan_payment = float(input('Enter the monthly cost of loan payment: '))
    insurance = float(input('Enter monthly insurance cost: '))
    gas = float(input('Enter the monthly cost of gas: '))
    oil = float(input('Enter the monthly cost of oil: '))
    tires = float(input('Enter the monthly cost of tires: '))
    maintenance = float(input('Enter the monthly cost of maintenance: '))
    return loan_payment,insurance,gas,oil,tires,maintenance

def calculate_monthly_cost(loan_payment,insurance,gas,oil,tires,maintenance):
    monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    return monthly_cost

def calculate_yearly_cost(monthly_cost):
    yearly_cost = monthly_cost * 12
    return yearly_cost

main()
    
