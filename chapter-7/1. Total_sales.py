#This program writes and display a store's sales for
#each day of the week and displays the total of the sales

def main():
    num_days = int(input('Specify the number of days'\
                         ' you want to enter sales: '))
    print()
    sales = get_sales(num_days)
    total = calculate_total(sales)
    print_details(sales,total)

def get_sales(num_days):
    #creating a list to hold sales
    sales = [0] * num_days

    #adding sales to list
    for index in range(len(sales)):
        print('Enter sales amount for day',index + 1,end='')
        sales[index] = float(input(': '))
    return sales

def calculate_total(sales):
    total = 0   #initiating accumulator
    
    for index in sales:
        total += index
    return total
        
def print_details(sales, total):
    print('\nThe sales entered are :',sales)
    print('\nAnd the total of the sales = $',format(total,',.2f'),sep='')
    
main()
