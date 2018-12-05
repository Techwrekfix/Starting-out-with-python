#This program calculates the amount generated from ticket sales

def main():
    class_A = float(input('Enter the number of ticket sales in Class A: '))
    class_B = float(input('Enter the number of ticket sales in Class B: '))
    class_C = float(input('Enter the number of ticket sales in Class C: '))
    ticket_A = get_number_of_class_A_tickets(class_A)
    ticket_B = get_number_of_class_B_tickets(class_B)
    ticket_C = get_number_of_class_C_tickets(class_C)
    total = get_amount_of_ticktes_sold(ticket_A,ticket_B,\
                                                        ticket_C)
    #Displaying total amount of tickets sold
    print('\nTotal income for tickets sold = $',format(total,',.2f'),sep='')

def get_number_of_class_A_tickets(class_A):
    class_A_tickets_sold = class_A * 20
    return  class_A_tickets_sold

def get_number_of_class_B_tickets(class_B):
    class_B_tickets_sold = class_B * 15
    return class_B_tickets_sold

def get_number_of_class_C_tickets(class_C):
    class_C_tickets_sold = class_C * 10
    return  class_C_tickets_sold

def get_amount_of_ticktes_sold(ticket_A,ticket_B,ticket_C):
    total_amount = ticket_A + ticket_B + ticket_C
    return total_amount

main()
