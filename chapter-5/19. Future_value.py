#This program calculates a compound interest on a savings account

def main():
    present_value = float(input("Enter the account's present value: "))
    interest = float(input('Enter monthly interest rate: '))
    months = int(input('Enter the number of months the money will'\
                       ' be left in the account: '))
    
    future_value = get_future_value(present_value,interest,months)

    print("The account's future value = $",\
          format(future_value,',.2f'),sep='')
    

def get_future_value(present,rate,months):
    future_value = present * (1+(rate/100))**months
    return future_value

main()
