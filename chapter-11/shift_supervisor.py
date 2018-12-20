#This program creates an object of the
#ShiftSupervisor class in particulars module

import particulars_class

def main():
    #Asking user to enter data for each of
    #the object's data attributes
    name = input('Enter name: ')
    number = input('Enter number: ')
    shift = int(input('Enter shift number(1 = Day or 2 = Night): '))
    pay_rate = float(input('Enter hourly pay rate: '))
    ann_salary = float(input('Enter annual salary: '))
    ann_bonus = float(input('Enter annual bonus: '))
    print()

    #Creating ShiftSupervisor object
    shift_supervisor = particulars_class.ShiftSupervisor(name,number,shift,pay_rate,\
                                                   ann_salary,ann_bonus)

    #Displaying the data entered
    print('Here is the data you entered.')
    print()
    print('Employee Name:',shift_supervisor.get_employee_name())
    print('Emplyee Number:',shift_supervisor.get_employee_number())
    print('Employee Shift Number:',shift_supervisor.get_shift_number())
    print('Hourly Pay Rate:',shift_supervisor.get_hourly_pay_rate())
    print('Annual Salary:',shift_supervisor.get_annual_salary())
    print('Annual Bonus:',shift_supervisor.get_annual_production_bonus())

main()
