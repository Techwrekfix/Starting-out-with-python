#This program creates an object of the
#ProductionWorker class in particulars module

import particulars_class

def main():
    #Asking user to enter data for each of
    #the object's data attributes
    name = input('Enter name: ')
    number = input('Enter number: ')
    shift = int(input('Enter shift number(1 = Day or 2 = Night): '))
    pay_rate = float(input('Enter hourly pay rate: '))
    print()

    #Creating ProductionWorker object
    production_worker = particulars_class.ProductionWorker(name,number,shift,
                                                     pay_rate)

    #Displaying the data entered
    print('Here is the data you entered.')
    print()
    print('Employee Name:',production_worker.get_employee_name())
    print('Emplyee Number:',production_worker.get_employee_number())
    print('Employee Shift Number:',production_worker.get_shift_number())
    print('Hourly Pay Rate:',production_worker.get_hourly_pay_rate())

main()
