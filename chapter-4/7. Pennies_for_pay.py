#Penny for pay

user_days = int(input('Enter the number of days: '))
print('\nNumber Of Days\tSalary($)')
print('--------------\t---------')
total = 0
penny_value = 0.01

for days in range(user_days):
    salary_formula = (2**days) * penny_value
    total += salary_formula
    print(days+1,'\t\t',salary_formula)

#Calculating total salary
print('\nTotal Salary = $',format(total,',.2f'),sep='')

    


