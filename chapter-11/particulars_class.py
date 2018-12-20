#This proram represents Employee and
#ProductionWorker classes

class Employee:
    #The init method accepts arguments for
    #employee name an employee number

    def __init__(self,employee_name,employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    #The following methods are mutators for
    #the data attributes

    def set_employee_name(self,employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self,employee_number):
        self.__employee_number = employee_number

    #The followng methods are accessors for
    #the data attributes

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

#Next is the ProductionWorker class
#which inherits the Employee class

class ProductionWorker(Employee):
    #The init method accepts arguments for the
    

    def __init__(self,employee_name,employee_number,
                 shift_number,hourly_rate):
        #Calling the superclass init method
        Employee.__init__(self,employee_name,employee_number)

        #Initializing the __shift_number and hourly_rate attributes
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

    #The following methods are mutators for the data attriubtes

    def set_shift_number(self,shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self,hourly_rate):
        self.__hourly_rate = hourly_rate

    #The following methods are accessors for the data attributes

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_rate   

#Next is ShiftSupervisor class which also
#inherits the ProductionWorker class

class ShiftSupervisor(ProductionWorker):
    #The init method accepts arguments for the
    #employee name,employee number,shift number,
    #and hourly pay rate,annual salary and
    #annual production bonus

    def __init__(self,employee_name,employee_number,
                 shift_number,hourly_rate,annual_salary,annual_bonus):
        #Calling the ProductionWorker init method
        ProductionWorker.__init__(self,employee_name,employee_number,
                 shift_number,hourly_rate)

        #Initializing the __annual_salary and __annual bonus attributes
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    #The following methods are mutators for the data attributes

    def set_annual_salary(self,annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_production_bonus(self,annual_bonus):
        self.__annual_bonus = annual_bonus

    #The following methods are accessors for the data attributes

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_production_bonus(self):
        return self.__annual_bonus
